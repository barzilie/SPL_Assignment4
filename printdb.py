from persistence import *
from dbtools import *

def get_activities():
    c = repo._conn.cursor()
    c.execute('SELECT * FROM activities ORDER BY date')
    return orm(c, Activitie)
        
def get_employees():
    c = repo._conn.cursor()
    c.execute('SELECT * FROM employees ORDER BY id') 
    return orm(c, Employee)

def get_employees_by_name():
    c = repo._conn.cursor()
    c.execute('SELECT * FROM employees ORDER BY name') 
    return orm(c, Employee)

def get_suppliers():
    c = repo._conn.cursor()
    c.execute('SELECT * FROM suppliers ORDER BY id') 
    return orm(c, Supplier)

def get_products():
    c = repo._conn.cursor()
    c.execute('SELECT * FROM products ORDER BY id')
    return orm(c, Product) 

def get_branches():
    c = repo._conn.cursor()
    c.execute('SELECT * FROM branches ORDER BY id') 
    return orm(c, Branche)

def get_branch_location(branch_id):
    c = repo._conn.cursor()
    c.execute(f'SELECT location FROM branches WHERE id = {branch_id}')
    return c.fetchone()[0]

def get_sales(employee_id):
    c = repo._conn.cursor()
    c.execute(f"""SELECT activities.product_id, activities.quantity, products.price
              FROM activities INNER JOIN products ON activities.product_id = products.id  
              WHERE activator_id = {employee_id} AND activities.quantity < 0""")
    sales = 0
    records = c.fetchall()
    for record in records:
        sales = sales + int(record[1])*float(record[2])*(-1)
    return sales

def get_activity_report():
    c = repo._conn.cursor()
    c.execute(f"""SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name
              FROM (((activities INNER JOIN products ON activities.product_id = products.id)
              LEFT OUTER JOIN employees ON activities.activator_id = employees.id)
              LEFT OUTER JOIN suppliers ON activities.activator_id = suppliers.id)
              ORDER BY date""")
    return c.fetchall()

def main():
    print("Activities")
    activities = get_activities()
    for activity in activities:
        print(activity)
        
    print("Branches")
    branches = get_branches()
    for branch in branches:
        print(branch) 
        
    print("Employees")
    employees = get_employees()
    for employee in employees:
        print(employee)  
        
    print("Products")
    products = get_products()
    for product in products:
        print(product) 
        
    print("Suppliers")
    suppliers = get_suppliers()
    for supplier in suppliers:
        print(supplier)
        
    print("Employees report")
    employees_by_name = get_employees_by_name()
    for employee in employees_by_name:
        location = get_branch_location(employee.branche)
        sales = get_sales(employee.id)
        print(f"{employee.name} {employee.salary} {location} {sales}")
    
    print("Activities report")
    activity_reports = get_activity_report()
    for activity in activity_reports:
        print(activity)
        #f"{activity.date}, {product.description}, {aactivity.quantity}, {employees.name}, {suppliers.name}"

        

if __name__ == '__main__':
    main()