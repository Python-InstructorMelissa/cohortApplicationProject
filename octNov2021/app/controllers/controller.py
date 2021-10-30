from app import app
from flask import Flask, render_template, redirect, session, request
from app.models.parks import Park
from app.models.employees import Employee

# -------------------- Main landing page
@app.route('/')
def index():
    return render_template('index.html', allParks=Park.getAll())

# --------------- Get Routes

# ----- view Park
@app.route('/park/viewPark/<int:id>')
def viewPark(id):
    data = {
        'id': id
    }
    return render_template('viewPark.html', onePark=Park.getOne(data), park=Park.getWorkers(data))

# ----- view Employee
@app.route('/employees/viewEmployee/<int:id>')
def viewEmployee(id):
    data = {
        'id': id
    }
    theJob=Employee.getJob(data)
    return render_template('viewEmployee.html', worker=Employee.getOne(data), job=Employee.getJob(data), allParks=Park.getAll())

# ---------- Forms

# ----- Park form
@app.route('/park/addPark')
def addPark():
    return render_template('addpark.html')

# ----- Employee Form
@app.route('/employees')
def addEmployee():
    return render_template('employees.html', allParks=Park.getAll(), allWorkers=Employee.getAll())

# --------------- Create Routes

# ----- Create Park
@app.route('/park/createPark', methods=['POST'])
def createpark():
    data = {
        "parkName": request.form['parkName'],
        "parkDesc": request.form['parkDesc'],
        "parkLocation": request.form['parkLocation'],
        "parkType": request.form['parkType']
    }
    Park.save(data)
    return redirect('/')

# ----- Create Employee
@app.route('/employees/createEmployee', methods=['POST'])
def createEmployee():
    data = {
        'eFirstName': request.form['eFirstName'],
        'eLastName': request.form['eLastName'],
        'eEmail': request.form['eEmail'],
        'parks_id': request.form['parks_id']
    }
    Employee.save(data)
    return redirect('/employees')

# --------------- Update Routes

# ----- Update Park
@app.route('/park/updatePark/<int:id>', methods=['POST'])
def updatePark(id):
    data = {
        'id': id,
        "parkName": request.form['parkName'],
        "parkDesc": request.form['parkDesc'],
        "parkLocation": request.form['parkLocation'],
        "parkType": request.form['parkType']
    }
    parkId = id
    Park.update(data)
    return redirect(f"/park/viewPark/{parkId}")

# ----- Update Employee
@app.route('/employee/updateEmployee/<int:id>', methods=['POST'])
def updateEmployee(id):
    data = {
        'id': id,
        'eFirstName': request.form['eFirstName'],
        'eLastName': request.form['eLastName'],
        'eEmail': request.form['eEmail'],
        'parks_id': request.form['parks_id']
    }
    eId = id
    Employee.update(data)
    return redirect(f"/employees/viewEmployee/{eId}")



# --------------- Delete Routes

# ----- Delete Park
@app.route('/park/deletePark/<int:id>')
def deletePark(id):
    data = {
        'id': id
    }
    Park.delete(data)
    return redirect('/')