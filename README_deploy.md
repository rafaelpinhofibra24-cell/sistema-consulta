# Deploy no Fly.io (com banco Supabase gratuito)

# Visão geral
Este repositório já possui um `Dockerfile` e é compatível com deploy no Fly.io. Recomendo usar o Fly.io para hospedar a aplicação e o Supabase (plano gratuito) para o banco Postgres. O Fly serve o app e o Supabase fornece `DATABASE_URL` seguro.

# Passos resumidos
1. Criar conta no Supabase e criar um projeto (grátis). Copie a `DATABASE_URL` do projeto (Postgres).
2. Criar conta no Fly.io e instalar `flyctl` localmente.
3. No terminal (na pasta do projeto), faça login: `flyctl auth login`.
4. Criar a app Fly: `flyctl apps create NOME_DA_SUA_APP`.
5. Definir secrets no Fly com a `DATABASE_URL` e `SECRET_KEY`:

```bash
flyctl secrets set DATABASE_URL="sua_database_url_aqui" SECRET_KEY="uma_chave_secreta_aqui"
```

6. Fazer deploy:

```bash
flyctl deploy --remote-only
```

7. Após deploy, verifique logs:

```bash
flyctl logs -a NOME_DA_SUA_APP
```

# Notas importantes
- O `Dockerfile` já expõe a porta `8000` e usa `gunicorn` com `app:app`.
- Não é recomendado usar SQLite em produção no Fly (containers são efêmeros). Use o Supabase/Postgres.
- Para migrar dados do SQLite local para o Supabase, exporte um dump ou use scripts Python para copiar registros.
- Se preferir, eu posso gerar um script para migrar o SQLite local para o Postgres do Supabase.

# Se quiser que eu faça mais
- Posso gerar um pequeno script `migrate_sqlite_to_postgres.py` e instruções para rodá-lo.
- Posso também preparar configurações adicionais (variáveis de ambiente, ajustes no `app.py`) se desejar.

## Script de migração SQLite -> Postgres

Criei `scripts/migrate_sqlite_to_postgres.py` para copiar o schema e os dados do `instance/employees.db` local para um Postgres (ex.: Supabase).

Exemplo de uso local (no diretório do repositório):

```bash
python scripts/migrate_sqlite_to_postgres.py --sqlite instance/employees.db --database-url "postgres://user:pass@host:5432/dbname"
```

Ou exportando a variável e rodando sem o argumento `--database-url`:

```bash
export DATABASE_URL="postgres://user:pass@host:5432/dbname"
python scripts/migrate_sqlite_to_postgres.py --sqlite instance/employees.db
```

O script tenta refletir o schema do SQLite, criar as mesmas tabelas no Postgres e copiar os dados tabela a tabela.
