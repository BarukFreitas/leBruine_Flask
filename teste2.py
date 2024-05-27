from app import app, db, Cliente, Restaurante, Reserva
from datetime import datetime

# Criar o contexto da aplicação Flask
app.app_context().push()

# Supondo que você já tenha os objetos Cliente e Restaurante que representam os registros do banco de dados
cliente = Cliente.query.first()  # Supondo que você selecionou o primeiro cliente da tabela
restaurante = Restaurante.query.first()  # Supondo que você selecionou o primeiro restaurante da tabela

# Criar um objeto de Reserva
nova_reserva = Reserva(
    cliente_id=cliente.id,
    restaurante_id=restaurante.id,
    data_reserva=datetime(2024, 5, 30, 12, 30),  # Substitua com a data e hora desejadas
    tamanho_mesa="4 pessoas",  # Substitua com o tamanho da mesa desejado
    numero_pessoas=4  # Substitua com o número de pessoas
)

# Adicionar a nova reserva ao banco de dados
db.session.add(nova_reserva)
db.session.commit()

print("Reserva criada com sucesso!")
