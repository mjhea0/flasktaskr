from flask import Flask, flash, redirect, render_template, request, \
    session, url_for

from functools import wraps
import sqlite3

app = Flask(__name__)
app.config.from_object('config')


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You are logged out. Bye. :(')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            return redirect(url_for('tasks'))
    if request.method == 'GET':
        return render_template('login.html')
