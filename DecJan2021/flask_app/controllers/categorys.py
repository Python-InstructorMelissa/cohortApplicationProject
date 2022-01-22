from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.category import Category
from flask_app.models.user import User


@app.route('/category/')
def categories():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        cats=Category.getAll()
        print("all Categories via controller: ", cats)
        return render_template('category.html', cats=cats, user=user)

# Hidden route to create new
@app.route('/createCategory/', methods=['POST'])
def createCategory():
    data = {
        'categoryName': request.form['categoryName'],
        'categoryInfo': request.form['categoryInfo']
    }
    Category.save(data)
    flash('Category Created')
    return redirect('/category/')

@app.route('/category/<int:category_id>/view/')
def viewCategory(category_id):
    pass

# view all the items associated with a single category
@app.route('/category/<int:category_id>/items/')
def catItems(category_id):
    pass

# Hidden route to update category
@app.route('/category/<int:category_id>/update/', methods=['POST'])
def updateCategory(category_id):
    pass

# Hidden route to delete category
@app.route('/category/<int:category_id>/delete/')
def deleteCategory(category_id):
    pass