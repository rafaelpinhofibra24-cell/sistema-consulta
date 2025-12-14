# Run Claro instance (PowerShell)
$env:SECRET_KEY = "claro-secret-key-please-change"
$env:DATABASE_URI = "sqlite:///employees_claro.db"
$env:PORT = "5002"
python .\app.py
