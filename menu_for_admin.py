# menu_for_admin.py
from google.cloud import bigquery
from admin_crud_operations import *
from admin_operations import *
from google.oauth2 import service_account


def display_menu():
    print("+--------------------------+")
    print("| 1. View Inflation Data   |")
    print("| 2. Create Inflation Data |")
    print("| 3. Update Inflation Data |")
    print("| 4. Delete Inflation Data |")
    print("| 5. Create new user       |")
    print("| 6. Update user details   |")
    print("| 7. Delete user           |")
    print("| 8. View users data       |")
    print("| 9. Exit                  |")
    print("+--------------------------+")

def handle_menu_choice(choice, client):
    if choice == '1':
        view_inflation_data(client)
    elif choice == '2':
        create_inflation_data(client)
    elif choice == '3':
        update_inflation_data(client)#, input("Enter country to update: "), input("Enter year to update: "), input("Enter new Energy Consumer Price: "), input("Enter new Food Consumer Price: "), input("Enter new Headline Consumer Price: "), input("Enter new Official Core Consumer Price: "), input("Enter new Producer Price Inflation: "))
    elif choice == '4':
        delete_inflation_data(client, input("Enter country to delete: "), input("Enter year to delete: "))
    elif choice == '9':
        print("Exiting. Goodbye!")
    elif choice=='5':
        create_user_by_admin(client,input("Enter the name of new user: "),input("Enter password for user: "),input("Enter user role: "))
    elif choice=='6':
        update_user_by_admin(client,input("Enter username: "),input("Enter new password: "))
    elif choice=='7':
        delete_user_by_admin(client,input("Enter username: "))
    elif choice=='8':
        view_users(client)
    else:
        print("Invalid choice. Try again.")
