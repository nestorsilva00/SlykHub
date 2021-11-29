from flask import Flask, render_template, request, redirect, url_for, flash
import logic as App_logic
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def users_new_table():
    assets = None
    return render_template('table.html', assets=assets)

@app.route('/update_users', methods=['GET', 'POST'])
def update_users_table():
    apikey = request.form['apikey']
    data = App_logic.get_users_data(apikey)
    assets = App_logic.get_wallets_balance(apikey)
    return render_template('table.html', user_data=data, assets=assets)
