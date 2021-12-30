from flask import Blueprint, render_template, request
import slykhub.user.logic as app_logic


users = Blueprint('users', __name__)

@users.route('/', methods=['GET', 'POST'])
def users_new_table():
    assets = None
    current_data = None
    current_balance = None
    
    return render_template('users_balance_table.html', assets=assets, current_data=current_data, current_balance=current_balance)

@users.route('/update_users', methods=['GET', 'POST'])
def update_users_table():
    apikey = request.form['apikey']
    try:
        data = app_logic.get_users_balance_data(apikey)
        assets = app_logic.get_wallets_balance(apikey)
        current_total_balance = app_logic.get_current_total_balance_for_asset(data, assets)
    except Exception as e:
        print(e)
    return render_template('users_balance_table.html', user_data=data, assets=assets, current_balance=current_total_balance)