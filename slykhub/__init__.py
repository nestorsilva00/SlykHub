from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    from slykhub.user.routes import users
    app.register_blueprint(users)


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

    return app