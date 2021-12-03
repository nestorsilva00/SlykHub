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
    try:
        data = App_logic.get_users_data(apikey)
        assets = App_logic.get_wallets_balance(apikey)
    except Exception as e:
        print(e)
    return render_template('table.html', user_data=data, assets=assets)

@app.errorhandler(500)
def page_not_found(e):
    error_type = "500 Internal Server Error"
    error_message = "Por favor, compruebe que su API Key sea correcta"
    return render_template('error.html', error_message=error_message, error_type=error_type), 500

@app.errorhandler(404)
def page_not_found(e):
    error_type = "404 Not Found"
    error_message = "La URL solicitada no existe"
    return render_template('error.html', error_message=error_message, error_type=error_type), 500

@app.errorhandler(400)
def page_not_found(e):
    error_type = "400 Bad Request"
    error_message = "Debe introducir su API Key"
    return render_template('error.html', error_message=error_message, error_type=error_type), 500