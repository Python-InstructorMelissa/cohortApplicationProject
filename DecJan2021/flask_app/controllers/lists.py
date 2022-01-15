from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.list import List

@app.route('/list/')
def lists():
    lists=List.getAll()
    print("all lists via controller: ", lists)
    return render_template('lists.html', lists=lists)

# Hidden route to create new
@app.route('/createList/')
def createList():
    pass

@app.route('/list/<int:list_id>/view/')
def viewList(list_id):
    pass

# Hidden route to update item
@app.route('/list/<int:list_id>/update/')
def updateList(list_id):
    pass

# Hidden route to delete item
@app.route('/list/<int:list_id>/delete/')
def deleteList(list_id):
    pass