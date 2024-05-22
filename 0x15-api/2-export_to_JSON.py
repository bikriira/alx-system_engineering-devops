#!/usr/bin/python3
"""
Using what done in file 0-gather_data_from_an_API.py,
extend your Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user = requests.get(user_api_url)
    user_data = []

    if todo_list.status_code == 200 and user.status_code == 200:
        for task in todo_list.json():
            if task["userId"] == int(argv[1]):
                user_data.append(
                    {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": user.json()["username"]
                    }
                )
        to_be_parse = {argv[1]:  user_data}
        with open(f"{argv[1]}.json", "w") as file:
            formated_json = json.dump(to_be_parse, file)
