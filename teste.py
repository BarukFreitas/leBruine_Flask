from app import app, db, Cliente, Restaurante

with app.app_context():
    # Verificar se o cliente já existe
    cliente_existente = Cliente.query.filter_by(email='cliente@example.com').first()
    if not cliente_existente:
        cliente = Cliente(nome='Exemplo Cliente', email='cliente@example.com', telefone='123456789')
        db.session.add(cliente)
        db.session.commit()
    else:
        print("Cliente já existe no banco de dados.")

    # Verificar se o restaurante já existe
    restaurante_existente = Restaurante.query.filter_by(nome='Exemplo Restaurante').first()
    if not restaurante_existente:
        restaurante = Restaurante(nome='Exemplo Restaurante', telefone='987654321', endereco='Rua Exemplo, 123')
        db.session.add(restaurante)
        db.session.commit()
    else:
        print("Restaurante já existe no banco de dados.")
