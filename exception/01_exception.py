def logged_in_user(is_logged):
    try:
        if is_logged != True:
            print("You are not logged in")
        else:
            {print("You are logged in")}
    except Exception as e:
        print(e)
    finally:
        print("This is always executed")


logged_in_user(False)



