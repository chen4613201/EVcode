from flask import Flask,render_template,url_for,request,send_from_directory,session
from form import email_verification
from flask_bootstrap import Bootstrap
from flask_mail import Mail,Message
import random


app = Flask(__name__,static_folder="statics")
app.config.from_pyfile('config.py')

app.config['MAIL_SERVER'] = 'mail.ancam-tech.com'
app.config['MAIL_PORT'] = 26
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'service@ancam-tech.com'
app.config['MAIL_PASSWORD'] = 'ZXCV1qaz!@#$'


bootstrap = Bootstrap(app)
mail = Mail(app)


@app.route("/", methods=["POST","GET"])
def index():
    email_form = email_verification()

    if request.method=="POST" and email_form.validate_on_submit():
        #if request.form.get('veri_code') == session["veri_code"]:
        #return send_from_directory(r"./appfile",filename="Bluetooth_notification.apk",as_attachment=True)
        pass

    return render_template("index.html", email_form=email_form)

def gen_code():
    str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(4):
        num = random.randint(0, len(str1) - 1)
        code += str1[num]
    return code


@app.route("/send_email",methods=["POST"])
def send_email():
    customer_email = request.values.get("user_email")
    print("+++++"+customer_email)
    #print("send_email:"+user_email)
    session["veri_code"] = gen_code()
    print("send_email:session"+session["veri_code"])

    print("-------"+app.config.get('SMTP_SENDER'))
    email_sender = app.config.get('SMTP_SENDER')
    msg_body = str('Hey ' + customer_email + '!\n\n  Verification code:' + session["veri_code"]+'\nThanks,\nThe ANCwear Team')
    msg=Message("ANCwear App Download", body=msg_body, sender=email_sender,recipients=[customer_email])

    with app.app_context():
        mail.send(msg)
    print("send_email:Send Successfully!")
    return "Send Successfully!"


if __name__ == "__main__":
    app.run(debug=True)