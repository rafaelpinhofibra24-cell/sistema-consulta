# Run unified instance (PowerShell) - Single instance on port 5000 serving both Vivo and Claro
$env:SECRET_KEY = "unified-secret-key-please-change"
$env:DATABASE_URI = "sqlite:///employees.db"
$env:PORT = "5000"
python .\app.py
