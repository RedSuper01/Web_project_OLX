from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для входа в аккаунт
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')