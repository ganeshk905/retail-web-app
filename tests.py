import unittest

from flask_testing import TestCase
from datetime import date
from flask import abort, url_for
from app import create_app, db
from app.models import Department, Employee, Role, Stock, Product, Customer
import initdb

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://admin_test:tadmin@localhost/myapp_test'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()
        initdb.initialize()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_employee_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Employee.query.count(), 2)

    def test_department_model(self):
        """
        Test number of records in Department table
        """

        # create test department
        department = Department(name="IT", description="The IT Department")

        # save department to database
        db.session.add(department)
        db.session.commit()

        self.assertEqual(Department.query.count(), 1)

    def test_role_model(self):
        """
        Test number of records in Role table
        """

        # create test role
        role = Role(name="CEO", description="Run the whole company")

        # save role to database
        db.session.add(role)
        db.session.commit()

        self.assertEqual(Role.query.count(), 1)

    def test_inventory_model(self):
        """
        Test number of records in Inventory table
        """

        # create test stock
        inventory = Stock(id=0, name="RCM",
                          quantity=10, expiry_date=date(2002, 12, 31))

        # save stock to database
        db.session.add(inventory)
        db.session.commit()

        self.assertEqual(Stock.query.count(), 1)

    def test_product_model(self):
        """
        Test number of records in Product table
        """

        # create test product
        product = Product(category="Milk",
                          available_quantity=100,
                          name="RBM", buying_price=45,
                          retailer_seling_price=48,
                          home_delivery_selling_price=50,
                          counter_selling_price=52)

        # save product to database
        db.session.add(product)
        db.session.commit()

        self.assertEqual(Product.query.count(), 5)

    def test_customer_model(self):
        """
        Test number of records in Customer table
        """

        # create test customer
        customer = Customer(name="Test Customer",
                            address="Test Road, Test City",
                            mobile=1234567890,
                            products="Test Product",
                            frequency="Daily",
                            start_subsc_date=date(2002, 12, 31),
                            is_active=True)

        # save customer to database
        db.session.add(customer)
        db.session.commit()

        self.assertEqual(Customer.query.count(), 1)

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_admin_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.admin_dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_departments_view(self):
        """
        Test that departments page is inaccessible without login
        and redirects to login page then to departments page
        """
        target_url = url_for('admin.list_departments')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_roles_view(self):
        """
        Test that roles page is inaccessible without login
        and redirects to login page then to roles page
        """
        target_url = url_for('admin.list_roles')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_employees_view(self):
        """
        Test that employees page is inaccessible without login
        and redirects to login page then to employees page
        """
        target_url = url_for('admin.list_employees')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_products_view(self):
        """
        Test that products page is inaccessible without login
        and redirects to login page then to products page
        """
        target_url = url_for('product.list_products')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_customers_view(self):
        """
        Test that customers page is inaccessible without login
        and redirects to login page then to customers page
        """
        target_url = url_for('customer.list_customers')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_inventory_view(self):
        """
        Test that stock page is inaccessible without login
        and redirects to login page then to stock page
        """
        target_url = url_for('stock.list_inventory')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

class TestErrorPages(TestBase):

    def test_403_forbidden(self):
        # create route to abort the request with the 403 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        self.assertTrue("403 Error" in response.data)

    def test_404_not_found(self):
        response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error" in response.data)

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error" in response.data)

if __name__ == '__main__':
    unittest.main()
