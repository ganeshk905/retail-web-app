from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Base(db.Model, UserMixin):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class Employee(Base):
    """
    Create an Employee table
    """
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(Base):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(Base):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Inventory(Base):
    """
    Create an Inventory table
    """
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=False)
    quantity = db.Column(db.Integer, index=True, unique=False)
    expiry_date = db.Column(db.Date, index=True)

    def __repr__(self):
        return '<Inventory: {}>'.format(self.__tablename__)

prod_counter = 0
def get_next_product_id():
    global prod_counter
    prod_counter = prod_counter+1
    return prod_counter

class Product(Base):
    """
    Create a Products table
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, default=get_next_product_id, primary_key=True)
    category = db.Column(db.String(60), index=True, unique=False)
    available_quantity = db.Column(db.String(60), index=True, unique=False)
    name = db.Column(db.String(60), index=True, unique=False)
    buying_price = db.Column(db.Float, index=True, unique=False)
    retailer_seling_price = db.Column(db.Float, index=True, unique=False)
    home_delivery_selling_price = db.Column(db.Float, index=True, unique=False)
    counter_selling_price = db.Column(db.Float,index=True, unique=False)

cust_counter = 1000
def get_next_cust_id():
    global cust_counter
    cust_counter = cust_counter+1
    return cust_counter

class Customer(Base):
    """
    Create a Customers table
    """
    __tablename__ = 'customers'
    id = db.Column(db.Integer, default=get_next_cust_id, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=False)
    address = db.Column(db.String(400), index=True, unique=False)
    mobile = db.Column(db.BigInteger, index=True, unique=False)
    products = db.Column(db.String(200), index=True, unique=False)
    frequency = db.Column(db.String(60), index=True, unique=False)
    start_subsc_date = db.Column(db.Date, index=True, unique=False)
    is_active = db.Column(db.Boolean, index=True, unique=False)

