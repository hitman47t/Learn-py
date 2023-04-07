from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

from dataclasses import dataclass

todo_app = Blueprint("product_app", __name__)

@dataclass
class Task:
    name: str
    isDone: bool
    # priority: int

    def update_status(self, isDone:bool):
        self.isDone = isDone

TASKS = {
    1: Task('Clean a home', False),
    2: Task('Learn Python', False),
    3: Task('Buy purchase', True)
}
SEQ = len(TASKS)

@todo_app.route("/", methods=['GET', 'POST'])
def product_list():
    global SEQ
    if request.method == 'POST':
        print(request.form['data'])
        SEQ += 1
        req_data = request.form['data']
        TASKS[SEQ] = Task(req_data, False)
    return render_template("todolist/index.html", tasks=TASKS)


@todo_app.route("/<int:task_id>/", methods=['GET','DELETE', 'POST'])
def task_detail(task_id: int):
    try:
        task_name = TASKS[task_id]
    except KeyError:
        raise BadRequest(f"Invalid product id #{task_id}")

    if request.method == 'DELETE':
        TASKS.pop(task_id)
        return jsonify(ok=True)

    if request.method == 'POST':
        isDone = True if request.form['isDone'] == '1' else False
        print('isDone=',isDone)
        TASKS[task_id].update_status(isDone)
        print(TASKS[task_id])

    return TASKS[task_id].name