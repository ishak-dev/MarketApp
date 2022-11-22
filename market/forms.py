from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo,Email,DataRequired

class RegisterForm(FlaskForm):
     username = StringField(label='username',validators=[Length(min=2,max=30),DataRequired()])
     email_address=StringField(label='email',validators=[Email(),DataRequired()])
     password1 = PasswordField(label='password',validators=[Length(min=6),DataRequired()])
     password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
     submit = SubmitField(label='submit')



