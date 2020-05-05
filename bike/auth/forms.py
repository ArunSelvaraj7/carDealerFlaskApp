from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import EqualTo, Email,Length,DataRequired,ValidationError

class Registration_form(FlaskForm):
    name=StringField("Enter your name/username",validators=[DataRequired(),Length(3,15,message='character lenght should be between 3 & 15')])
    email=StringField("Enter your email",validators=[DataRequired(),Email()])
    password=PasswordField("Enter your password",validators=[DataRequired(),EqualTo('confirm',message='password does not match')])
    confirm=PasswordField("confirm your password",validators=[DataRequired()])
    submit=SubmitField()
    

class Login_form(FlaskForm):
    email=StringField("Enter your registered email",validators=[DataRequired(),Email()])
    password=PasswordField("Enter your password",validators=[DataRequired()])
    stay_logged_in=BooleanField("Stay logged in")
    submit=SubmitField()