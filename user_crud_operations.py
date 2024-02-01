from google.cloud import bigquery
from tabulate import tabulate
from google.oauth2 import service_account


def connect_to_bigquery():
    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    project_id = 'theta-cell-406519'
    return bigquery.Client(credentials= credentials,project=project_id)

def view_inflation_data(client):
    query = "SELECT * FROM `bharath_inflation_dataset.inflation` LIMIT 10"

    result = client.query(query).to_dataframe()

    if result.empty:
        print("No data found.")
        return

    print(tabulate(result, headers="keys", tablefmt="pretty"))

def view_country_data(client):
    query = "SELECT * FROM `bharath_inflation_dataset.countries`"

    result = client.query(query).to_dataframe()

    if result.empty:
        print("No data found.")
        return

    print(tabulate(result, headers="keys", tablefmt="pretty"))

def main():
    # Connect to BigQuery
    client = connect_to_bigquery()

    # View inflation data
    print("Inflation Data:")
    view_inflation_data(client)

    # View country data
    print("\nCountry Data:")
    view_country_data(client)

if __name__ == "__main__":
    main()
