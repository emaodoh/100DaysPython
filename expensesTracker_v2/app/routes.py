from flask import  Blueprint, render_template, request, redirect, flash, url_for
from .models import Expense
from . import storage 
from . import services
from . services import expenses


main = Blueprint("main", __name__)



@main.route("/")
def home():
    
    
    statistics = services.expense_statistics(expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        statistics=statistics
    )

@main.route("/edit_expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):
    expense = services.get_expense_by_id(id)
    if  expense:

        

        if request.method == "POST":
                
            date = request.form["date"]
            category = request.form["category"]
            price = float (request.form["price"])
            item = request.form["item"]

            services.update_expense(expense, category, item, price, date)
            flash("Expense have been updated successfully")
            return redirect(url_for("main.home"))


        return render_template(
            "edit.html",
            expense=expense
        )

    return "Expense not found"

@main.route("/delete_expense/<int:id>")
def delete_expense(id):
    
   
    services.delete_expense(id)
    flash("Expenses deleted successfully")

    return redirect(url_for("main.home"))

@main.route("/add_expense", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST":

        category = request.form["category"]
        item = request.form["item"]
        price = float (request.form["price"])
        date = str(request.form["date"])
        new_id = len(expenses) +1

        services.add_expense(new_id, category, item, date, price)
        

        flash("Expense added successfully!", "success")
        return redirect(url_for("main.home"))

    return render_template("add.html")
