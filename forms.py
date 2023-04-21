from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, DateField
from wtforms import FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import datetime


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[NumberRange(min=0)])
    cost = FloatField('Cost', validators=[DataRequired(), NumberRange(min=0)])


class ServiceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired(), NumberRange(min=0)])


class InvoiceItemForm(FlaskForm):
    product_id = SelectField('Product', choices=[], validators=[DataRequired()])
    service_id = SelectField('Service', choices=[], validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    cost = FloatField('Cost', validators=[DataRequired(), NumberRange(min=0)])


class InvoiceForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], default=datetime.date.today())
    type = SelectField('Type', choices=[('in', 'Income'), ('out', 'Outcome')], validators=[DataRequired()])
    items = FieldList(FormField(InvoiceItemForm), min_entries=1)
    submit = SubmitField('Save')