# Run Vivo instance (PowerShell)
$env:SECRET_KEY = "vivo-secret-key-please-change"
$env:DATABASE_URI = "sqlite:///employees_vivo.db"
$env:PORT = "5001"
python .\app.py
