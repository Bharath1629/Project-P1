from google.cloud import bigquery
from admin_crud_operations import *
from admin_operations import authenticate_user
from menu_for_admin import display_menu, handle_menu_choice
from menu_for_users import *
from login_page import *
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json')

project_id = 'theta-cell-406519'
client = bigquery.Client(credentials= credentials,project=project_id)


def main():
    try:
        project_id = 'theta-cell-406519'
        dataset_id = 'bharath_inflation_dataset'

        # No need to set credentials explicitly here
        client = bigquery.Client(credentials= credentials,project=project_id)

        while True:
            display_login()
            choice = input("Enter your choice: ")

            if choice == '1':
                # Authentication and admin menu for BigQuery
                user = authenticate_user(client, input("Enter username: "), input("Enter password: "), 'admin')
                if not user:
                    print("Enter valid credentials!")
                    continue

                while True:
                    display_menu()
                    choice = input("Enter your choice: ")

                    if choice == '9':
                        print("Thanks for your time! See you again!")
                        break

                    handle_menu_choice(choice, client)
                break

            elif choice == '2':
                # Authentication and user menu for BigQuery
                user = authenticate_user(client, input("Enter username: "), input("Enter password: "), 'user')
                if not user:
                    print("Enter valid credentials!")
                    continue

                while True:
                    display_user_menu()
                    choice = input("Enter your choice: ")

                    if choice == '5':
                        print("Thanks for your time!")
                        break

                    handle_menu_user_choice(choice, client)
                break

            elif choice == '3':
                # User registration and user menu for BigQuery
                new_user_registration(client, input("Enter username: "), input("Enter password: "))
                user = authenticate_user(client, input("Enter username: "), input("Enter password: "), 'user')
                if not user:
                    print("Enter valid credentials!")
                    continue

                while True:
                    display_user_menu()
                    choice = input("Enter your choice: ")

                    if choice == '5':
                        print("Thanks for your time!")
                        break

                    handle_menu_user_choice(choice, client)
                break

            else:
                print("Please, Enter a valid number!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


# import streamlit as st
# from google.cloud import bigquery
# from admin_crud_operations import *
# from admin_operations import authenticate_user
# from menu_for_admin import display_menu, handle_menu_choice
# from menu_for_users import *
# from login_page import *
# from google.oauth2 import service_account
#
# credentials = service_account.Credentials.from_service_account_file('credentials.json')
# project_id = 'theta-cell-406519'
# client = bigquery.Client(credentials=credentials, project=project_id)
#
# def main():
#     st.title("Your Streamlit App Title")
#
#     try:
#         project_id = 'theta-cell-406519'
#         dataset_id = 'bharath_inflation_dataset'
#
#         # No need to set credentials explicitly here
#         client = bigquery.Client(credentials=credentials, project=project_id)
#
#         display_login()
#         choice = st.text_input("Enter your choice:")
#
#         if choice == '1':
#             # Authentication and admin menu for BigQuery
#             user = authenticate_user(client, st.text_input("Enter username:"), st.text_input("Enter password:"), 'admin')
#             if not user:
#                 st.warning("Enter valid credentials!")
#                 return
#
#             while True:
#                 display_menu()
#                 choice = st.text_input("Enter your choice:")
#
#                 if choice == '9':
#                     st.write("Thanks for your time! See you again!")
#                     break
#
#                 handle_menu_choice(choice, client)
#             return
#
#         elif choice == '2':
#             # Authentication and user menu for BigQuery
#             user = authenticate_user(client, st.text_input("Enter username:"), st.text_input("Enter password:"), 'user')
#             if not user:
#                 st.warning("Enter valid credentials!")
#                 return
#
#             while True:
#                 display_user_menu()
#                 choice = st.text_input("Enter your choice:")
#
#                 if choice == '5':
#                     st.write("Thanks for your time!")
#                     break
#
#                 handle_menu_user_choice(choice, client)
#             return
#
#         elif choice == '3':
#             # User registration and user menu for BigQuery
#             new_user_registration(client, st.text_input("Enter username:"), st.text_input("Enter password:"))
#             user = authenticate_user(client, st.text_input("Enter username:"), st.text_input("Enter password:"), 'user')
#             if not user:
#                 st.warning("Enter valid credentials!")
#                 return
#
#             while True:
#                 display_user_menu()
#                 choice = st.text_input("Enter your choice:")
#
#                 if choice == '5':
#                     st.write("Thanks for your time!")
#                     break
#
#                 handle_menu_user_choice(choice, client)
#             return
#
#         else:
#             st.warning("Please enter a valid number!")
#
#     except Exception as e:
#         st.error(f"Error: {e}")
#
# if __name__ == "__main__":
#     main()
