from flask import render_template, request, redirect, url_for, flash, session
from models import Cliente, Restaurante, Reserva, db
from datetime import datetime
import random

def init_routes(app):
    @app.route("/")
    def index():
        restaurantes = Restaurante.query.all()
        imagens = [
            "/static/assets/cheiro-verde.png",
            "/static/assets/donna-benta.png",
            "/static/assets/feijao-verde.png",
            "/static/assets/panela-de-barro.png",
            "/static/assets/restaurante1.png",
            "/static/assets/restaurante2.png",
            "/static/assets/restaurante3.png",
            "/static/assets/restaurante4.png",
            "/static/assets/restaurante5.png",
            "/static/assets/restaurante6.png",
            "/static/assets/restaurante7.png"
        ]
        random.shuffle(imagens)

        restaurantes_com_imagens = []
        for restaurante in restaurantes:
            imagem_aleatoria = random.choice(imagens)
            restaurantes_com_imagens.append((restaurante, imagem_aleatoria))
        
        random.shuffle(restaurantes_com_imagens)

        return render_template("index.html", restaurantes=restaurantes_com_imagens)

    @app.route('/cadastrar_cliente', methods=['GET', 'POST'])
    def cadastrar_cliente():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            telefone = request.form['telefone']
            senha = request.form['senha']

            novo_cliente = Cliente(
                nome=nome,
                email=email,
                telefone=telefone,
                senha=senha
            )
            try:
                db.session.add(novo_cliente)
                db.session.commit()
                flash('Cadastro realizado com sucesso!', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao cadastrar: {str(e)}', 'danger')

        return render_template('cadastrar_cliente.html')

    @app.route("/cadastroEmpresa", methods=['GET', 'POST'])
    def cadastroEmpresa():
        if request.method == 'POST':
            nome = request.form['nome']
            endereco = request.form['endereco']
            cnpj = request.form['cnpj']
            email = request.form['email']
            telefone = request.form['telefone']
            segmento = request.form['segmento']
            senha = request.form['senha']

            novo_restaurante = Restaurante(
                nome=nome,
                telefone=telefone,
                endereco=endereco,
                segmento=segmento,
                cnpj=cnpj,
                email=email,
                senha_hash=senha
            )

            try:
                db.session.add(novo_restaurante)
                db.session.commit()
                flash('Restaurante cadastrado com sucesso!', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao cadastrar: {str(e)}', 'danger')

        return render_template('cadastroEmpresa.html')

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']

            cliente = Cliente.query.filter_by(email=email).first()

            if cliente and cliente.senha == senha:
                session['cliente_id'] = cliente.id
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Email ou senha incorretos.', 'danger')

        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.pop('cliente_id', None)
        flash('Você saiu da sua conta.', 'success')
        return redirect(url_for('index'))

    @app.route("/reservaConcluida/<int:reserva_id>")
    def reservaConcluida(reserva_id):
        reserva = Reserva.query.get_or_404(reserva_id)
        return render_template('reserva_concluida.html', reserva=reserva)

    @app.route("/reservar/<int:restaurante_id>", methods=['GET', 'POST'])
    def reservar(restaurante_id):
        if 'cliente_id' not in session:
            flash('Você precisa estar logado para fazer uma reserva.', 'danger')
            return redirect(url_for('login'))

        restaurante = Restaurante.query.get_or_404(restaurante_id)

        if request.method == 'POST':
            cliente_id = session['cliente_id']
            data_reserva_str = request.form['data_reserva']
            hora_reserva_str = request.form['hora_reserva']
            data_hora_reserva_str = f"{data_reserva_str} {hora_reserva_str}"
            data_reserva = datetime.strptime(data_hora_reserva_str, '%Y-%m-%d %H:%M')
            tamanho_mesa = request.form['tamanho_mesa']
            numero_pessoas = request.form['numero_pessoas']

            cliente = Cliente.query.get(cliente_id)
            if cliente is None:
                flash('Erro ao fazer reserva. Tente novamente mais tarde.', 'danger')
                return redirect(url_for('index'))

            nova_reserva = Reserva(
                cliente_id=cliente_id,
                restaurante_id=restaurante_id,
                data_reserva=data_reserva,
                tamanho_mesa=tamanho_mesa,
                numero_pessoas=numero_pessoas,
                nome_cliente=cliente.nome,
                nome_restaurante=restaurante.nome
            )
            try:
                db.session.add(nova_reserva)
                db.session.commit()
                return redirect(url_for('reservaConcluida', reserva_id=nova_reserva.id))
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao fazer reserva: {str(e)}', 'danger')
                return redirect(url_for('index'))

        return render_template("reservar.html", restaurante=restaurante)

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/cadastroEscolher')
    def cadastroEscolher():
        return render_template('cadastroEscolher.html')

    @app.route('/gerenciarClientes')
    def gerenciarClientes():
        return render_template('gerenciarClientes.html')

    @app.route('/gerenciarRestaurantes')
    def gerenciarRestaurantes():
        return render_template('gerenciarRestaurantes.html')

    @app.route('/homeRestaurante')
    def homeRestaurante():
        return render_template('homeRestaurante.html')

    @app.route('/minhasReservas')
    def minhasReservas():
        return render_template('minhasReservas.html')
