from app import db
import configparser
from app.models import Employee, Product, ProductCategory, SaleCategory, Quantity, DeliveryFrequency, ExpenseCategory

class Initialize:

    def add(self, item):
        db.session.add(item)

    def commit(self):
        db.session.commit()

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("data/initializers.ini")

    def readItem(self, section, key):
        return self.config.get(section, key).strip().split(',')

    def initAdmin(self, data):
        self.add(Employee(email=data[0], username=data[1], password=data[2], is_admin=True))

    def initManager(self, data):
        self.add(Employee(email=data[0], username=data[1], password=data[2], is_manager=True))

    def initUsers(self):
        admin_data = self.readItem("DEFAULT", "admin")
        self.initAdmin(admin_data)
        manager_data = self.readItem("DEFAULT", "manager")
        self.initManager(manager_data)

    def initProducts(self):
        product_list = ["product1", "product2", "product3", "product4"]

        for product in product_list:
            data = self.readItem("PRODUCTS", product)
            self.add(Product(name=data[0], category=data[1], quantity=data[2],
                             buying_price=data[3], retailer_seling_price=data[4],
                             home_delivery_selling_price=data[5], counter_selling_price=data[6]))

    def initQuantities(self, section, key):
        quantities = self.readItem(section, key)
        for quantity in quantities:
            self.add(Quantity(name=quantity))

    def initProductCategory(self):
        product_data = self.readItem("PRODUCTS","types")
        for item in product_data:
            self.add(ProductCategory(name=item))
            self.initQuantities(item.upper(), "quantities")

    def initSaleCategory(self):
        categories = self.readItem("SALES","categories")
        for category in categories:
            self.add(SaleCategory(name=category))

    def initFrequencies(self):
        frequencies = self.readItem("FREQUENCIES","frequency")
        for frequency in frequencies:
            self.add(DeliveryFrequency(name=frequency))

    def initExpenseCategories(self):
        categories = self.readItem("EXPENSES", "categories")
        for category in categories:
            self.add(ExpenseCategory(name=category))

    def main(self):
        self.initUsers()
        self.initProducts()
        self.initProductCategory()
        self.initFrequencies()
        self.initSaleCategory()
        self.initExpenseCategories()
        self.commit()

def initialize():
    init = Initialize()
    init.main()
