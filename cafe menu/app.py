from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from models import db, User, MenuItem, Order
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/cafemenu'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)


migrate = Migrate(app, db)

@app.route('/')
def menu():
    items = MenuItem.query.all()
    return render_template('menu.html', items=items)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)
