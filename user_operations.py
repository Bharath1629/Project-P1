from google.cloud import bigquery
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json')
project_id = 'theta-cell-406519'
client = bigquery.Client(credentials= credentials,project=project_id)

# def analysis_operations_inflation(client, country_code):
#     query = f"""
#         SELECT country_code, year, energy_consumer_price, food_consumer_price, headline_consumer_price, official_core_consumer_price, producer_price_inflation
#         FROM `theta-cell-406519.bharath_inflation_dataset.inflation`
#         WHERE country_code = '{country_code}'
#     """
#
#     result = client.query(query).to_dataframe()
#
#     if result.empty:
#         print(f"No data found for country code {country_code}")
#     else:
#         col_data = ['energy_consumer_price', 'food_consumer_price', 'headline_consumer_price', 'official_core_consumer_price', 'producer_price_inflation']
#
#         # Melt the DataFrame to combine columns into a single variable
#         df_melted = pd.melt(result, id_vars=['year'], value_vars=col_data, var_name='Consumer Price Type', value_name='Consumer Price')
#
#         plt.figure(figsize=(12, 6))
#         sns.barplot(x="year", y="Consumer Price", hue="Consumer Price Type", data=df_melted, palette="viridis")
#         plt.xlabel("Year")
#         plt.ylabel("Consumer Price")
#         plt.title(f"Bar Graph for Consumer Prices in {country_code}")
#         plt.legend(title="Consumer Price Type", bbox_to_anchor=(1, 1))
#         plt.show()

def analysis_operations_inflation(client, country_code):
    query = f"""
        SELECT country_code, year, energy_consumer_price, food_consumer_price, headline_consumer_price, official_core_consumer_price, producer_price_inflation 
        FROM `theta-cell-406519.bharath_inflation_dataset.inflation` 
        WHERE country_code = '{country_code}'
    """

    result = client.query(query).to_dataframe()

    if result.empty:
        print(f"No data found for country code {country_code}")
    else:
        col_data = ['energy_consumer_price', 'food_consumer_price', 'headline_consumer_price', 'official_core_consumer_price', 'producer_price_inflation']

        # Melt the DataFrame to combine columns into a single variable
        df_melted = pd.melt(result, id_vars=['year'], value_vars=col_data, var_name='Consumer Price Type', value_name='Consumer Price')

        plt.figure(figsize=(12, 6))
        sns.lineplot(x="year", y="Consumer Price", hue="Consumer Price Type", data=df_melted, palette="viridis")
        plt.xlabel("Year")
        plt.ylabel("Consumer Price")
        plt.title(f"Line Graph for Consumer Prices in {country_code}")
        plt.legend(title="Consumer Price Type", bbox_to_anchor=(1, 1))
        plt.show()


def analysis_country_data(client, country_codes):
    # Generate a string of comma-separated country codes
    country_codes_str = ', '.join([f"'{code.upper()}'" for code in country_codes])

    query = f"""
        SELECT country, IMF_count, country_code
        FROM `theta-cell-406519.bharath_inflation_dataset.countries`
        WHERE COUNTRY_CODE IN ({country_codes_str})
    """

    result = client.query(query).to_dataframe()

    if result.empty:
        print("No data found for the provided country codes")
    else:
        plt.figure(figsize=(12, 6))
        sns.barplot(x="country", y="IMF_count", hue="country_code", data=result, palette="viridis")
        plt.xlabel("Country")
        plt.ylabel("IMF count")
        plt.title("Bar Graph for IMF Count in Selected Countries")
        plt.legend(title="Country Code", bbox_to_anchor=(1, 1))
        plt.show()


def get_multiple_inputs():
    user_inputs = []
    while True:
        user_input = input("Enter a country code (or 'done' to finish): ").upper()
        if user_input == 'DONE':
            break
        user_inputs.append(user_input)
    return user_inputs
