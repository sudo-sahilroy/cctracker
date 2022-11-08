from flask import Blueprint

auth = Blueprint('auth',__name__)


@auth.route('/register')
def register():
    return "<p>Register</p>"