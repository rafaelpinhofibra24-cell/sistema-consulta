from app import app, db
from datetime import datetime

with app.app_context():
    # Verifica se a coluna já existe
    inspector = db.inspect(db.engine)
    columns = [column['name'] for column in inspector.get_columns('employee')]
    
    if 'last_updated' not in columns:
        print("Adicionando coluna 'last_updated' à tabela 'employee'...")
        try:
            # Adiciona a nova coluna com um valor padrão
            db.engine.execute('''
                ALTER TABLE employee 
                ADD COLUMN last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            ''')
            print("Coluna 'last_updated' adicionada com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar a coluna: {str(e)}")
    else:
        print("A coluna 'last_updated' já existe na tabela 'employee'.")
