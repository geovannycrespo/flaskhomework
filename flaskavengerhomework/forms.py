from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo,Email
from flask_wtf import FlaskForm
class SignupForm(FlaskForm):
    avengername = StringField("Avenger's Name", validators=[DataRequired()])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")