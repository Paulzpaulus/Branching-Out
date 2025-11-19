import json


def load_users():
    """Load user data safely."""
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error: users.json is missing or invalid.")
        return []


def filter_users_by_name(name):
    name = name.strip().lower()
    users = load_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower().strip()]

    if not filtered_users:
        print("no users found with that name")
        return

    for user in filtered_users:
        print(user)


def filter_user_by_age(age):
    try:
        age = int(age)
    except ValueError as e:
        print(f"{e}. Age must be a number")
        return
    users = load_users()
    filtered_by_age = [user for user in users if user.get("age") == age]
    if not filtered_by_age:
        print("no user with that age")
        return
    for user in filtered_by_age:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (age/name): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age = input("enter age:").strip()
        filter_user_by_age(age)
    else:
        print("Filtering by that option is not yet supported.")

