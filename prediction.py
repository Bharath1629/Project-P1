import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from google.cloud import bigquery

# Set up BigQuery client (replace 'path/to/your/credentials.json' with your actual JSON file path)
from google.oauth2 import service_account
import warnings

# Ignore specific warnings
warnings.filterwarnings("ignore", message="No frequency information was provided")
warnings.filterwarnings("ignore", message="Non-stationary starting autoregressive parameters found")
warnings.filterwarnings("ignore", category=FutureWarning, module="statsmodels.tsa.statespace.representation")
warnings.filterwarnings("ignore", category=FutureWarning, module="pandas.core.indexing")
warnings.filterwarnings("ignore", message="Series.__getitem__ treating keys as positions is deprecated")

credentials = service_account.Credentials.from_service_account_file('credentials.json')
project_id = 'theta-cell-406519'
client = bigquery.Client(credentials=credentials, project=project_id)

def inflation_rate_types():
    print("1.Headline Consumer Price")
    print("2.Energy Consumer Price")
    print("3.Food Consumer Price")
    print("4.Official Core Consumer Price")
    print("5.Producer Price Inflation")

# Function to query BigQuery for inflation data
def get_inflation_data_from_bigquery(client, country_code, inflation_type):
    query = f"""
        SELECT year, {inflation_type}
        FROM theta-cell-406519.bharath_inflation_dataset.inflation
        WHERE country_code = '{country_code}'
        ORDER BY year
    """
    df = client.query(query).to_dataframe()
    df['year'] = pd.to_datetime(df['year'], format='%Y')
    df.set_index('year', inplace=True)
    return df

# Function to predict inflation for a specific year and country
def predict_inflation_for_year_and_country(df,country, year, inflation_type):
    order = (1, 1, 1)  # Adjust order based on your data characteristics
    # freq = 'A'  # Assuming annual frequency, adjust as needed
    model = ARIMA(df[inflation_type], order=order)#, freq=freq)
    fit_model = model.fit()

    # Make predictions
    predictions = fit_model.predict(start=len(df), end=len(df) + 5, typ='levels')  # Predict 5 years ahead

    # Display the predicted inflation rate
    predicted_inflation = predictions[0]
    return predicted_inflation

# Example usage
def display_result(user_country,user_year,predicted_inflation,country_data,inflation_type):
    try:
        print(f"\nPredicted Inflation Rate for {user_country} in {user_year}: {predicted_inflation:.2f}%")
        plt.figure(figsize=(10, 6))
        plt.plot(country_data.index, country_data[inflation_type], label='Historical')
        plt.scatter([pd.to_datetime(f'{user_year}-01-01')], [predicted_inflation], color='red', label='Predicted', marker='o')
        plt.title(f'Inflation Rates for {inflation_type.replace("_", " ").title()} in {user_country}')
        plt.xlabel('Year')
        plt.ylabel('Inflation Rate')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
