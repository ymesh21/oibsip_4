# registration.py
import getpass
import hashlib

def register(user_database):
    print("Register:")
    username = input("Enter your username: ")

    # Check if the username already exists
    if username in user_database:
        print("Username already exists. Please choose a different username.")
        return

    password = getpass.getpass("Enter your password: ")

    # Generate a random salt
    salt = hashlib.sha256(username.encode()).hexdigest()[:10]

    try:
        # Hash the password with the salt
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

        user_database[username] = (salt, hashed_password)
        print("Registration successful.")
    except Exception as e:
        print(f"An error occurred during registration: {e}")
