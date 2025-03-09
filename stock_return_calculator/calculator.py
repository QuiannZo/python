import pandas as pd
import os

import merge_stock_data

# A fn to get the desired data range
def get_information(ticket, start_date, end_date):
    file_path = "stock_return_csvs/" + ticket + ".csv"

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    # Convertir la columna 'date' a tipo datetime, con formato 'month.day.year'
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    
    # Definir las fechas de inicio y fin
    start = pd.to_datetime(start_date, format="%m/%d/%Y")
    end = pd.to_datetime(end_date, format="%m/%d/%Y")

    # Filtrar las filas en el rango de fechas
    df_filtrado = df[(df["Date"] >= start) & (df["Date"] <= end)]
    print(df_filtrado.head(1))

    return df_filtrado

def get_stock_return(df, initial_investment, monthly_contribution):
    # Get capital gains over time with monthly additions.
    # Iterate through each row on the "Change %" column to get the daily return values.
    total = initial_investment
    last_month = None

    for index, row in df.iterrows():
        # Convert current date to datetime format
        current_date = pd.to_datetime(row["Date"])

        # Add monthly contribution at the start of a new month
        if last_month is None or current_date.month != last_month:
            total += monthly_contribution  # Add money to investment
            last_month = current_date.month  # Update last month tracker

        # Calculate stock return
        daily_return_str = row["Change %"]
        if "%" in str(daily_return_str):
            daily_ret = float(daily_return_str.replace('%', '')) / 100
        else:
            daily_ret = float(daily_return_str) / 100
        # Get the total new value.
        total = total * (1 + daily_ret)

    print(round(total, 2))

def get_stock_return_external_dividends(df, initial_investment, monthly_contribution):
    # Ask the user if he wants the calculation to contain dividend reinvestment.
    div = input("Reinvest dividends (yes/no): ")
    if div == "no":
        get_stock_return(df, initial_investment)
        return
    total = initial_investment
    for index, row in df.iterrows():
        # Check for dividend payment
        div_bool = False # Boolean to check if dividends have been paid.

        # Calculate stock return
        daily_return_str = row["Change %"]
        if "%" in str(daily_return_str):
            daily_ret = float(daily_return_str.replace('%', '')) / 100
        else:
            daily_ret = float(daily_return_str)
        # Get the total new value.
        total = total * (1 + daily_ret)

    print(str(round(total, 2)) + " with dividends included.")

# Calculate stock returns based on the user's desired parameters.
# This base function calls two other functions based on the existence of external dividend data.
def get_return():
    # Get initial data from the user. (Console atm).
    ticket = input("Ticket: ")
    #start_date = input("Start date(month/day/year): ")
    #end_date = input("End date(month/day/year): ")
    #initial_investment = float(input("initial investment: "))
    #monthly_contribution = float(input("monthly contribution: "))
    start_date = "01/01/2012"
    end_date = "01/01/2023"
    initial_investment = 10000.0
    monthly_contribution = 100.0

    # Get data from ticket on the selected range
    df = get_information(ticket, start_date, end_date)

    # Calculate return depending on dividends availability.
    if os.path.exists("stock_return_csvs/" + ticket + "d.csv"):
        get_stock_return_external_dividends(df, initial_investment, monthly_contribution)
    else:
        get_stock_return(df, initial_investment, monthly_contribution)

if __name__ == "__main__":
    get_return()