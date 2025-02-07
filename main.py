from flask import render_template

from app import create_app

app = create_app()

print("Appp creada")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def update_page():
    return render_template('login.html')