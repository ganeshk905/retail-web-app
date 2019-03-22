from .. import db
from . import stock
from ..models import Stock, Product
from .forms import StockForm
from flask_login import current_user, login_required
from flask import abort, render_template, redirect, url_for, flash

def check_manager():
    """
    Prevent non-manager from accessing the page
    """
    if not current_user.is_manager:
        abort(403)

def getAmount(productID, quantity):
    product = db.session.query(Product).filter(Product.id == productID).first()
    return quantity * product.buying_price


@stock.route('/stocks', methods=['GET', 'POST'])
@login_required
def list_stock():
    """
    List all stocks
    """
    check_manager()

    stocks = Stock.query.all()

    return render_template('stock/stocks.html',
                           stocks=stocks, title="stock")


@stock.route('/stock/add', methods=['GET', 'POST'])
@login_required
def add_stock():
    """
    Add a department to the database
    """
    check_manager()

    add_stock = True

    form = StockForm()
    if form.validate_on_submit():
        stock = Stock(product_id=form.product_id.data.id,
                      quantity=form.quantity.data,
                      expiry_date=form.expiry_date.data,
                      amount=getAmount(form.product_id.data.id,
                                       form.quantity.data))
        try:
            db.session.add(stock)
            db.session.commit()
            flash('You have successfully added a new stock.')
        except :
            # in case product name already exists
            flash('Error: stock stock already exists.')

        # redirect to departments page
        return redirect(url_for('stock.list_stock'))

    # load department template
    return render_template('stock/stock.html', action="Add",
                           add_stock=add_stock, form=form, title="Add stock")


@stock.route('/stock/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_stock(id):
    """
    Edit a product
    """
    check_manager()

    add_stock = False

    stock = Stock.query.get_or_404(id)
    form = StockForm(obj=stock)
    if form.validate_on_submit():
        stock.product_id = form.product_id.data.id
        stock.quantity = form.quantity.data
        stock.exp_date = form.exp_date.data
        stock.amount = getAmount(form.product_id.data.id,
                                 form.quantity.data)
        db.session.commit()
        flash('You have successfully edited the stock.')

        # redirect to the departments page
        return redirect(url_for('stock.list_stock'))

    form.product_id.data.id = stock.product_id
    form.quantity.data = stock.quantity
    form.exp_date.data = stock.exp_date

    return render_template('stock/stock.html', action="Edit",
                           add_stock=add_stock, form=form,
                           stock=stock, title="Edit stock")


@stock.route('/stock/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_stock(id):
    """
    Delete a stock from the database
    """
    check_manager()

    stock = Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    flash('You have successfully deleted the stock stock.')

    # redirect to the departments page
    return redirect(url_for('stock.list_stock'))

    return render_template(title="Delete stock stock")


