from functools import wraps


def login_with_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("You are not an admin")
        else:
            func(user_role)

    return wrapper


@login_with_admin
def show_dashboard(role):
    print(f"Welcome to the dashboard {role}")


show_dashboard("user_admin")


def access_hotel_admin_room(func):
    @wraps(func)
    def wrapper(admin_room_keys):
        if admin_room_keys != "admin":
            print("You are not an admin")
        else:
            func(admin_room_keys)

    return wrapper


@access_hotel_admin_room
def show_admin_room_keys(keys):
    print(f"Welcome to the admin room {keys}")


show_admin_room_keys("admin")
