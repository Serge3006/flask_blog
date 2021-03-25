from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class EditUserForm(FlaskForm):
    name = StringField("Real Name", validators=[DataRequired(), Length(0, 64)])
    location = StringField("Location", validators=[DataRequired(), Length(0, 64)])
    about_me = TextAreaField("About me")
    submit = SubmitField("Submit")