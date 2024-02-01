from google.cloud import bigquery
from user_crud_operations import *
from user_operations import *
from google.oauth2 import service_account


def display_user_menu():
    print("+-------------------------------------+")
    print("| 1. View data of inflation           |")
    print("| 2. View Country data                |")
    print("| 3. Analysis Operations on Inflation |")
    print("| 4. Analysis on Country Data         |")
    print("| 5. Exit                             |")
    print("+-------------------------------------+")



def handle_menu_user_choice(choice,client):
    if choice=='1':
        view_inflation_data(client)
    elif choice=='2':
        view_country_data(client)
    elif choice=='3':
        analysis_operations_inflation(client,input("Enter country code: ").upper())
    elif choice=='4':
        codes=get_multiple_inputs()
        analysis_country_data(client,codes)
    else:
        print("Invalid Choice, Try again!")