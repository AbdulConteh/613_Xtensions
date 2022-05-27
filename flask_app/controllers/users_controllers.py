from flask_app import app
from flask_app.models.users_models import User
from flask import redirect, render_template, request

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register')
def register_user():
    data = {
        "first_name" : request.template['first_name'],
        "last_name" : request.template['last_name'],
        "email" : request.template['email'],
        "password" : request.template['password']
    }

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')