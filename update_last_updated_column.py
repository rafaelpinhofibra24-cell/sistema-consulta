from app import app, db
from sqlalchemy import text

def update_last_updated_column():
    with app.app_context():
        try:
            # Verifica se a coluna já existe
            inspector = db.inspect(db.engine)
            columns = [column['name'] for column in inspector.get_columns('employee')]
            
            if 'last_updated' not in columns:
                print("Adicionando coluna 'last_updated'...")
                # Adiciona a coluna sem valor padrão
                db.session.execute(text('ALTER TABLE employee ADD COLUMN last_updated DATETIME'))
                
                # Atualiza os registros existentes com a data/hora atual
                print("Atualizando registros existentes...")
                from datetime import datetime, timezone
                current_time = datetime.now(timezone.utc) - timedelta(hours=3)  # Ajuste para o fuso horário de Brasília
                db.session.execute(
                    text('UPDATE employee SET last_updated = :current_time'),
                    {'current_time': current_time}
                )
                
                db.session.commit()
                print("Coluna 'last_updated' adicionada e preenchida com sucesso!")
            else:
                print("A coluna 'last_updated' já existe na tabela 'employee'.")
                
                # Atualiza a data de todos os registros para o fuso horário correto
                print("Atualizando datas existentes para o fuso horário de Brasília...")
                from datetime import datetime, timezone, timedelta
                current_time = datetime.now(timezone.utc) - timedelta(hours=3)
                db.session.execute(
                    text('UPDATE employee SET last_updated = :current_time'),
                    {'current_time': current_time}
                )
                db.session.commit()
                print("Datas atualizadas com sucesso!")
                
        except Exception as e:
            print(f"Erro ao atualizar o banco de dados: {e}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    update_last_updated_column()
