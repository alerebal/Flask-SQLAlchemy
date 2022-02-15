from crypt import methods
from unicodedata import category
from flask import redirect, render_template, request, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template('tasks.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/add_category', methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(catagory_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template('add_category.html')