from app import app, db
from sqlalchemy import text
from datetime import datetime

with app.app_context():
    try:
        # 1. Primeiro, adiciona a coluna sem valor padrão
        print("Adicionando coluna 'last_updated'...")
        db.session.execute(text('ALTER TABLE employee ADD COLUMN last_updated DATETIME'))
        
        # 2. Atualiza todos os registros existentes com a data/hora atual
        print("Atualizando registros existentes...")
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        db.session.execute(
            text('UPDATE employee SET last_updated = :current_time'),
            {'current_time': current_time}
        )
        
        # 3. Modifica a coluna para ter um valor padrão (isso não é estritamente necessário, 
        #    mas garante que novos registros tenham um valor padrão)
        print("Configurando valor padrão...")
        # SQLite não suporta adicionar um valor padrão a uma coluna existente,
        # então vamos criar uma nova tabela e copiar os dados
        
        # Cria uma nova tabela com a estrutura correta
        db.session.execute(text('''
            CREATE TABLE employee_new (
                id INTEGER NOT NULL,
                registration VARCHAR(50) NOT NULL,
                full_name VARCHAR(200) NOT NULL,
                role VARCHAR(100),
                employee_type VARCHAR(50),
                admission_date DATE,
                cep VARCHAR(20),
                status VARCHAR(50),
                course_status VARCHAR(50),
                team VARCHAR(100),
                course_location VARCHAR(200),
                manager VARCHAR(100),
                corporate_manager VARCHAR(100),
                instructor VARCHAR(100),
                contato VARCHAR(20),
                operation_ready VARCHAR(10),
                integration_start DATE,
                integration_end DATE,
                normative_start DATE,
                normative_end DATE,
                technical_course_start DATE,
                technical_course_end DATE,
                double_start DATE,
                double_end DATE,
                loading_date DATE,
                field_operation_date DATE,
                last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (id),
                UNIQUE (registration)
            )
        '''))
        
        # Copia os dados da tabela antiga para a nova
        print("Copiando dados para a nova tabela...")
        db.session.execute(text('''
            INSERT INTO employee_new (
                id, registration, full_name, role, employee_type, admission_date, cep, 
                status, course_status, team, course_location, manager, corporate_manager,
                instructor, contato, operation_ready, integration_start, integration_end,
                normative_start, normative_end, technical_course_start, technical_course_end,
                double_start, double_end, loading_date, field_operation_date, last_updated
            )
            SELECT 
                id, registration, full_name, role, employee_type, admission_date, cep, 
                status, course_status, team, course_location, manager, corporate_manager,
                instructor, contato, operation_ready, integration_start, integration_end,
                normative_start, normative_end, technical_course_start, technical_course_end,
                double_start, double_end, loading_date, field_operation_date, 
                COALESCE(last_updated, DATETIME('now'))
            FROM employee
        '''))
        
        # Remove a tabela antiga e renomeia a nova
        print("Atualizando a estrutura do banco de dados...")
        db.session.execute(text('DROP TABLE employee'))
        db.session.execute(text('ALTER TABLE employee_new RENAME TO employee'))
        
        # Confirma as alterações
        db.session.commit()
        
        print("Migração concluída com sucesso!")
        
    except Exception as e:
        print(f"Erro durante a migração: {e}")
        db.session.rollback()
        raise
