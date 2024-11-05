from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

from passwords import _mysql_password

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = _mysql_password
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DicCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html ')

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True)