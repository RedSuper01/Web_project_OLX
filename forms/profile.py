from flask_wtf import FlaskForm
from wtforms import FileField, EmailField, StringField, IntegerField, SubmitField
from wtforms.validators import  DataRequired


#Форма для изменения данных в профиле пользователя
class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    contacts = StringField('Contacts', validators=[DataRequired()])
    email = EmailField('Login/email', validators=[DataRequired()])
    photo = FileField('Your avatar')
    submit = SubmitField('Submit')