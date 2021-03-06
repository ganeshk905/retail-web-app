from .. import db
from . import home
from flask import abort, render_template, flash
from flask_login import current_user, login_required
from .. models import Sale, Expense, Stock

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

def list_expenses():
    """
    List all expenses
    """
    pass

@home.route('/manager/dashboard')
@login_required
def manager_dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    balance = 0.0
    items = []
    try:
        items = list()

        sale_items = db.session.query(Sale.amount).all()
        sales = 0.0
        for s in sale_items:
            sales+=s[0]

        items.append(("Sales",sales))


        expense_items = db.session.query(Expense.amount).all()
        expenses = 0.0
        for e in expense_items:
            expenses += e[0]

        items.append(("Expenses", expenses))

        stock_items = db.session.query(Stock.amount).all()
        stocks = 0.0
        for s in stock_items:
            stocks += s[0]

        items.append(("Stock", stocks))

        balance = 0.0
        for i in items:
            if i[0] == "Sales":
                balance += i[1]
                continue
            balance -= i[1]

    except Exception as e:
        flash("Something went wrong while updating dashboard, please contact your administrator")

    return render_template('home/manager_dashboard.html', title="Dashboard", items=items, balance=balance)


