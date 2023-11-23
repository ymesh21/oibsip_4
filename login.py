# login.py
import getpass
import hashlib

def login(user_database, admin_page):
    print("Login:")
    username = input("Enter your username: ")

    # Check if the username exists
    if username not in user_database:
        print("Username not found. Please register first.")
        return

    password = getpass.getpass("Enter your password: ")

    # Retrieve the stored salt and hashed password
    salt, hashed_password = user_database[username]

    try:
        # Hash the entered password with the stored salt
        entered_password_hashed = hashlib.sha256((password + salt).encode()).hexdigest()

        # Check if the entered password matches the stored password
        if entered_password_hashed == hashed_password:
            print("Login successful. Welcome, {}!".format(username))
            admin_page(username)
        else:
            raise ValueError("Incorrect password. Please try again.")
    except Exception as e:
        print(f"An error occurred during login: {e}")
