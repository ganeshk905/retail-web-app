from .. import db
from . import inventory
from ..models import Inventory
from .forms import InventoryForm
from flask_login import current_user, login_required
from flask import abort, render_template, redirect, url_for, flash

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@inventory.route('/inventory', methods=['GET', 'POST'])
@login_required
def list_inventory():
    """
    List all items
    """
    check_admin()

    items = Inventory.query.all()

    return render_template('inventory/inventory.html',
                           inventory=items, title="Inventory")


@inventory.route('/inventory/add', methods=['GET', 'POST'])
@login_required
def add_inventory():
    """
    Add a department to the database
    """
    check_admin()

    add_inventory = True

    form = InventoryForm()
    if form.validate_on_submit():
        item = Inventory(id=form.id.data,product=form.product.data,
                          quantity=form.quantity.data,expiry_date=form.expiry_date.data)
        try:
            db.session.add(item)
            db.session.commit()
            flash('You have successfully added a new inventory item.')
        except:
            # in case product name already exists
            flash('Error: inventory item already exists.')

        # redirect to departments page
        return redirect(url_for('inventory.list_inventory'))

    # load department template
    return render_template('inventory/inventoryitem.html', action="Add",
                           add_inventory=add_inventory, form=form, title="Add Inventory")


@inventory.route('/inventory/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_inventory(id):
    """
    Edit a product
    """
    check_admin()

    add_inventory = False

    item = Inventory.query.get_or_404(id)
    form = InventoryForm(obj=item)
    if form.validate_on_submit():
        item.id = form.id.data
        item.product = form.product.data
        item.quantity = form.quantity.data
        item.exp_date = form.exp_date.data
        db.session.commit()
        flash('You have successfully edited the inventory item.')

        # redirect to the departments page
        return redirect(url_for('inventory.list_inventory'))

    form.id.data = item.id
    form.product.data = item.product
    form.quantity.data = item.quantity
    form.exp_date.data = item.exp_date

    return render_template('inventory/inventory.html', action="Edit",
                           add_inventory=add_inventory, form=form,
                           inventory=inventory, title="Edit Inventory")


@inventory.route('/inventory/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_inventory(id):
    """
    Delete a inventory from the database
    """
    check_admin()

    item = Inventory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('You have successfully deleted the inventory item.')

    # redirect to the departments page
    return redirect(url_for('inventory.list_inventory'))

    return render_template(title="Delete Inventory Item")


