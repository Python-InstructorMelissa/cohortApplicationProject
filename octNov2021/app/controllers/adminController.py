from app import app
from flask import Flask, render_template, redirect, session, request
from app.models.parks import Park
from app.models.employees import Employee

# -------------------- Main landing page
@app.route('/dashboard')
def dashboard():
    pass

# --------------- Get Routes

# ----- All Parks
@app.route('/admin/parks')
def adminParks():
    pass

# ----- All Employees
@app.route('/admin/employees')
def adminEmployees():
    pass

# ----- All Add Ons Like rides, regions, animals attractions
@app.route('/admin/allAddOns')
def adminAddOns():
    pass


# ---------- Forms

# ----- Add new Park
@app.route('/admin/addPark')
def addPark():
    pass

# ----- Add new Employee
@app.route('/admin/addEmployee')
def addEmployee():
    pass

# ----- Add new Add ons
@app.route('/admin/addToPark')
def addToPark():
    pass


# --------------- Create Routes
# ----- New Park
# ----- New Park Address
# ----- New Employee
# ----- New Employee Address
# ----- New Ride
# ----- New Attraction
# ----- New Region
# ----- New Animal

# --------------- Update Routes
# ----- Update Park
# ----- Update Park Address
# ----- Update Employee
# ----- Update Employee Address
# ----- Update Ride
# ----- Update Attraction
# ----- Update Region
# ----- Update Animal

# --------------- Delete Routes
# ----- Delete Park
# ----- Delete Park Address
# ----- Delete Employee
# ----- Delete Employee Address
# ----- Delete Ride
# ----- Delete Attraction
# ----- Delete Region
# ----- Delete Animal