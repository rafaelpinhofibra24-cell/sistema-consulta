-- Schema export for Supabase (Postgres)
-- Tables: users, employees, audit_log

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    password VARCHAR(200) NOT NULL,
    name VARCHAR(100) NOT NULL,
    access_type VARCHAR(20) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    CONSTRAINT uq_username_brand UNIQUE (username, brand)
);

CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    registration VARCHAR(50) NOT NULL,
    brand VARCHAR(20) NOT NULL DEFAULT 'Vivo',
    full_name VARCHAR(200) NOT NULL,
    role VARCHAR(100),
    employee_type VARCHAR(50),
    admission_date DATE,
    cep VARCHAR(20),
    status VARCHAR(50),
    course_status VARCHAR(50),
    team VARCHAR(100),
    course_location VARCHAR(200),
    manager VARCHAR(100),
    corporate_manager VARCHAR(100),
    instructor VARCHAR(100),
    contato VARCHAR(20),
    operation_ready VARCHAR(10),
    integration_start DATE,
    integration_end DATE,
    normative_start DATE,
    normative_end DATE,
    technical_course_start DATE,
    technical_course_end DATE,
    double_start DATE,
    double_end DATE,
    loading_date DATE,
    field_operation_date DATE,
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    CONSTRAINT uq_registration_brand UNIQUE (registration, brand)
);

CREATE TABLE IF NOT EXISTS audit_log (
    id SERIAL PRIMARY KEY,
    registration VARCHAR(50) NOT NULL,
    field_changed VARCHAR(50) NOT NULL,
    old_value VARCHAR(500),
    new_value VARCHAR(500),
    changed_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    changed_by VARCHAR(80) NOT NULL,
    change_source VARCHAR(20) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_audit_registration ON audit_log (registration);

-- End of schema
