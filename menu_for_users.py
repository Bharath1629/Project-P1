from google.cloud import bigquery
from user_crud_operations import *
from user_operations import *
from google.oauth2 import service_account
from prediction import *
from validation import *

def display_user_menu():
    print("+-------------------------------------+")
    print("| 1. View data of inflation           |")
    print("| 2. View Country data                |")
    print("| 3. Analysis Operations on Inflation |")
    print("| 4. Analysis on Country Data         |")
    print("| 5. Predict the inflation rates      |")
    print("| 6. Exit                             |")
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
    elif choice=='5':
        user_country = validate_non_empty_input("Enter the country code (e.g., 'USA'): ").upper()
        user_year = int(input("Enter the year for prediction: "))
        inflation_rate_types()
        choice = int(input("Enter your choice: "))
        while True:
            if choice == 1:
                inflation_type = 'headline_consumer_price'
                break
            elif choice == 2:
                inflation_type = 'energy_consumer_price'
                break
            elif choice == 3:
                inflation_type = 'food_consumer_price'
                break
            elif choice == 4:
                inflation_type = 'official_core_consumer_price'
                break
            elif choice == 5:
                inflation_type = 'producer_price_inflation'
                break
            else:
                print("Enter valid number!")
        country_data = get_inflation_data_from_bigquery(client, user_country, inflation_type)
        predicted_inflation = predict_inflation_for_year_and_country(country_data,user_country, user_year, inflation_type)
        display_result(user_country,user_year,predicted_inflation,country_data,inflation_type)
    else:
        print("Invalid Choice, Try again!")