import os
import sys
from app import app, db
from sqlalchemy import text

def add_contato_column():
    with app.app_context():
        with db.engine.connect() as conn:
            try:
                # Tenta adicionar a coluna diretamente
                conn.execute(text('ALTER TABLE employee ADD COLUMN contato VARCHAR(20)'))
                conn.commit()
                print("Coluna 'contato' adicionada com sucesso!")
            except Exception as e:
                conn.rollback()
                if 'duplicate column name' in str(e):
                    print("A coluna 'contato' já existe na tabela.")
                else:
                    print(f"Erro ao adicionar a coluna: {e}")

if __name__ == '__main__':
    add_contato_column()
