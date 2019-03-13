from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    """
    Form for users to create new account
    """
    quantity_list = dict()
    quantity_list[1] = [(1, "500 ml"), (2, "1 ltr")]
    quantity_list[2] = [(1, "80 gm"), (2, "100 gm"), (3, "125 gm"), (4, "200 gm"),
                        (5, "250 gm"), (6, "400 gm"), (7, "500 gm"), (8, "1 kg"),
                        (9, "200 ml"), (10, "250 ml"), (11, "500 ml"), (12, "1 ltr"),]
    category = SelectField('Category', choices=[(1, "Milk"),(2, "Bi-Products"),(3, "Ice-cream"),(4, "Other")], validators=[DataRequired()])
    name = StringField('Product Name', validators=[DataRequired()])
    available_quantity = SelectField('Available quantity',
                                     choices=[(1, "Milk"),(2, "Bi-Products"),(3, "Ice-cream"),(4, "Other")],
                                     validators=[DataRequired()])
    buying_price = FloatField('Buying Price', validators=[DataRequired()])
    retailer_seling_price = FloatField('Retailer selling Price', validators=[DataRequired()])
    home_delivery_selling_price = FloatField('HD Selling Price', validators=[DataRequired()])
    counter_selling_price = FloatField('Counter Selling Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

