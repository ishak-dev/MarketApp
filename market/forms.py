from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo,Email,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username exist')
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already used')
    username = StringField(label='username',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='email',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='password',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='submit')




class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired()])
    password = StringField(label='password',validators=[DataRequired()])
    submit = SubmitField(label='Signin')