import os
import sys
import psycopg2

DB_URL = os.getenv('DATABASE_URL')
if not DB_URL:
    print('ERROR: DATABASE_URL não está definida. Defina a variável de ambiente antes de rodar.')
    sys.exit(1)

base_dir = os.path.dirname(os.path.abspath(__file__))
files = ['create_tables_supabase.sql', 'seed_supabase.sql']

try:
    conn = psycopg2.connect(DB_URL)
    conn.autocommit = True
    cur = conn.cursor()
    for f in files:
        path = os.path.join(base_dir, f)
        if not os.path.exists(path):
            print(f'WARNING: arquivo {f} não encontrado, pulando.')
            continue
        print(f'Executando {f}...')
        with open(path, 'r', encoding='utf-8') as fh:
            sql = fh.read()
            cur.execute(sql)
    cur.close()
    conn.close()
    print('Schema e seed aplicados com sucesso.')
except Exception as e:
    print('Erro ao aplicar SQL:', e)
    sys.exit(2)
