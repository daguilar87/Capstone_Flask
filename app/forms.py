from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class CreateService(FlaskForm):
    name = StringField("Service Name", validators = [DataRequired()])
    details1 = StringField('Details1')
    details2 = StringField('Details2')
    details3 = StringField('Details3')
    details4 = StringField('Details4')
    details5 = StringField('Details5')
    details6 = StringField('Details6')
    details7 = StringField('Details7')
    details8 = StringField('Details8')
    img_url = StringField('img')
    price = IntegerField('Price')
    submit = SubmitField()


class UpdateService(FlaskForm):
    name = StringField("Service Name")
    details1 = StringField('Details1')
    details2 = StringField('Details2')
    details3 = StringField('Details3')
    details4 = StringField('Details4')
    details5 = StringField('Details5')
    details6 = StringField('Details6')
    details7 = StringField('Details7')
    details8 = StringField('Details8')
    img_url = StringField('img')
    price = IntegerField('Price')
    submit = SubmitField()

class Createaddon(FlaskForm):
    det1 = StringField('det1')
    det2 = StringField('det2')
    det3 = StringField('det3')
    det4 = StringField('det4')
    submit = SubmitField()


class Updateaddon(FlaskForm):
    det1 = StringField('det1')
    det2 = StringField('det2')
    det3 = StringField('det3')
    det4 = StringField('det4')
    submit = SubmitField()

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField("Confirm", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()