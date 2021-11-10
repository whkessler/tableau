from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/covid')
def data():
    if 'user_id' not in session:
        flash('Please login')
        return redirect('/')

    return render_template('dashboard.html')

@app.route('/2020data')
def world():
    if 'user_id' not in session:
        flash('Please login')
        return redirect('/')

    return render_template('cases2020.html')

@app.route('/month')
def month():
    if 'user_id' not in session:
        flash('Please login')
        return redirect('/')

    return render_template('month.html')

@app.route('/continent')
def continent():
    if 'user_id' not in session:
        flash('Please login')
        return redirect('/')

    return render_template('continents.html')