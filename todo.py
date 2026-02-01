import json
import os

file_name = "todo_list.json"

if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4, ensure_ascii=False)

def get_tasks():
    with open(file_name, encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def add_task(task):
    tasks = get_tasks()
    id = max(t["id"] for t in tasks) + 1 if tasks else 1
    tasks.append({"id": id, "title": task})
    save_tasks(tasks)


def change_task(id, title_n):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == id:
            task["title"] = title_n
            save_tasks(tasks)
            return
    return "Error. Задача не найдена."


def del_task(id):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break
    save_tasks(tasks)
