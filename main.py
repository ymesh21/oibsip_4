# main.py
from registration import register
from login import login
from admin import admin_page

def display_menu():
    print("\n=== Authentication System ===")
    print("1. Register\n2. Login\n3. Access Admin Page\n4. Exit")

def main():
    user_database = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            register(user_database)
        elif choice == "2":
            login(user_database, admin_page)
        elif choice == "3":
            print("Please login first.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

