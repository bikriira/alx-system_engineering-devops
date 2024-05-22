#!/usr/bin/python3
"""
Using what done in file 0-gather_data_from_an_API.py,
extend your Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import json
    import requests

    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_api_url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(user_api_url)
    all_users_data = {}

    if todo_list.status_code == 200 and users.status_code == 200:
        for user in users.json():
            user_data = []
            for task in todo_list.json():
                if task["userId"] == user["id"]:
                    user_data.append(
                        {
                            "task": task["title"],
                            "completed": task["completed"],
                            "username": user["username"]
                        }
                    )
            all_users_data[user["id"]] = user_data

        with open(f"todo_all_employees.json", "w") as file:
            formated_json = json.dump(all_users_data, file)
