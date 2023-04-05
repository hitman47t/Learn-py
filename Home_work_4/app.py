
from flask import Flask, request, render_template

from views import todo_app

app = Flask(__name__)
app.register_blueprint(todo_app, url_prefix="/todolist")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", name='MAIN PAGE')