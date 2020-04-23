from flask import Flask,render_template
from form import email_verification
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY']='dev'
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    email_form = email_verification()
    return render_template("index.html", email_form=email_form)


if __name__ == "__main__":
    app.run(debug=True)