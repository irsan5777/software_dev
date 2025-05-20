"""
Irsan Sutanto
Project 2 sales website
"""

from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError   # to catch duplicate username/email
from flask_bcrypt import Bcrypt
import random
import json
import psycopg2
import os

app = Flask(__name__)
bcrypt = Bcrypt

#connecting to Postgresql
DB_USERNAME = os.environ.get('DB.USERNAME', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '123')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('sales_webDB')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/sales_webDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a db object
db = SQLAlchemy(app)

TAX_RATE = 0.08875
SHIPPING_COST = 0.00   # free shipping cost

# create a secret key to handle data within our server
app.config['SECRET_KEY']=os.urandom(24)

def get_db_connection():
    """Establishes and returns a database connection."""
    conn = None
    try:
        conn = psycopg2.connect(dbname="sales_webDB", user="postgres", password="123")

        # print("Database connection successful!") # For debugging
    except psycopg2.OperationalError as e:
        print(f"Database connection failed: {e}")
        conn = None # Ensure conn is None if connection fails
    return conn

# --- Helper function to calculate cart totals ---
# This function will now take cart items as a dictionary (from client-side)
def calculate_cart_totals(cart_items):
    """Calculates subtotal, tax, shipping, and total for the given cart items."""
    subtotal = 0
    # cart_items is expected to be a dictionary where values are item details
    for item in cart_items.values():
        # Ensure price and quantity are treated as numbers
        try:
            price = float(item.get('price', 0))
            quantity = int(item.get('quantity', 0))
            subtotal += price * quantity
        except (ValueError, TypeError) as e:
            print(f"Error calculating item total: {e} for item {item}")
            # Handle cases where price or quantity might be invalid

    tax = subtotal * TAX_RATE
    shipping_cost = SHIPPING_COST # Using a flat rate for now
    total = subtotal + tax + shipping_cost
    return subtotal, tax, shipping_cost, total

# --- Routes ---

# Home Route - Product Categories
@app.route('/')
def index():

    """Displays the product categories."""
    # In a real app, you might fetch categories from the database
    # For now, we'll just render the template with hardcoded categories
    categories = [
        {'name': 'Jeans', 'image': 'https://placehold.co/600x200/007bff/ffffff?text=Jeans+Category', 'url_key': 'jeans'},
        {'name': 'Dresses', 'image': 'https://placehold.co/600x200/28a745/ffffff?text=Dresses+Category', 'url_key': 'dresses'},
        # Add more categories here if needed
    ]
    return render_template('index.html', categories=categories)


# Product Listing by Category
@app.route('/products/<category>')
def products_by_category(category):
    """Displays products for a specific category."""
    products = [] # Initialize an empty list for products
    category_name = category.replace('-', ' ').title() # Format category name for display

    conn = get_db_connection()
    if conn is None:
        flash('Database connection error when fetching products.', 'danger')
        return render_template('products.html', category_name=category_name, products=products) # Render with empty list

    cur = conn.cursor()

    try:
        # Fetch products from the 'products' table based on the category
        cur.execute(
            "SELECT id, name, image_url, price FROM products WHERE category = %s",
            (category,) # Pass category as a tuple
        )
        # Fetch all matching rows
        product_rows = cur.fetchall()

        # Convert fetched rows into a list of dictionaries
        products = [{'id': row[0], 'name': row[1], 'image': row[2], 'price': row[3]} for row in product_rows]

    except Exception as e:
        print(f"Error fetching products: {e}")
        flash(f'An error occurred while fetching products for category "{category_name}".', 'danger')
        products = [] # Ensure products is empty on error

    finally:
        if cur:
            cur.close()
        if conn:
                conn.close()

    return render_template('products.html', category_name=category_name, products=products)

# Removed /add_to_cart and /remove_from_cart as cart is handled client-side

