-- seed_supabase.sql
-- Inserts de exemplo e admin (hash já gerado)

INSERT INTO users (username, password, name, access_type, brand)
VALUES ('RafaelPinho',
 'scrypt:32768:8:1$DGi19hPV2qFEwVvF$965bb3ccd58f105c4447c2867c77983b4a3218330c702609c03b980aee37ca012eca0ae46dd950334613a5320c03444a627157b58fd7b1c5f9690a205365973c',
 'Rafael Pinho', 'admin', 'Vivo');

INSERT INTO employees (registration, brand, full_name, role, status, course_status, team, manager, loading_date)
VALUES
('1001','Vivo','João Silva','Tecnico','Ativo','Concluído','Time A','Maria','2025-12-01'),
('1002','Vivo','Ana Souza','Operador','Ativo','Em Andamento','Time B','Carlos','2025-12-05'),
('1003','Claro','Pedro Lima','Instrutor','Ativo','Concluído','Time C','Roberto','2025-11-20');

-- Políticas RLS sugestão (cole apenas se quiser habilitar RLS)
-- ALTER TABLE employees ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE users ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY employees_select_auth ON employees FOR SELECT USING (auth.role() = 'authenticated');
-- CREATE POLICY employees_block_public_crud ON employees FOR ALL USING (false);
