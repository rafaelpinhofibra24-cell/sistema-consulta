""
Migration script to add the audit_log table
"""
from app import db

def upgrade():
    # Create the audit_log table
    db.create_all()
    print("Audit log table created successfully")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        upgrade()
