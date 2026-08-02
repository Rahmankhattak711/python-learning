USER_DATABASE = {"username": "rahmanullah", "password": "123456"}


def login(username, password):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == USER_DATABASE["username"] and password == USER_DATABASE["password"]:
        return "Login successful"
    else:
        return "Login failed"


def create_account():
    username = input("Enter your username: ").strip()
    if username in USER_DATABASE:
        print("Username already exists")
        return None

    password = input("Enter your password: ").strip()
    USER_DATABASE[username] = password

    print("Account created successfully")
    return USER_DATABASE


def main():
    choice = input("Do you want to (1) login or (2) create an account? ")

    if choice == "1":
        result = login(USER_DATABASE["username"], USER_DATABASE["password"])
        print(result)
    elif choice == "2":
        create_account()
    else:
        print("Invalid choice. Please select 1 or 2.")


main()
