from flask import Flask

app = Flask(__name__)

# @app.route("/")
def index():
    return '<h3>Hello world</h3>'

app.add_url_rule("/", view_func=index)