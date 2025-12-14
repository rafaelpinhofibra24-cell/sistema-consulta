from app import app, db, Employee
import sys

def check_employee_dates(registration=None):
    with app.app_context():
        if registration:
            # Verificar um colaborador específico
            employee = Employee.query.filter_by(registration=str(registration)).first()
            if employee:
                print(f"\nDados do colaborador {employee.registration} - {employee.full_name}:")
                print(f"Início Duplado: {employee.double_start}")
                print(f"Término Duplado: {employee.double_end}")
                print(f"Data de Carregamento: {employee.loading_date}")
            else:
                print(f"Colaborador com matrícula {registration} não encontrado.")
        else:
            # Listar todos os colaboradores com pelo menos uma data preenchida
            employees = Employee.query.filter(
                (Employee.double_start.isnot(None)) | 
                (Employee.double_end.isnot(None)) | 
                (Employee.loading_date.isnot(None))
            ).all()
            
            if not employees:
                print("Nenhum registro com datas preenchidas encontrado.")
                return
                
            print("\nColaboradores com datas preenchidas:")
            print("-" * 80)
            for emp in employees:
                print(f"Matrícula: {emp.registration}")
                print(f"Nome: {emp.full_name}")
                print(f"Início Duplado: {emp.double_start}")
                print(f"Término Duplado: {emp.double_end}")
                print(f"Data de Carregamento: {emp.loading_date}")
                print("-" * 80)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_employee_dates(sys.argv[1])
    else:
        check_employee_dates()
