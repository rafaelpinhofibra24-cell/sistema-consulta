# Sistema (Vivo / Claro)

Este workspace contém a aplicação principal e scripts para executar duas instâncias independentes (Vivo e Claro), além de uma landing page para escolher a instância.

Visão geral
- `app.py` - aplicação Flask principal (configurável por variáveis de ambiente).
- `launcher.py` - landing page que roda na porta 5000 e mostra dois botões: Vivo (roxo) e Claro (vermelho).
- `.env.vivo` / `.env.claro` - exemplos de variáveis de ambiente para cada instância.
- `run_vivo.ps1` / `run_claro.ps1` / `run_launcher.ps1` - scripts PowerShell para iniciar cada serviço localmente.

Como executar (Windows PowerShell)
1. Crie e ative um ambiente virtual (opcional, recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instale dependências (apenas se necessário):

```powershell
pip install -r requirements.txt
```

3. Em três terminais PowerShell separados, execute:

- Iniciar landing (porta 5000):
```powershell
.\run_launcher.ps1
```

- Iniciar Vivo (porta 5001):
```powershell
.\run_vivo.ps1
```

- Iniciar Claro (porta 5002):
```powershell
.\run_claro.ps1
```

4. Abra o navegador em `http://localhost:5000/` e escolha a instância (Vivo ou Claro).

Admin padrão
- Usuário: `RafaelPinho`
- Senha: `@21314100`

Observações importantes
- Cada instância usa um arquivo de banco SQLite diferente (`employees_vivo.db` e `employees_claro.db`) para garantir independência total dos dados.
- Se preferir, você pode ajustar as variáveis em `.env.vivo` e `.env.claro` e usar esses valores no PowerShell antes de iniciar as instâncias.
- Por segurança, atualize `SECRET_KEY` nos arquivos `.env.*` antes de expor a aplicação.

Se quiser, eu posso:
- Rodar aqui um teste (iniciar as 3 aplicações) e confirmar que as páginas abrem.
- Gerar `*.bat` em vez de `*.ps1` se preferir usar cmd.exe.
- Alterar a aparência (logos/cores) dos templates além do botão da landing.
