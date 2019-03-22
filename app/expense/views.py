from .. import db
from . import expense
from .. models import Expense
from .forms import ExpenseForm
from flask_login import current_user, login_required
from flask import abort, flash, redirect, render_template, url_for

def check_manager():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_manager:
        abort(403)

@expense.route('/expenses', methods=['GET', 'POST'])
@login_required
def list_expenses():
    """
    List all expenses
    """
    check_manager()

    expenses = Expense.query.all()

    return render_template('expense/expenses.html',
                           expenses=expenses, title="Expenses")


@expense.route('/expenses/add', methods=['GET', 'POST'])
@login_required
def add_expense():
    """
    Add a expense to the database
    """
    check_manager()

    add_expense = True

    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(category=form.category.data.name,
                          description=form.description.data,
                          amount=form.amount.data)
        try:
            db.session.add(expense)
            db.session.commit()
            flash('You have successfully added a new expense.')
        except:
            # in case expense already exists
            flash('Error: expense already exists.')

        # redirect to expenses page
        return redirect(url_for('expense.list_expenses'))

    # load expense template
    return render_template('expense/expense.html', action="Add",
                           add_expense=add_expense, form=form,
                           title="Add expense")


@expense.route('/expenses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    """
    Edit a expense
    """
    check_manager()

    add_expense = False

    expense = Expense.query.get_or_404(id)
    form = ExpenseForm(obj=expense)
    if form.validate_on_submit():
        expense.category = form.category.data.name
        expense.description = form.description.data
        expense.amount = form.amount.data
        db.session.commit()
        flash('You have successfully edited the expense.')

        # redirect to the expenses page
        return redirect(url_for('expense.list_expenses'))

    form.category.data.name = expense.category
    form.description.data = expense.description
    form.amount.data = expense.amount
    
    return render_template('expense/expense.html', action="Edit",
                           add_expense=add_expense, form=form,
                           expense=expense, title="Edit expense")


@expense.route('/expenses/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_expense(id):
    """
    Delete a expense from the database
    """
    check_manager()

    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('You have successfully deleted the expense.')

    # redirect to the expenses page
    return redirect(url_for('expense.list_expenses'))

    return render_template(title="Delete expense")
