from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.item import Items 
from flask_app.models.user import User
from flask_app.models.category import Category

@app.route('/item/')
def items():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        items=Items.getAll()
        cats=Category.getAll()
        users=User.getAll()
        print("all Items via controller: ", items)
        return render_template('items.html', items=items, user=user, cats=cats, users=users)

# Hidden route to create new
@app.route('/createItem/', methods=['POST'])
def createItem():
    data = {
        'itemName': request.form['itemName'],
        'itemInfo': request.form['itemInfo'],
        'category_id': request.form['category_id'],
        'user_id': request.form['user_id']
    }
    print('item data on save', data)
    Items.save(data)
    flash('Item created')
    return redirect('/item/')

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