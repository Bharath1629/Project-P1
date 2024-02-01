from google.cloud import bigquery
from validation import *
from tabulate import tabulate
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json')

project_id = 'theta-cell-406519'
client = bigquery.Client(credentials= credentials,project=project_id)

def view_inflation_data(client):
    query = "SELECT * FROM `theta-cell-406519.bharath_inflation_dataset.inflation`  ORDER BY record_id"
    result = client.query(query).to_dataframe()

    if result.empty:
        print("No data found.")
        return

    print(tabulate(result, headers="keys", tablefmt="pretty"))

def create_inflation_data(client):
    query = f""" SELECT count(*) as row_count FROM `{project_id}.bharath_inflation_dataset.inflation`;"""
    query_job = client.query(query)
    df = query_job.to_dataframe()
    record_id = df['row_count'][0]
    record_id+=1
    country_code = validate_non_empty_input("Enter country code: ").upper()
    year = validate_numeric_int_input("Enter year: ")
    energy_price = validate_numeric_input("Enter Energy Consumer Price: ")
    food_price = validate_numeric_input("Enter Food Consumer Price: ")
    headline_price = validate_numeric_input("Enter Headline Consumer Price: ")
    core_price = validate_numeric_input("Enter Official Core Consumer Price: ")
    producer_price = validate_numeric_input("Enter Producer Price Inflation: ")

    query = f"""
        INSERT INTO `theta-cell-406519.bharath_inflation_dataset.inflation` 
        (record_id, country_code, year, headline_consumer_price, energy_consumer_price, food_consumer_price, official_core_consumer_price, producer_price_inflation) 
        VALUES ({record_id}, '{country_code}', {year}, {headline_price}, {energy_price}, {food_price}, {core_price}, {producer_price})
    """

    result=client.query(query)
    for row in result:
        print(row)

def update_inflation_data(client):
    country_code = validate_non_empty_input("Enter country code: ").upper()
    year = validate_numeric_input("Enter year: ")
    energy_consumer_price = validate_numeric_input("Enter Energy Consumer Price: ")
    food_consumer_price = validate_numeric_input("Enter Food Consumer Price: ")
    headline_consumer_price = validate_numeric_input("Enter Headline Consumer Price: ")
    official_core_consumer_price = validate_numeric_input("Enter Official Core Consumer Price: ")
    producer_price_inflation = validate_numeric_input("Enter Producer Price Inflation: ")

    check_query = f"""
        SELECT COUNT(*) 
        FROM `theta-cell-406519.bharath_inflation_dataset.inflation` 
        WHERE country_code = '{country_code}' AND year = {year}
    """
    check_result = client.query(check_query).to_dataframe()

    if check_result.iloc[0, 0] == 0:
        print(f"Inflation data not found for country code {country_code} and year {year}. Please provide correct data.")
        return

    update_query = f"""
        UPDATE `theta-cell-406519.bharath_inflation_dataset.inflation`
        SET 
            energy_consumer_price = {energy_consumer_price},
            food_consumer_price = {food_consumer_price},
            headline_consumer_price = {headline_consumer_price},
            official_core_consumer_price = {official_core_consumer_price},
            producer_price_inflation = {producer_price_inflation}
        WHERE 
            country_code = '{country_code}' AND 
            year = {year}
    """

    client.query(update_query)
    print("Inflation data updated successfully.")

from google.cloud import bigquery

def delete_inflation_data(client, country_code, year):
    try:
        check_query = f"""
            SELECT COUNT(*)
            FROM `theta-cell-406519.bharath_inflation_dataset.inflation`
            WHERE country_code = '{country_code}' AND year = {year}
        """

        check_result = client.query(check_query).result()
        check_count = next(check_result)[0]

        if check_count == 0:
            print(f"Inflation data not found for country code {country_code} and year {year}. Please provide correct data.")
            return

        delete_query = f"""
            DELETE FROM `theta-cell-406519.bharath_inflation_dataset.inflation`
            WHERE country_code = '{country_code}' AND year = {year}
        """

        client.query(delete_query).result()

        print("Inflation data deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
