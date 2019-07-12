from flask import Flask, render_template, request
from sqlite3 import connect
#just writing it for the sake of writing
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/add_employee_form')
def add_employee_form():
    return render_template('add_employee.html')

@app.route('/add_employee')
def add_employee():
    id = request.args.get('id')
    name = request.args.get('name')
    designation = request.args.get('designation')
    add_employee_to_db(id, name, designation)

    all_employees = get_all_employees_from_db()

    return render_template('view_all_employees.html', all_employees=all_employees)

@app.route('/updateForm')
def updateForm():
    pass

@app.route('/updateEmployee')
def updateEmployee():
    pass

@app.route('/get_all_employees')
def get_all_employees():
    all_employees = get_all_employees_from_db()
    return render_template('view_all_employees.html', all_employees=all_employees )

@app.route('/delete')
def delete_employee():
    pass

def add_employee_to_db(employee_id, name, designation):
    con = connect('employee_details.sql')
    sql_query = """insert into employee values ("%s", "%s", "%s") """ %(employee_id, name, designation)
    cursor = con.cursor()
    cursor.execute(sql_query)
    con.commit()

def get_all_employees_from_db():
    con = connect('employee_details.sql')
    sql_query = """select * from employee"""
    cursor = con.cursor()
    cursor.execute(sql_query)
    all_employees = cursor.fetchall()
    return all_employees

def delete_employee_from_db(id):
    pass

def get_employee_from_db(id):
    pass

def update_employee_in_db(id, name, designation):
    pass

app.run(debug=True, port=5008)
