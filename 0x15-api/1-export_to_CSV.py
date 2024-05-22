#!/usr/bin/python3
"""
Using what done in file 0-gather_data_from_an_API.py,
extend your Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user = requests.get(user_api_url)
    records = []

    if todo_list.status_code == 200 and user.status_code == 200:
        for task in todo_list.json():
            if task["userId"] == int(argv[1]):
                records.append(
                    [
                        task["userId"],
                        user.json()["name"],
                        task["completed"],
                        task["title"]
                    ]
                )

        with open("USER_ID.csv", "w") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for record in records:
                writer.writerow(record)
