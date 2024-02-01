# from google.cloud import bigquery
# import pandas as pd
#
# # Set up credentials
# client = bigquery.Client.from_service_account_json('credentials.json')
#
# # Specify your project ID and dataset ID
# project_id = 'theta-cell-406519'
# dataset_id = 'bharath_inflation_dataset'
#
# # Construct a reference to the dataset
# dataset_ref = client.dataset(dataset_id, project=project_id)
#
# # Check if the dataset already exists
# try:
#     dataset = client.get_dataset(dataset_ref)
#     print(f'Dataset {dataset_id} already exists.')
# except Exception as e:
#     # If the dataset doesn't exist, create it
#     dataset = bigquery.Dataset(dataset_ref)
#     dataset.description = 'Dataset for inflation, countries, and users'
#     dataset.location = 'US'  # Specify the location, e.g., US, EU
#     created_dataset = client.create_dataset(dataset)
#     print(f'Dataset {created_dataset.dataset_id} created.')
#
# # Function to load data into BigQuery table
# # def load_data_into_table(csv_path, table_id):
# #     table_ref = dataset_ref.table(table_id)
# #     dataframe = pd.read_csv(csv_path)
# #
# #     # Remove the explicit schema definition for auto-detection
# #     job_config = bigquery.LoadJobConfig()
# #     job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
# #     job.result()
# #     print(f'Data loaded into {project_id}:{dataset_id}.{table_id}')
# # Set up credentials
# client = bigquery.Client.from_service_account_json('credentials.json')
#
# # Specify your project ID and dataset ID
# project_id = 'theta-cell-406519'
# dataset_id = 'bharath_inflation_dataset'
# table_id = 'users'
#
# # Construct a reference to the table
# table_ref = client.dataset(dataset_id, project=project_id).table(table_id)
#
# # Get the table schema
# table = client.get_table(table_ref)
# schema = table.schema
#
# # Print the schema
# for field in schema:
#     print(f"Column: {field.name}, Type: {field.field_type}")
#
# def load_data_into_table(csv_path, table_id, column_mapping=None):
#     table_ref = dataset_ref.table(table_id)
#     dataframe = pd.read_csv(csv_path)
#
#     # Rename columns if column_mapping is provided
#     if column_mapping:
#         dataframe.rename(columns=column_mapping, inplace=True)
#
#     # Remove the explicit schema definition for auto-detection
#     job_config = bigquery.LoadJobConfig()
#     job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
#     job.result()
#     print(f'Data loaded into {project_id}:{dataset_id}.{table_id}')
#
# # Define column mapping if needed
# # Example: {'old_column_name': 'new_column_name'}
# # column_mapping_users = {'username ': 'username', 'password': 'password', 'role': 'role'}
#
# # Load data into tables with optional column renaming
# # load_data_into_table('C:/Users/91630/Desktop/Revature/Project-P0/users.csv', 'users', column_mapping_users)
#
#
# # Load data into tables
# # load_data_into_table('C:/Users/91630/Desktop/Revature/Project-P0/inflation.csv', 'inflation')
# # load_data_into_table('C:/Users/91630/Desktop/Revature/Project-P0/Countries.csv', 'countries')
# # load_data_into_table('C:/Users/91630/Desktop/Revature/Project-P0/users.csv', 'users')
#
# # Fetch and print the data from the 'users' table
# table_id = 'users'
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
