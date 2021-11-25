from flask import Flask, render_template, request, redirect, url_for, flash
from api import get_data_from_api
app = Flask(__name__)

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/update_apikey', methods=['GET', 'POST'])
def update_users():
    apikey = request.form['apikey']
    data = get_data_from_api("https://api.slyk.io/orders", apikey)
    return render_template('users.html', orders=data['data'])