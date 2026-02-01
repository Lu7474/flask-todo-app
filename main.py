from flask import Flask, render_template, request, redirect

from todo import get_tasks, add_task, del_task, change_task

app = Flask(__name__)


@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task_fr():
    task = request.form.get("task")
    add_task(task)
    return redirect("/")


@app.route("/delete/<int:id>")
def del_task_fr(id):
    del_task(id)
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task_fr(id):
    if request.method == "POST":
        title_n = request.form.get("task")
        change_task(id, title_n)
        return redirect("/")

    tasks = get_tasks()
    task = None

    for t in tasks:
        if t["id"] == id:
            task = t
            break
    return render_template("edit_task.html", task=task)

app.run(debug=True)