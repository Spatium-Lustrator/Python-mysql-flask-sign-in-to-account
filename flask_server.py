from flask import Flask, render_template, request
from db_requests import Requester

requester = Requester()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('sign_in_page.html')


@app.route('/check-admins/', methods=["GET"])
def check_admins():
    login = request.args.get('login')
    password = request.args.get('password')
    password_from_bd = requester.return_admin_password(login)
    if password == password_from_bd:
        return render_template('account_page.html')
    else:
        return render_template('sign_in_page.html')


if __name__ == '__main__':
    app.run(debug=True)
