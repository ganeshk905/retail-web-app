from .. import db
from . import customer
from .. models import Customer
from forms import CustomerForm
from flask_login import current_user, login_required
from flask import abort, flash, redirect, render_template, url_for

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@customer.route('/customers', methods=['GET', 'POST'])
@login_required
def list_customers():
    """
    List all customers
    """
    check_admin()

    customers = Customer.query.all()

    return render_template('customer/customers.html',
                           customers=customers, title="Customer")


@customer.route('/customers/add', methods=['GET', 'POST'])
@login_required
def add_customer():
    """
    Add a customer to the database
    """
    check_admin()

    add_customer = True

    form = CustomerForm(active=True)
    if form.validate_on_submit():
        customer = Customer(name=form.name.data,
                          address=form.address.data,
                          mobile=form.mobile.data,
                          products=form.products.data,
                          frequency=form.frequency.data,
                          start_subsc_date=form.start_subsc_date.data,
                          is_active=form.is_active.data)
        try:
            db.session.add(customer)
            db.session.commit()
            flash('You have successfully added a new customer.')
        except:
            # in case customer already exists
            flash('Error: customer already exists.')

        # redirect to departments page
        return redirect(url_for('customer.list_customers'))

    # load department template
    return render_template('customer/customer.html', action="Add",
                           add_customer=add_customer, form=form,
                           title="Add customer")


@customer.route('/customers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_customer(id):
    """
    Edit a customer
    """
    check_admin()

    add_customer = False

    customer = Customer.query.get_or_404(id)
    form = CustomerForm(obj=customer)
    if form.validate_on_submit():
        customer.name = form.name.data
        customer.address = form.address.data
        customer.mobile = form.mobile.data
        customer.products = form.products.data
        customer.frequency = form.frequency.data
        customer.start_subsc_date = form.start_subsc_date.data
        customer.is_active = form.is_active.data
        db.session.commit()
        flash('You have successfully edited the customer.')

        # redirect to the departments page
        return redirect(url_for('customer.list_customers'))

    form.name.data = customer.name
    form.address.data = customer.address
    form.mobile.data = customer.mobile
    form.products.data = customer.products
    form.frequency.data = customer.frequency
    form.start_subsc_date.data = customer.start_subsc_date
    form.is_active.data = customer.is_active

    return render_template('customer/customer.html', action="Edit",
                           add_customer=add_customer, form=form,
                           customer=customer, title="Edit customer")


@customer.route('/customers/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_customer(id):
    """
    Delete a customer from the database
    """
    check_admin()

    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    flash('You have successfully deleted the customer.')

    # redirect to the departments page
    return redirect(url_for('customer.list_customers'))

    return render_template(title="Delete customer")