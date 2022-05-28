from flask_app import app
from flask_app.models.users_models import User
from flask_bcrypt import Bcrypt
from flask import flash
from flask import redirect, render_template, request, session
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate_users(request.form):
        return redirect('/')
    data = {
        "first_name" : request.template['first_name'],
        "last_name" : request.template['last_name'],
        "email" : request.template['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.created_user(data)
    print(id)
    session['user_id'] = id
    return redirect("/")

@app.route("/login", methods=['POST'])
def login():
    data = {
        "email" : request.form["email"]
    }
    user = User.get_user(data)
    print(user)
    if not user:
        flash("Unregistered email. Please try again", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password.", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect ('/profile')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')