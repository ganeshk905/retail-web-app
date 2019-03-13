from .. import db
from . import product
from .. models import Product
from forms import ProductForm
from flask_login import current_user, login_required
from flask import abort, flash, redirect, render_template, url_for

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@product.route('/products', methods=['GET', 'POST'])
@login_required
def list_products():
    """
    List all departments
    """
    check_admin()

    products = Product.query.all()

    return render_template('product/products.html',
                           products=products, title="Products")


@product.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    """
    Add a department to the database
    """
    check_admin()

    add_product = True

    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data,
                          category=form.category.data,
                          available_quantity=form.available_quantity.data,
                          buying_price=form.buying_price.data,
                          retailer_seling_price=form.retailer_seling_price.data,
                          home_delivery_selling_price=form.home_delivery_selling_price.data,
                          counter_selling_price=form.counter_selling_price.data)
        try:
            db.session.add(product)
            db.session.commit()
            flash('You have successfully added a new product.')
        except:
            # in case product name already exists
            flash('Error: product name already exists.')

        # redirect to departments page
        return redirect(url_for('product.list_products'))

    # load department template
    return render_template('product/product.html', action="Add",
                           add_product=add_product, form=form,
                           title="Add Product")


@product.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    """
    Edit a product
    """
    check_admin()

    add_product = False

    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.category.data
        product.category = form.category.data
        product.available_quantity = form.available_quantity.data
        product.buying_price = form.buying_price.data
        product.retailer_seling_price = form.retailer_seling_price.data
        product.home_delivery_selling_price = form.home_delivery_selling_price.data
        product.counter_selling_price = form.counter_selling_price.data
        db.session.commit()
        flash('You have successfully edited the product.')

        # redirect to the departments page
        return redirect(url_for('product.list_products'))

    form.name.data = product.name
    form.category.data = product.category
    form.available_quantity.data = product.available_quantity
    form.buying_price.data = product.buying_price
    form.retailer_seling_price.data = product.retailer_seling_price
    form.home_delivery_selling_price.data = product.home_delivery_selling_price
    form.counter_selling_price.data = product.counter_selling_price

    return render_template('product/product.html', action="Edit",
                           add_product=add_product, form=form,
                           product=product, title="Edit Product")


@product.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    """
    Delete a product from the database
    """
    check_admin()

    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('You have successfully deleted the product.')

    # redirect to the departments page
    return redirect(url_for('product.list_products'))

    return render_template(title="Delete Product")