from ..models import Product
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, IntegerField, SubmitField

class StockForm(FlaskForm):
    """
    Form for users to create new account
    """
    product_id =  QuerySelectField("Product ID", query_factory=lambda: Product.query.all(),
                                      get_label="id")
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    expiry_date = DateField('Expiry Date', format='%Y-%m-%d', validators=[DataRequired()])
    remark = StringField('Remark', validators=[DataRequired()])
    submit = SubmitField('Submit')

