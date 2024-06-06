from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key'  # Adicione uma chave secreta para flash messages
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    telefone = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)  # Adicionando o campo senha

class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    restaurante_id = db.Column(db.Integer, db.ForeignKey('restaurante.id'), nullable=False)
    data_reserva = db.Column(db.DateTime, nullable=False)
    tamanho_mesa = db.Column(db.Integer, nullable=False)
    numero_pessoas = db.Column(db.Integer, nullable=False)
    nome_cliente = db.Column(db.String(255), nullable=False)  # Novo campo para o nome do cliente
    nome_restaurante = db.Column(db.String(255), nullable=False)  # Novo campo para o nome do restaurante

    cliente = db.relationship('Cliente', backref=db.backref('reservas', lazy=True))
    restaurante = db.relationship('Restaurante', backref=db.backref('reservas', lazy=True))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cliente = Cliente.query.filter_by(email=email).first()

        if cliente and check_password_hash(cliente.senha, senha):
            session['cliente_id'] = cliente.id  # Armazena o ID do cliente na sessão
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Email ou senha incorretos.', 'danger')
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('cliente_id', None)  # Remove o cliente da sessão
    flash('Você saiu da sua conta.', 'success')
    return redirect(url_for('index'))

@app.route("/reservaConcluida/<int:reserva_id>")
def reservaConcluida(reserva_id):
    reserva = Reserva.query.get_or_404(reserva_id)
    return render_template("reservaConcluida.html", reserva=reserva)


@app.route("/reservar", methods=['GET', 'POST'])
def reservar():
    if 'cliente_id' not in session:
        flash('Você precisa estar logado para fazer uma reserva.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        cliente_id = session['cliente_id']
        restaurante_id = 1  # Vamos supor que o restaurante está fixo, no exemplo
        data_reserva_str = request.form['data_reserva']
        hora_reserva_str = request.form['hora_reserva']
        data_hora_reserva_str = f"{data_reserva_str} {hora_reserva_str}"
        data_reserva = datetime.strptime(data_hora_reserva_str, '%Y-%m-%d %H:%M')
        tamanho_mesa = request.form['tamanho_mesa']
        numero_pessoas = request.form['numero_pessoas']

        cliente = Cliente.query.get(cliente_id)
        restaurante = Restaurante.query.get(restaurante_id)

        nova_reserva = Reserva(
            cliente_id=cliente_id,
            restaurante_id=restaurante_id,
            data_reserva=data_reserva,
            tamanho_mesa=tamanho_mesa,
            numero_pessoas=numero_pessoas,
            nome_cliente=cliente.nome,
            nome_restaurante=restaurante.nome
        )
        db.session.add(nova_reserva)
        db.session.commit()

        return redirect(url_for('reservaConcluida', reserva_id=nova_reserva.id))

    return render_template("reservar.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        
        hashed_senha = generate_password_hash(senha, method='pbkdf2:sha256')
        
        novo_cliente = Cliente(
            nome=nome,
            email=email,
            telefone=telefone,
            senha=hashed_senha
        )
        
        try:
            db.session.add(novo_cliente)
            db.session.commit()
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro ao cadastrar: {str(e)}', 'danger')
    
    return render_template('cadastro.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
