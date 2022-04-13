from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, EmailField, PasswordField, StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import  DataRequired


# Форма для добавления пользователей в базу данных(регистрация)
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    contacts = StringField('Contacts', validators=[DataRequired()])
    email = EmailField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = StringField('Repeat password', validators=[DataRequired()])
    photo = FileField('Your avatar')
    bag = ''
    submit = SubmitField('Submit')