from app import app, db
from sqlalchemy import text

with app.app_context():
    try:
        # Adiciona a coluna last_updated à tabela employee
        db.session.execute(text('ALTER TABLE employee ADD COLUMN last_updated DATETIME DEFAULT CURRENT_TIMESTAMP'))
        db.session.commit()
        print("Coluna 'last_updated' adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar a coluna: {e}")
        db.session.rollback()
