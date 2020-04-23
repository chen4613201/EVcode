from flask_wtf import FlaskForm
from wtforms import form,StringField,validators,SubmitField
import email_validator


class email_verification(FlaskForm):
    email = StringField(label="Email", validators= [validators.DataRequired("Email is required."),validators.Email("Email address format is incorrect.")])
    veri_code = StringField(label="Verification code", validators=[validators.DataRequired("Verification code is required."),validators.NumberRange(max=6)])
    submit = SubmitField()