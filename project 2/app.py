from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def index():
    return render_template(index.html)

# set the app to run if you execute the file directly (not when it's imported)
if __name__ == '__main__':
    app.run(debug=True)
