from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from ..models import Quantity, ProductCategory
from wtforms import FloatField, StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class ProductForm(FlaskForm):
    """
    Form to add a new product
    """
    category = QuerySelectField('Category', query_factory=lambda: ProductCategory.query.all(),
                                get_label="name", validators=[DataRequired()])
    name = StringField('Product Name', validators=[DataRequired()])
    quantity = QuerySelectField('Quantity', query_factory=lambda: Quantity.query.all(),
                                get_label="name", validators=[DataRequired()])
    buying_price = FloatField('Buying Price', validators=[DataRequired()])
    retailer_seling_price = FloatField('Retailer selling Price', validators=[DataRequired()])
    home_delivery_selling_price = FloatField('HD Selling Price', validators=[DataRequired()])
    counter_selling_price = FloatField('Counter Selling Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

