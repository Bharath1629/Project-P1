from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json')
project_id = 'theta-cell-406519'
client = bigquery.Client(credentials= credentials,project=project_id)

def authenticate_user(client, username, password, role):
    query = f"""
        SELECT *
        FROM `theta-cell-406519.bharath_inflation_dataset.users`
        WHERE username = '{username}' AND password = '{password}' AND role = '{role}'
    """

    try:
        result = client.query(query).to_dataframe()

        return result.iloc[0].to_dict() if not result.empty else None
    except Exception as e:
        print(f"Error executing query: {e}")
        return None


def create_user_by_admin(client, username, password, role):
    try:
        query = f"""
            INSERT INTO `theta-cell-406519.bharath_inflation_dataset.users` (username, password, role)
            VALUES ('{username}', '{password}', '{role}')
        """

        client.query(query)

        print(f"User '{username}' created successfully by admin.")

    except Exception as e:
        print(f"Error: {e}")

def update_user_by_admin(client, username, new_password):
    try:
        query = f"""
            UPDATE `theta-cell-406519.bharath_inflation_dataset.users`
            SET password = '{new_password}'
            WHERE username = '{username}'
        """

        client.query(query)

        print(f"Password updated successfully for user with ID {username} by admin.")

    except Exception as e:
        print(f"Error: {e}")

def delete_user_by_admin(client, username):
    try:
        query = f"""
            DELETE FROM `theta-cell-406519.bharath_inflation_dataset.users`
            WHERE username = '{username}'
        """

        client.query(query)

        print(f"User with username {username} deleted successfully by admin.")

    except Exception as e:
        print(f"Error: {e}")

def view_users(client):
    try:
        query = "SELECT * FROM `theta-cell-406519.bharath_inflation_dataset.users`"
        result = client.query(query).to_dataframe()

        if not result.empty:
            print("User Data:")
            for _, row in result.iterrows():
                print(f"Role: {row['role']}, Username: {row['username']}")
        else:
            print("No users found.")

    except Exception as e:
        print(f"Error: {e}")
