from flask_wtf import FlaskForm
from wtforms import form,StringField,validators,SubmitField,ValidationError


class email_verification(FlaskForm):
    email = StringField(label="Email", validators= [validators.DataRequired("Email address is required."),validators.Email("Email address format is incorrect.")])
    veri_code = StringField(label="Verification Code", validators=[validators.DataRequired("Verification Code is required.")])
    submit = SubmitField()

    def valid_veri_code(self,field,compare_value):
        print("begin")
        print(field)
        print(compare_value)
        if field != compare_value:
            print("end")
            raise validators.ValidationError("The Verification Code is incorrect.")