@app.route('/cart', methods=['GET'])
def cart():
    """Displays the shopping cart contents."""
    # Cart data is now handled client-side in cart.html using local storage.
    # We only need to render the template and pass the constants for calculations.
    return render_template(
        'cart.html',
        tax_rate=TAX_RATE,
        shipping_cost=SHIPPING_COST
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handles user registration."""
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        address = request.form.get('address')

        # Basic validation (you'll want more robust validation)
        if not all([first_name, last_name, username, password, email, address]):
            flash('All fields are required!', 'danger')
            return render_template('signup.html', form_data=request.form) # Pass form data back to repopulate form

        conn = get_db_connection()
        if conn is None:
            flash('Database connection error.', 'danger')
            return render_template('signup.html', form_data=request.form)

        cur = conn.cursor()

        try:
            # Check for duplicate username or email
            cur.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
            existing_user = cur.fetchone()

            if existing_user:
                flash('Username or Email already exists. Please choose a different one.', 'danger')
                return render_template('signup.html', form_data=request.form) # Pass form data back

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Insert new user into the database
            cur.execute(
                "INSERT INTO users (first_name, last_name, username, password, email, address) VALUES (%s, %s, %s, %s, %s, %s)",
                (first_name, last_name, username, hashed_password, email, address)
            )
            conn.commit() # Commit the transaction

            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login')) # Redirect to the login page

        except Exception as e:
            conn.rollback() # Rollback the transaction on error
            print(f"Error during signup: {e}")
            flash('An error occurred during registration. Please try again.', 'danger')
            return render_template('signup.html', form_data=request.form) # Pass form data back

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    # If it's a GET request, render the signup form
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Basic validation
        if not username or not password:
            flash('Please enter both username and password.', 'danger')
            return render_template('login.html', form_data=request.form) # Pass data back

        conn = get_db_connection()
        if conn is None:
            flash('Database connection error.', 'danger')
            return render_template('login.html', form_data=request.form)

        cur = conn.cursor()

        try:
            # Retrieve user from database by username
            cur.execute("SELECT id, password FROM users WHERE username = %s", (username,))
            user = cur.fetchone() # Fetches one row, or None if no user found

            if user and bcrypt.check_password_hash(user[1], password):
                # Login successful
                session['user_id'] = user[0] # Store user ID in session
                flash('Login successful!', 'success')
                # Redirect to the checkout page after successful login
                return redirect(url_for('checkout'))

            else:
                # Login failed (user not found or password incorrect)
                flash('Invalid username or password.', 'danger')
                return render_template('login.html', form_data=request.form) # Pass data back

        except Exception as e:
            print(f"Error during login: {e}")
            flash('An error occurred during login. Please try again.', 'danger')
            return render_template('login.html', form_data=request.form) # Pass data back

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    # If it's a GET request, render the login form
    return render_template('login.html')

@app.route('/logout')
def logout():
    
    """Logs out the current user."""
    session.pop('user_id', None) # Remove user_id from session
    # Cart is in local storage, no need to clear session cart
    flash('You have been logged out.', 'info')
    return redirect(url_for('index')) # Redirect to home page after logout

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Handles displaying the checkout page and processing order submission."""
    # Ensure user is logged in to access checkout
    if 'user_id' not in session:
        flash('Please log in to proceed to checkout.', 'warning')
        return redirect(url_for('login'))

    user_id = session['user_id']
    cart_items = {} # Initialize empty cart dictionary

    # For POST requests (order submission), get cart data from form
    if request.method == 'POST':
        cart_data_json = request.form.get('cart_data')
        if cart_data_json:
            try:
                cart_items = json.loads(cart_data_json)
            except json.JSONDecodeError:
                flash('Error processing cart data.', 'danger')
                return redirect(url_for('cart')) # Redirect if cart data is invalid

    # Calculate totals (only needed for POST submission logic)
    subtotal, tax, shipping_cost, total = calculate_cart_totals(cart_items)

    conn = get_db_connection()
    if conn is None:
        flash('Database connection error.', 'danger')
        # For GET request, render template with error. For POST, redirect.
        if request.method == 'POST':
             return redirect(url_for('checkout'))
        else:
             return render_template(
                'checkout.html',
                cart_items={}, # Empty cart for display on error
                subtotal=0, tax_rate=TAX_RATE, tax=0, shipping_cost=SHIPPING_COST, total=0, cart_item_count=0,
                user_address="Error fetching address"
            )

    cur = conn.cursor()
    user_address = "Address not found" # Default

    try:
        # Fetch user's address for display on checkout page
        cur.execute("SELECT address FROM users WHERE id = %s", (user_id,))
        user_row = cur.fetchone()
        if user_row:
            user_address = user_row[0]

    except Exception as e:
        print(f"Error fetching user address for checkout: {e}")
        flash('An error occurred while fetching your address.', 'danger')

    finally:
        # Close connection after fetching address for GET request
        if request.method == 'GET':
            if cur:
                cur.close()
            if conn:
                conn.close()

    if request.method == 'POST':
        # --- Process Order Submission ---
        # Database connection is already open from fetching address for POST method
        # Ensure cart is not empty before processing order
        if not cart_items:
             flash('Your cart is empty. Please add items before checking out.', 'warning')
             # Close connection before redirecting
             if cur: cur.close()
             if conn: conn.close()
             return redirect(url_for('cart')) # Redirect back to cart

        order_id = None

        try:
            # Prepare order details for database storage (JSONB format)
            # We'll store a list of dictionaries with product_id, name, price, and quantity
            order_details_list = []
            for product_id_str, item in cart_items.items():
                 order_details_list.append({
                    'product_id': int(product_id_str),
                    'name': item.get('name', 'Unknown Product'), # Use .get with default
                    'price': float(item.get('price', 0)), # Ensure float
                    'quantity': int(item.get('quantity', 0)) # Ensure int
                 })

            # Insert the order into the orders table
            cur.execute(
                "INSERT INTO orders (user_id, order_details, total_price) VALUES (%s, %s, %s) RETURNING order_id",
                (user_id, json.dumps(order_details_list), total) # Use json.dumps for JSONB
            )
            order_id = cur.fetchone()[0] # Get the generated order_id
            conn.commit() # Commit the order transaction

            # Cart is in local storage, client-side JS will clear it after redirect

            flash('Your order has been placed!', 'success')
            # Close connection before redirecting
            if cur: cur.close()
            if conn: conn.close()
            return redirect(url_for('order_complete', order_id=order_id)) # Redirect to order complete page

        except Exception as e:
            conn.rollback() # Rollback the transaction on error
            print(f"Error during order submission: {e}")
            flash('An error occurred while submitting your order. Please try again.', 'danger')
            # Close connection before redirecting
            if cur: cur.close()
            if conn: conn.close()
            return redirect(url_for('checkout')) # Redirect back to checkout on error

        # Finally block for POST request is handled within the try/except

    # If it's a GET request, render the checkout page
    # Note: Cart items and totals will be rendered client-side by checkout.html JS
    return render_template(
        'checkout.html',
        user_address=user_address, # Pass user address for display
        # Pass constants for client-side calculation in checkout.html JS
        tax_rate=TAX_RATE,
        shipping_cost=SHIPPING_COST
    )

@app.route('/order_complete/<int:order_id>') # Use <int:order_id> to specify integer type
def order_complete(order_id):
    """Displays the order complete confirmation page."""
    # You might want to fetch order details from the database here
    # to display more information on the confirmation page,
    # but for now, we'll just pass the order_id.
    return render_template('order_complete.html', order_id=order_id)

# --- Running the App ---
if __name__ == '__main__':
    app.run(debug=True) # debug=True is useful during development
