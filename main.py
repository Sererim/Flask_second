from flask import Flask, render_template, request
from flask import session, make_response, url_for
from flask import redirect
from werkzeug.utils import secure_filename
from datetime import datetime
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def logged():
    if 'delete' in request.form:
        session.pop('username', None)
        return redirect(url_for('login'))
    else:
        username = request.form.get('uname')
        usermail = request.form.get('uemail')
        userpassword = request.form.get('upass')
    
        response = make_response("Logged in")
        response.set_cookie('username', username)
        response.set_cookie('usermail', usermail)
        time: str =  f"{datetime.now()}"
        return render_template('login.html', uname=username, time=time)


if __name__ == "__main__":
    app.run(debug=True)
