# Script PowerShell para aplicar create_tables_supabase.sql usando psql
# Requisitos: psql (Postgres client) disponível no PATH e variável $env:DATABASE_URL definida

if (-not $env:DATABASE_URL) {
    Write-Host "Variável DATABASE_URL não encontrada. Defina-a antes de rodar:`$env:DATABASE_URL = 'postgres://user:pass@host:5432/db'" -ForegroundColor Red
    exit 1
}

# Executa o arquivo SQL
psql $env:DATABASE_URL -f "$(Join-Path $PSScriptRoot 'create_tables_supabase.sql')"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Erro ao aplicar o schema (psql retornou código de erro $LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "Schema aplicado com sucesso." -ForegroundColor Green
