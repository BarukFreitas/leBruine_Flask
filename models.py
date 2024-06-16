from db import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    telefone = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    segmento = db.Column(db.String(255), nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    restaurante_id = db.Column(db.Integer, db.ForeignKey('restaurante.id'), nullable=False)
    data_reserva = db.Column(db.DateTime, nullable=False)
    tamanho_mesa = db.Column(db.Integer, nullable=False)
    numero_pessoas = db.Column(db.Integer, nullable=False)
    nome_cliente = db.Column(db.String(255), nullable=False)
    nome_restaurante = db.Column(db.String(255), nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('reservas', lazy=True))
    restaurante = db.relationship('Restaurante', backref=db.backref('reservas', lazy=True))
