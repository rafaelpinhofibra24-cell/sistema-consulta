from app import app, db, Employee
from datetime import datetime

def check_employee(registration):
    with app.app_context():
        # Encontrar o funcionário pela matrícula
        employee = Employee.query.filter_by(registration=registration).first()
        
        if employee:
            print(f"Dados do colaborador {employee.full_name} (Matrícula: {employee.registration}):")
            print(f"- Integração: {employee.integration_start} a {employee.integration_end}")
            print(f"- Normativo: {employee.normative_start} a {employee.normative_end}")
            print(f"- Curso Técnico: {employee.technical_course_start} a {employee.technical_course_end}")
            print(f"- Duplado: {employee.double_start} a {employee.double_end}")
            print(f"- Data de Carregamento: {employee.loading_date}")
            print(f"- Data de Operação em Campo: {employee.field_operation_date}")
            print(f"- Status do Curso: {employee.course_status}")
            
            # Verificar a fase atual
            today = datetime.now().date()
            print(f"\nData de hoje: {today}")
            print(f"Fase atual: {employee.get_current_phase()}")
            
            # Verificar se a data de hoje está dentro do período de integração
            if employee.integration_start and employee.integration_end:
                if employee.integration_start <= today <= employee.integration_end:
                    print("AVISO: A data atual está dentro do período de integração, mas a fase não está sendo detectada como 'Integração'")
                else:
                    print(f"Período de integração: {employee.integration_start} a {employee.integration_end}")
        else:
            print(f"Colaborador com matrícula {registration} não encontrado.")

if __name__ == "__main__":
    check_employee("58294")
