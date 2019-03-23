from .. import db
from . import sale
from .forms import SaleForm
from .. models import Sale, Product
from flask_login import current_user, login_required
from flask import abort, flash, redirect, render_template, url_for

def check_manager():
    """
    Prevent non-managers from accessing the page
    """
    if not current_user.is_manager:
        abort(403)

@sale.route('/sales', methods=['GET', 'POST'])
@login_required
def list_sales():
    """
    List all sale
    """
    check_manager()

    sales = Sale.query.all()

    return render_template('sale/sales.html',
                           sales=sales, title="Sales")

def getAmount(p_id, category, quantity):
    price = 0.0
    product = db.session.query(Product).filter(Product.id == p_id).first()
    if category == "Counter" or category == "Other":
        price = product.counter_selling_price
    elif category == "Delivery":
        price = product.home_delivery_selling_price
    elif category == "Retailer":
        price = product.retailer_seling_price

    return quantity * price

@sale.route('/sales/add', methods=['GET', 'POST'])
@login_required
def add_sale():
    """
    Add a sale to the database
    """
    check_manager()

    add_sale = True

    form = SaleForm()
    if form.validate_on_submit():
        try:
            sale = Sale(product_id=form.product_id.data.id,
                        category=form.category.data.name,
                        quantity=form.quantity.data,
                        remark=form.remark.data,
                        amount=getAmount(form.product_id.data.id,
                                         form.category.data.name,
                                         form.quantity.data))

            db.session.add(sale)
            db.session.commit()
            flash('You have successfully added a new sale item.')
        except Exception as e:
            flash(str(e))
            db.session.rollback()
            # in case sale name already exists
            flash('Error: sale item already exists.')

        # redirect to sales page
        return redirect(url_for('sale.list_sales'))

    # load sale template
    return render_template('sale/sale.html', action="Add", add_sale=add_sale, form=form, title="Add Sale Item")


@sale.route('/sales/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_sale(id):
    """
    Edit a sale
    """
    check_manager()

    add_sale = False

    sale = Sale.query.get_or_404(id)
    form = SaleForm(obj=sale)
    if form.validate_on_submit():
        sale.product_id = form.product_id.data.id
        sale.category = form.category.data.name
        sale.quantity = form.quantity.data
        sale.remark = form.remark.data
        sale.amount = getAmount(form.product_id.data.id,
                                form.category.data.name,
                                form.quantity.data)

        db.session.commit()
        flash('You have successfully edited the sale.')

        # redirect to the sales page
        return redirect(url_for('sale.list_sales'))
    else:
        form.product_id.data.id = sale.product_id
        form.category.data.name = sale.category
        form.remark.data = sale.remark
        form.quantity.data = sale.quantity

    return render_template('sale/sale.html', action="Edit",add_sale=add_sale,
                           form=form, sale=sale, title="Edit Sale Item")


@sale.route('/sales/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_sale(id):
    """
    Delete a sale from the database
    """
    check_manager()

    sale = Sale.query.get_or_404(id)
    db.session.delete(sale)
    db.session.commit()
    flash('You have successfully deleted the sale.')

    # redirect to the sales page
    return redirect(url_for('sale.list_sales'))

    return render_template(title="Delete Sale Item")
