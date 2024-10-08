"""Forms Class"""
from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    """Creating Login Form contains email and password"""
    email = StringField("Email", validators=[
        validators.Length(min=7, max=50),
        validators.DataRequired(message="Please Fill This Field")
        ])
    password = PasswordField("Password", validators=[
        validators.DataRequired(message="Please Fill This Field")
        ])

class RegisterForm(Form):
    """Creating Registration Form contains username, name, email, password and confirm password."""
    name = StringField("Full Name", validators=[
        validators.Length(min=3, max=25),
         validators.DataRequired(message="Please Fill This Field")
         ])
    username = StringField("Username", validators=[
        validators.Length(min=3, max=25),
         validators.DataRequired(message="Please Fill This Field")
         ])
    email = StringField("Email", validators=[
        validators.Email(message="Please enter a valid email address")
        ])
    password = PasswordField("Password", validators=[
        validators.Length(min=12),
        validators.DataRequired(message="Please Fill This Field"),
        validators.EqualTo(fieldname="confirm", message="Your Passwords Do Not Match")
    ])

    confirm = PasswordField("Confirm Password", validators=[
        validators.Length(min=12),
        validators.DataRequired(message="Please Fill This Field")])