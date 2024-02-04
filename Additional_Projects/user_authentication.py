user_credentials = {}


def register():
    username = input("Please enter your new username: ")
    password = input("Please enter your new password: ")
    if username not in user_credentials:
        user_credentials[username] = password


def login():
    username = input("Please enter your username: ")
    if username in user_credentials:
        password = input("Please enter your password: ")
        if password == user_credentials[username]:
            pass
        else:
            print("ERROR! Wrong password!")
    else:
        print("ERROR! Wrong username!")
