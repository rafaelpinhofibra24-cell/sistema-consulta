Guia: Implantação do sistema no Supabase

Resumo rápido
- O projeto usa Flask + SQLAlchemy. Atualizei a app para usar `DATABASE_URL` e adicionei `psycopg2-binary`.
- Há um arquivo `create_tables_supabase.sql` com o schema necessário.

Passos (resumido)
1) Criar projeto Supabase
   - Entre em https://app.supabase.com e crie um novo projeto (escolha password/region).
   - Copie a `DATABASE_URL` (Settings → Database → Connection string → `Connection string`)

2) Criar tabelas
   - Abra o SQL Editor no painel do projeto Supabase e cole o conteúdo de `create_tables_supabase.sql`.
   - Ou, localmente, use `psql` apontando para `DATABASE_URL`: `psql "$DATABASE_URL" -f create_tables_supabase.sql`

3) Configurar variáveis de ambiente (local ou no host de deploy)
   - `DATABASE_URL` = URL fornecida pelo Supabase
   - `SECRET_KEY` = sua chave secreta para Flask

4) Instalar dependências e testar localmente
```powershell
pip install -r requirements.txt
$env:DATABASE_URL="postgres://usuario:senha@host:5432/dbname"
$env:SECRET_KEY="uma-chave-secreta"
python app.py
```

5) Auth/Storage (opcional)
   - Se quiser usar Supabase Auth, ative em Authentication → Settings e crie usuários.
   - Para Storage, crie buckets em Storage → Buckets.

6) Deploy
   - Opções simples: Render, Fly, Railway, ou container em VPS.
   - Configure `DATABASE_URL` e `SECRET_KEY` nas variáveis de ambiente do serviço de deploy.

Notas e dicas
- O app mantém Compatibilidade com sqlite local se `DATABASE_URL` não estiver setado.
- Se o psql não estiver disponível, use o SQL Editor do Supabase.

Arquivos criados/alterados
- `app.py` (já atualizado para `DATABASE_URL`)
- `requirements.txt` (adicionado `psycopg2-binary`)
- `create_tables_supabase.sql` (schema)
- `.env.example` (exemplo de env)
- `apply_schema.ps1` (script PowerShell para aplicar o SQL via `psql`)

Se quiser, eu posso:
- Gerar um script de seed (dados iniciais) e roles/permissões no Supabase.
- Preparar um `Dockerfile` e `render.yaml` para deploy automático.
- Orientar passo-a-passo enquanto você cria o projeto Supabase (posso esperar você colar a URL aqui).
Se quiser, eu posso:
- Gerar um script de seed (dados iniciais) e roles/permissões no Supabase.
- Preparar um `Dockerfile` e `render.yaml` para deploy automático.
- Orientar passo-a-passo enquanto você cria o projeto Supabase (posso esperar você colar a URL aqui).

**Deploy com Docker / Render (passos rápidos)**
- Push do repositório para GitHub.
- No Render: New → Web Service → conectar ao repositório GitHub.
- Escolher "Docker" como ambiente (ou usar Dockerfile detectado).
- Configurar variáveis de ambiente em Render: `DATABASE_URL` e `SECRET_KEY`.
- Deploy automático fará build da imagem e rodará o serviço.

Comandos para testar localmente com a connection string:
```powershell
$env:DATABASE_URL="postgresql://postgres:YOUR_PASSWORD@db.rfpabvedkrqitbxfsyxf.supabase.co:5432/postgres"
$env:SECRET_KEY="uma-chave-secreta"
pip install -r requirements.txt
python app.py
```

Arquivos adicionados:
- `Dockerfile` — imagem para rodar a app com `gunicorn`.
- `.dockerignore` — arquivos ignorados na imagem.
- `render.yaml` — configuração de exemplo para Render.

Quer que eu faça o push para um repositório GitHub (se você me autorizar a criar/commitar aqui eu posso preparar tudo), ou prefere que eu te guie no push e deploy passo a passo?
