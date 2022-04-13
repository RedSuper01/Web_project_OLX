from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# Форма для сбора информации для сообщений админа
class EmailForm(FlaskForm):
    subject = StringField('Subject of your mail', validators=[DataRequired()])
    description = TextAreaField('Text of  your mail', validators=[DataRequired()])
    submit = SubmitField('Submit')