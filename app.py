from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks as a list of dictionaries
tasks = []

@app.route("/")
def home():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["done"])
    progress = (completed_tasks / total_tasks * 100) if total_tasks else 0
    return render_template("index.html", tasks=tasks, enumerate=enumerate, progress=int(progress))

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    priority = request.form.get("priority", "Medium")
    if task:
        tasks.append({"task": task, "done": False, "priority": priority})
    return redirect(url_for("home"))

@app.route("/complete/<int:task_index>")
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
    return redirect(url_for("home"))

@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
