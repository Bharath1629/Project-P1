from google.cloud import bigquery
from google.oauth2 import service_account


def connect_to_bigquery():
    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    project_id = 'theta-cell-406519'
    return bigquery.Client(credentials= credentials,project=project_id)

def display_login():
    print("1. Admin user")
    print("2. Normal user")
    print("3. New user")

def new_user_registration(client, username, password):
    try:
        # Assuming you have a dataset named 'inflation' and a table named 'users' in your BigQuery project
        query = f"""
            INSERT INTO `theta-cell-406519.bharath_inflation_dataset.users` (username, password, role)
            VALUES ('{username}', '{password}', 'user')
        """

        result = client.query(query)
        print(f"Hi '{username}', Thanks for registration!")
        print("Welcome to the Inflation project")
        print("Please enter your credentials below")

    except Exception as e:
        print(f"Error: {e}")

def main():
    # Connect to BigQuery
    client = connect_to_bigquery()

if __name__ == "__main__":
    main()
