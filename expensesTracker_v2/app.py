from flask import Flask, render_template, request, redirect, flash, url_for
from models import Expense
import storage 
import services

expenses = storage.load_expenses()

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route("/")
def home():

    statistics = services.expense_statistics(expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        statistics=statistics
    )

@app.route("/edit_expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    for expense in expenses:

        if expense.new_id == id:

            if request.method == "POST":
                
                expense.date = request.form["date"]
                expense.category = request.form["category"]
                expense.price = float (request.form["price"])
                expense.item = request.form["item"]

                storage.save_expenses(expenses)
                flash("Expense have been updated successfully")
                return redirect(url_for("home"))


            return render_template(
                "edit.html",
                expense=expense
            )

    return "Expense not found"@app.route("/delete/<int:new_id>")

@app.route("/delete_expense/<int:id>")
def delete_expense(id):
    
    for expense in expenses:

        if expense.new_id == id:
            expenses.remove(expense)
            break

    storage.save_expenses(expenses)

    flash("Expenses deleted successfully")

    return redirect(url_for("home"))

@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST":

        category = request.form["category"]
        item = request.form["item"]
        price = float (request.form["price"])
        date = request.form["date"]
        new_id = len(expenses) +1

        user_expense = Expense(new_id, category, item, str(date), price)
        expenses.append(user_expense)
        storage.save_expenses(expenses)

        flash("Expense added successfully!", "success")
        return redirect(url_for("home"))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)