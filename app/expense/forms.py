from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, FloatField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .. models import ExpenseCategory

class ExpenseForm(FlaskForm):
    """
    Form to record expenses
    """
    category = QuerySelectField("Category", query_factory=lambda: ExpenseCategory.query.all(),
                           get_label="name",validators=[DataRequired()] )
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

