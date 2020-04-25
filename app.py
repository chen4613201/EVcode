from flask import Flask,render_template,url_for,request,send_from_directory,session,flash,redirect
from form import email_verification
from flask_bootstrap import Bootstrap
from flask_mail import Mail,Message
import random
from db import db
import pymysql

app = Flask(__name__,static_folder="statics")
app.config.from_pyfile('config.py')

db.init_app(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

from model import Download_Record


@app.route("/", methods=["POST","GET"])
def index():
    email_form = email_verification()

    if request.method=="POST" and email_form.validate_on_submit():
        veri_code = request.form.get('veri_code')
        user_email = request.form.get('email')
        print("++++++:"+session.get("veri_code"))
        if veri_code == session.get("veri_code"):
            #db.drop_all()
            #db.create_all()
            New_Record = Download_Record(User_Email=user_email, Veri_Code=veri_code)
            db.session.add(New_Record)
            db.session.commit()
            email_form.veri_code.errors[:]=[]
            return send_from_directory(r"./appfile",filename="Bluetooth_notification.apk",as_attachment=True)
        else:
            email_form.veri_code.errors.append("The Verification Code is incorrect,click 'Send' button to get it.")

    return render_template("index.html", email_form=email_form)


def gen_code():
    str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(4):
        num = random.randint(0, len(str1) - 1)
        code += str1[num]
    return code


def del_session(session_key):
    if session.get(session_key):
        session.pop(session_key)


@app.route("/send_email",methods=["GET"])
def send_email():
    customer_email = request.values.get("user_email")
    del_session("veri_code")
    session["veri_code"] = gen_code()
    print("------:"+session.get("veri_code"))
    email_sender = app.config.get('MAIL_USERNAME')
    msg_body = str('Hey ' + customer_email + '!\n\n  Verification code:' + session["veri_code"]+'\nThanks,\nThe ANCwear Team')
    msg=Message("ANCwear App Download", body=msg_body, sender=email_sender,recipients=[customer_email])
    try:
        #with app.app_context():
            #mail.send(msg)
        print("send_email:Send Successfully!")
        return "1"
    except Exception as e:
        return "0"


if __name__ == "__main__":
    app.run(debug=True)