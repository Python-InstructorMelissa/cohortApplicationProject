from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.item import Items 

@app.route('/item/')
def items():
    items=Items.getAll()
    print("all Items via controller: ", items)
    return render_template('items.html', items=items)

# Hidden route to create new
@app.route('/createItem/')
def createItem():
    pass

@app.route('/item/<int:items_id>/view/')
def viewItem(items_id):
    pass

# Hidden route to update item
@app.route('/item/<int:items_id>/update/')
def updateItem(items_id):
    pass

# Hidden route to delete item
@app.route('/item/<int:items_id>/delete/')
def deleteItem(items_id):
    pass