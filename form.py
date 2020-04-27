from flask_wtf import FlaskForm
from flask import session,current_app
from wtforms import form,StringField,validators,SubmitField,ValidationError


class email_verification(FlaskForm):
    email = StringField(label="Email", validators= [validators.DataRequired("Email address is required."),validators.Email("Email address format is incorrect.")])
    veri_code = StringField(label="Verification Code", validators=[validators.DataRequired("Verification Code is required.")])
    submit = SubmitField()

    def validate_veri_code(form, field):
        current_app.logger.info("I come in")
        if field.data != session.get("veri_code"):
            raise validators.ValidationError("The Verification Code is incorrect,get it again.")

