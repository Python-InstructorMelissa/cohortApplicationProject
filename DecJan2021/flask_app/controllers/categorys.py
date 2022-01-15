from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.category import Category


@app.route('/category/')
def categories():
    cats=Category.getAll()
    print("all Categories via controller: ", cats)
    return render_template('category.html', cats=cats)

# Hidden route to create new
@app.route('/createCategory/', methods=['POST'])
def createCategory():
    data = {
        'categoryName': request.form['categoryName'],
        'categoryInfo': request.form['categoryInfo']
    }
    Category.save(data)
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