from app import app
from flask import Flask, render_template, redirect, session, request
from app.models.parks import Park

# ----------- Main landing page
@app.route('/')
def index():
    return render_template('index.html', allParks=Park.getAll())



# -------- create park landing
@app.route('/park/addPark')
def addPark():
    return render_template('addpark.html')

# ------- view park landing page
@app.route('/park/viewPark/<int:id>')
def viewPark(id):
    data = {
        'id': id
    }
    return render_template('viewPark.html', onePark=Park.getOne(data))



# --------- hidden create park route
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

# ------ hidden edit park route
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

# ------- hidden remove park route
@app.route('/park/deletePark/<int:id>')
def deletePark(id):
    data = {
        'id': id
    }
    Park.delete(data)
    return redirect('/')
