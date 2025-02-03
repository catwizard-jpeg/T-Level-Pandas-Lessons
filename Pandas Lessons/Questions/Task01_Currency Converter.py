import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_csv("Data/currency.csv")

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

earliest_date = df['Date'].min().strftime('%d/%m/%Y')
latest_date = df['Date'].max().strftime('%d/%m/%Y')

print(f"The earliest date recorded is {earliest_date}.")
print(f"The latest date recorded is {latest_date}.")

currencies = df.columns.tolist() # Get all the columns in the dataframe
currencies.remove('Date')
print("Possible currency conversions are:")
for currency in currencies:
    print(currency)

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validate_currency(currency):
    return currency in df.columns.tolist()

def get_conversion_rate(date, currency):
    row = df[df['Date'] == pd.to_datetime(date, format='%d/%m/%Y')]
    if not row.empty and currency in row.columns:
        return row[currency].values[0]
    else:
        return None

def plot_conversion_rate(currency):
    df.plot(x='Date', y=currency)
    plt.show()

while True:
    date = input("Enter a date (DD/MM/YYYY): ")
    if not validate_date(date):
        print("Invalid date format. Please try again.")
        continue

    currency = input("Enter a currency: ")
    if not validate_currency(currency):
        print("Invalid currency. Please try again.")
        continue

    rate = get_conversion_rate(date, currency)
    if rate is not None:
        print(f"The conversion rate for {currency} on {date} is {rate}.")
        plot_conversion_rate(currency)
    else:
        print(f"No data available for {date}.")

    repeat = input("Do you want to perform another conversion? (yes/no): ")
    if repeat.lower() != 'yes':
        break



