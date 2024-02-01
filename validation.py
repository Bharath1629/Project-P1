# validation.py

def validate_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Please enter a non-empty value.")

def validate_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")

def validate_numeric_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# from google.cloud import bigquery
# from google.oauth2 import service_account
#
# credentials = service_account.Credentials.from_service_account_file('credentials.json')
# project_id = 'theta-cell-406519'
# client = bigquery.Client(credentials= credentials,project=project_id)
#
#
# # Specify your project ID and dataset ID
# project_id = 'theta-cell-406519'
# dataset_id = 'bharath_inflation_dataset'
# table_id = 'countries'
# dataset_ref = client.dataset(dataset_id, project=project_id)
# table_ref = dataset_ref.table(table_id)
#
# # Try to get the table
# try:
#     table = client.get_table(table_ref)
# except Exception as e:
#     print(f'Error: {e}')
#     exit()
#
# # Fetch the table rows
# rows = client.list_rows(table)
#
# # Print the table data
# print(f"Content of the '{table_id}' table:")
# for row in rows:
#     print(row)
