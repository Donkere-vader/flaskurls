from flask import Blueprint

user_stats = Blueprint('user_stats', __name__, template_folder='templates')

@user_stats.route('/')
def hello_world():
    return 'Hello World!'
