from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FileField, BooleanField
from wtforms.validators import DataRequired


class GoodsForm(FlaskForm):
    good = StringField('Name of the good', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo of the good', validators=[DataRequired()])
    contacts = StringField('Contacts', validators=[DataRequired()])
    is_sold = BooleanField('Have you sold it?')
    submit = SubmitField('Submit')