#!/usr/bin/env python3
"""
Migra dados de um SQLite local (`instance/employees.db`) para um Postgres (ex.: Supabase).

Uso:
  python migrate_sqlite_to_postgres.py --sqlite instance/employees.db --database-url "postgres://..."

Se `--database-url` não for passado, o script tenta ler `DATABASE_URL` do ambiente.
"""
import os
import argparse
from sqlalchemy import create_engine, MetaData
import pandas as pd


def parse_args():
    p = argparse.ArgumentParser(description='Migrate SQLite to Postgres')
    p.add_argument('--sqlite', '-s', default=os.path.join('instance', 'employees.db'), help='Path to sqlite DB file')
    p.add_argument('--database-url', '-d', default=os.getenv('DATABASE_URL'), help='Destination Postgres DATABASE_URL')
    return p.parse_args()


def main():
    args = parse_args()
    sqlite_path = args.sqlite
    dst_url = args.database_url

    if not os.path.exists(sqlite_path):
        print(f"Arquivo sqlite não encontrado: {sqlite_path}")
        return

    if not dst_url:
        print('DATABASE_URL não informado. Ex.: export DATABASE_URL="postgres://..."')
        return

    print('Conectando ao SQLite:', sqlite_path)
    src_engine = create_engine(f"sqlite:///{os.path.abspath(sqlite_path)}")

    print('Conectando ao Postgres:', dst_url)
    dst_engine = create_engine(dst_url)

    # Reflete o schema do sqlite e cria no Postgres
    src_meta = MetaData()
    print('Refletindo schema do SQLite...')
    src_meta.reflect(bind=src_engine)

    if not src_meta.tables:
        print('Nenhuma tabela encontrada no sqlite. Abortando.')
        return

    # Normalizar tipos incompatíveis com Postgres (ex.: DATETIME em sqlite)
    from sqlalchemy import DateTime
    print('Normalizando tipos de colunas para compatibilidade com Postgres...')
    for table in src_meta.tables.values():
        for col in table.columns:
            try:
                tname = type(col.type).__name__.lower()
            except Exception:
                tname = str(col.type).lower()
            if 'datetime' in tname or 'datetime' in str(col.type).lower():
                col.type = DateTime()

    print('Criando tabelas no Postgres (se não existirem)...')
    try:
        # Reflete o schema já existente no destino para evitar criar índices/constraints duplicados
        dst_meta = MetaData()
        dst_meta.reflect(bind=dst_engine)

        for table_name, table_obj in src_meta.tables.items():
            if table_name in dst_meta.tables:
                print(f'  Tabela {table_name} já existe no destino — pulando criação.')
                continue
            try:
                print(f'  Criando tabela {table_name}...')
                table_obj.create(bind=dst_engine)
            except Exception as e:
                print(f'  Erro criando tabela {table_name}:', e)
        
    except Exception as e:
        print('Erro ao criar tabelas no Postgres:', e)
        return

    # Copiar dados tabela por tabela
    summary = {}
    for table_name in src_meta.tables:
        print(f'Processando tabela: {table_name}')
        try:
            df = pd.read_sql_table(table_name, src_engine)
        except Exception as e:
            print(f'  Erro lendo {table_name} do sqlite: {e}')
            summary[table_name] = 'read_error'
            continue

        if df.empty:
            print('  Sem linhas para migrar.')
            summary[table_name] = 0
            continue

        try:
            df.to_sql(table_name, dst_engine, if_exists='append', index=False, method='multi', chunksize=1000)
            print(f'  Migradas {len(df)} linhas.')
            summary[table_name] = len(df)
        except Exception as e:
            print(f'  Erro ao inserir em {table_name}:', e)
            summary[table_name] = 'write_error'

    print('\nResumo:')
    for t, v in summary.items():
        print(f' - {t}: {v}')


if __name__ == '__main__':
    main()
