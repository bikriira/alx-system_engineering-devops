#!/usr/bin/python3
"""
script that, using jsonplaceholder API, for a given employee ID,
returns information about his/her Todo list progress
"""
if __name__ == "__main__":
    from sys import argv
    import requests

    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user = requests.get(user_api_url)
    task_count = 0
    completed_tasks = []

    if todo_list.status_code == 200 and user.status_code == 200:
        for task in todo_list.json():
            if task["userId"] == int(argv[1]):
                if task["completed"]:
                    completed_tasks.append(task["title"])
                task_count += 1

        print(f"Employee {user.json()['name']} is done with",
              f"tasks({len(completed_tasks)}/{task_count})")
        for task in completed_tasks:
            print(f"     {task}")
