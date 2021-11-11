from app import app
from flask import Flask, render_template, redirect, session, request
from app.models.parks import Park
from app.models.employees import Employee

# -------------------- Main landing page
@app.route('/')
def index():
    return render_template('index.html', allParks=Park.getAll())

# --------------- Get Routes
# ----- Get Limited Park Info
@app.route('/park/<int:id>')
def publicPark(id):
    data = {
        'id': id
    }
    return render_template('viewPark.html', onePark=Park.getOne(data))

@app.route('/admin')
def logReg():
    return render_template('logReg.html')