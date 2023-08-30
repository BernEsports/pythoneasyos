import os

greetings_message = "Hello its terminal based fun made python OS\n" \
                    "============================== version 0.1 =="

list_of_users = {"Nikita": "9578"}


def creating_new_user():

    """Creating new user and adding them to list of users dictionary"""

    # print("Oops, your account not found, do you want to create new? Y/N")
    creating_new_account = input(">> ")
    if creating_new_account.lower() == "y":
        print("Enter your name")
        new_account_name = input(">> ")
        if not new_account_name:
            print("Incorrect name!")
        else:
            print("Enter your password")
            new_account_pass = input(">> ")
            if not new_account_pass or len(new_account_pass) < 4:
                print("Incorrect password, min lenght of password should be 4!")
            else:
                list_of_users[new_account_name] = new_account_pass
                print("Succesfully created new account with name\n"
                      f"'{new_account_name}' and password '{new_account_pass}'")
    else:
        print("Stopping system...")


def authorization():

    """Authorization as first systeem screen as it opens"""

    print("Enter your login")
    user_login_input = input(">> ")
    if user_login_input in list_of_users:
        print("Enter your password")
        user_password_input = input(">> ")
        if user_password_input == list_of_users[user_login_input]:
            print(greetings_message)
            return True
        else:
            print("Incorrect password")
    else:
        print("Oops, your account not found, do you want to create new? Y/N")
        creating_new_user()

authorization()
