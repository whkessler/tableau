from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def logon():
    return render_template('logon.html')

@app.route('/users/register', methods=['POST'])
def register_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }
    valid = User.validate_registration(data)
    if valid:
        User.create_user(data)
        flash('Account Created - Login Below')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():

    data ={
        'email': request.form['email'] 
    }
    user = User.get_user_by_email(data)

    if user == None:
        flash('Email is invalid')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is incorrect')
        return redirect('/')

    session['user_id'] = user.id
    session['user_email'] = user.email
    session['user_first_name'] = user.first_name
    session['user_last_name'] = user.last_name

    return redirect('/covid')

@app.route('/logout')
def logout():
    session.clear()
    if 'email' not in session:
        flash('User not loged in')
    return redirect('/')
