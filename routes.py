from flask import render_template, redirect, url_for, flash, session, request
from models import Cliente, Restaurante, Reserva, db
from datetime import datetime, timedelta
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
    

    #rotas do cliente
    
    @app.route('/minhasReservas')
    def minhasReservas():
        mensagem = ''

        if 'cliente_id' in session:
            cliente_id = session['cliente_id']
            cliente = Cliente.query.get(cliente_id)
            if cliente:
                reservas = Reserva.query.filter_by(cliente_id=cliente_id).all()
                reservas_formatadas = []
                hoje = datetime.now()

                for reserva in reservas:
                    restaurante = Restaurante.query.get(reserva.restaurante_id)
                    if reserva.data_reserva < hoje:
                        status = 'excluir'
                    else:
                        status = 'cancelar'
                    reservas_formatadas.append({
                        'id': reserva.id,
                        'nome_cliente': reserva.nome_cliente,
                        'data_reserva': reserva.data_reserva,
                        'tamanho_mesa': reserva.tamanho_mesa,
                        'numero_pessoas': reserva.numero_pessoas,
                        'status': status,
                        'nome_restaurante': restaurante.nome if restaurante else 'Restaurante não encontrado'
                    })
                    
                return render_template('minhasReservas.html', cliente=cliente, reservas=reservas_formatadas)

        mensagem = 'Você precisa estar logado para olhar as reservas!'
        return redirect(url_for('login'), mensagem=mensagem)

    @app.route('/excluirReserva/<int:reserva_id>', methods=['POST'])
    def excluirReserva(reserva_id):
        if 'cliente_id' in session:
            reserva = Reserva.query.get_or_404(reserva_id)
            db.session.delete(reserva)
            db.session.commit()
            return redirect(url_for('minhasReservas'))

    @app.route('/cancelarReserva/<int:reserva_id>', methods=['POST'])
    def cancelarReserva(reserva_id):
        if 'cliente_id' in session:
            reserva = Reserva.query.get_or_404(reserva_id)
            db.session.delete(reserva)
            db.session.commit()
            flash('Reserva cancelada com sucesso.', 'success')
            return redirect(url_for('minhasReservas'))

        return redirect(url_for('login'))

    @app.route('/perfilUsuario')
    def perfil_usuario():
        mensagem = ''

        if 'cliente_id' in session:
            cliente = Cliente.query.get(session['cliente_id'])
            if cliente:
                return render_template('perfilUsuario.html', cliente=cliente)
        mensagem = 'Você precisa estar logado para acessar essa página!'
        return redirect(url_for('login'), mensagem=mensagem)
    
    @app.route('/clienteLogado')
    def cliente_logado():
        mensagem = ''

        if 'cliente_id' in session:
            cliente = Cliente.query.get(session['cliente_id'])
            if cliente:
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

                return render_template("clienteLogado.html", cliente=cliente, restaurantes=restaurantes_com_imagens)

        mensagem = 'Você precisa estar logado para acessar esta página.'
        return redirect(url_for('login'), mensagem=mensagem)

    @app.route('/cadastrar_cliente', methods=['GET', 'POST'])
    def cadastrar_cliente():
        mensagem = ''
        mensagem2 = ''
        
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
                mensagem = 'Cadastro realizado com sucesso!'
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                mensagem2 = f'Erro ao cadastrar: {str(e)}'

        return render_template('cadastrar_cliente.html', mensagem=mensagem, mensagem2=mensagem2)
    
    # Login route
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            return login(email, senha)

        return render_template("login.html")
    

    # Common login function
    def login(email, senha):
        cliente = Cliente.query.filter_by(email=email).first()
        restaurante = Restaurante.query.filter_by(email=email).first()

        if cliente and cliente.senha == senha:
            session['cliente_id'] = cliente.id
            return redirect(url_for('cliente_logado'))

        elif restaurante and restaurante.senha_hash == senha:
            session['restaurante_id'] = restaurante.id
            return redirect(url_for('perfilRestaurante'))

        else:
            flash('Email ou senha incorreto, tente novamente!', 'danger')
            return redirect(url_for('login'))

    # Logout route
    @app.route("/logout")
    def logout():
        session.pop('cliente_id', None)
        session.pop('restaurante_id', None)
        flash('Você saiu da sessão', 'info')
        return redirect(url_for('index'))
    
    @app.route("/reservaConcluida/<int:reserva_id>")
    def reservaConcluida(reserva_id):
        reserva = Reserva.query.get_or_404(reserva_id)
        return render_template('reserva_concluida.html', reserva=reserva)

    @app.route("/reservar/<int:restaurante_id>", methods=['GET', 'POST'])
    def reservar(restaurante_id):
        mensagem = ''
        mensagem2 = ''
        mensagem3 = ''

        if 'cliente_id' not in session:
            mensagem = 'Você precisa estar logado para fazer uma reserva!'
            return redirect(url_for('login'))

        restaurante = Restaurante.query.get_or_404(restaurante_id)

        if request.method == 'POST':
            cliente_id = session['cliente_id']
            data_reserva_str = request.form['data_reserva']
            hora_reserva_str = request.form['hora_reserva']
            data_hora_reserva_str = f"{data_reserva_str} {hora_reserva_str}"
            data_reserva = datetime.strptime(data_hora_reserva_str, '%Y-%m-%d %H:%M')
            
            # Validação de data
            hoje = datetime.now()
            if data_reserva <= hoje:
                mensagem2 = 'Você só pode fazer reservas para datas futuras a partir de amanhã.'
                return render_template("reservar.html", restaurante=restaurante, mensagem2=mensagem2)

            tamanho_mesa = request.form['tamanho_mesa']
            numero_pessoas = request.form['numero_pessoas']

            cliente = Cliente.query.get(cliente_id)
            if cliente is None:
                mensagem2 = 'Erro ao fazer a reserva, tente novamente mais tarde.'
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
                mensagem3 = (f'Erro ao fazer reserva: {str(e)}')
                return redirect(url_for('index'))

        return render_template("reservar.html", restaurante=restaurante, mensagem=mensagem, mensagem2=mensagem2, mensagem3=mensagem3)

    #rotas da empresa

    @app.route('/excluirReserva/<int:reserva_id>', methods=['POST'])
    def excluir_reserva_cliente(reserva_id):
        if 'cliente_id' in session:
            reserva = Reserva.query.get_or_404(reserva_id)
            db.session.delete(reserva)
            db.session.commit()
            return redirect(url_for('minhasReservas'))

        return redirect(url_for('login'))


    @app.route("/cadastroEmpresa", methods=['GET', 'POST'])
    def cadastroEmpresa():
        mensagem = ''
        mensagem2 = ''

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
                mensagem = ('Restaurante cadastrado com sucesso!')
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                mensagem2 = (f'Erro ao cadastrar: {str(e)}')

        return render_template('cadastroEmpresa.html', mensagem=mensagem , mensagem2=mensagem2)


    #rotas sem dependencias

    @app.route('/dashboard')
    def dashboard():
        reservas = Reserva.query.all()
        return render_template('dashboard.html', reservas=reservas)


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
        mensagem = ''
        reservas = []

        if 'restaurante_id' in session:
            restaurante_id = session['restaurante_id']
            restaurante = Restaurante.query.get(restaurante_id)

            if restaurante:
                # Filtrando reservas apenas para o restaurante logado
                reservas = Reserva.query.filter_by(restaurante_id=restaurante_id).all()

                # Excluir reservas passadas do banco de dados
                reservas_passadas = [reserva for reserva in reservas if reserva.data_reserva < datetime.now()]
                for reserva in reservas_passadas:
                    db.session.delete(reserva)
                    db.session.commit()

                # Filtrar novamente para obter apenas as reservas futuras
                reservas = [reserva for reserva in reservas if reserva.data_reserva >= datetime.now()]
            else:
                mensagem = 'Restaurante não encontrado'
        
        return render_template('homeRestaurante.html', restaurante=restaurante, reservas=reservas, mensagem=mensagem)
    
    @app.route('/perfilRestaurante')
    def perfilRestaurante():
        mensagem = ''
        restaurante = None

        if 'restaurante_id' in session:
            restaurante_id = session['restaurante_id']
            restaurante = Restaurante.query.get(restaurante_id)

        if restaurante:
            return render_template('perfilRestaurante.html', restaurante=restaurante)
        else:
            mensagem = 'Restaurante não encontrado'
        
        return render_template('perfilRestaurante.html', mensagem=mensagem)
    
    @app.route('/cadastroConcluido')
    def cadastroConcluido():
        return render_template('cadastroConcluido.html')
    

    

