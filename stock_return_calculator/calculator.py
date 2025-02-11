import pandas as pd

import merge_stock_data

# A fn to get the desired data range
def get_information(ticket, start_date, end_date):
    df = pd.read_csv("stock_return_csvs/" + ticket + ".csv")

    # Convertir la columna 'date' a tipo datetime, con formato 'month.day.year'
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    
    # Definir las fechas de inicio y fin
    start = pd.to_datetime(start_date, format="%m/%d/%Y")
    end = pd.to_datetime(end_date, format="%m/%d/%Y")

    # Filtrar las filas en el rango de fechas
    df_filtrado = df[(df["Date"] >= start) & (df["Date"] <= end)]
    return df_filtrado

# Calculate stock returns based on the user's desired parameters.
def get_stock_return():
    # Get initial data from the user. (Console atm).
    ticket = input("Ticket: ")
    start_date = input("Start date(month/day/year): ")
    end_date = input("End date(month/day/year): ")
    initial_investment = float(input("initial investment: "))
    monthly_contribution = float(input("monthly contribution: "))

    # Get data from ticket on the selected range
    df = get_information(ticket, start_date, end_date)
    
    # Get capital gains over time with monthly additions.
    # Iterate through each row on the "Change %" column to get the daily return values.
    total = initial_investment
    for index, row in df.iterrows():
        # Check for dividend payment
        div_bool = False # Boolean to check if dividends have been paid.
        

        # Calculate stock return
        daily_return_str = row["Change %"]
        daily_ret = float(daily_return_str.replace('%', '')) / 100
        # Get the total new value.
        total = total * (1 + daily_ret)

    print(total)

if __name__ == "__main__":
    get_stock_return()