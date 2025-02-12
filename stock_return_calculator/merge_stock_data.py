import pandas as pd
import os

# Function to add a column to a data set
def add_dividends(file_base, file_dividends, output_folder="stock_return_csvs", output_filename="merged.csv"):
    output_path = os.path.join(output_folder, output_filename) # Output for the end file.

    # Read main file
    df_main = pd.read_csv(file_base)
    df_main['Date'] = pd.to_datetime(df_main['Date'], errors='coerce').dt.strftime("%m/%d/%Y")

    # Read dividend file
    df_dividends = pd.read_csv(file_dividends)
    df_dividends['Date'] = pd.to_datetime(df_dividends['Date']).dt.date

    # Ensure that both 'Date' columns are of the same type (datetime64)
    df_dividends['Date'] = pd.to_datetime(df_dividends['Date'], format="%Y-%m-%d")

    # Merge the main file with the column "Yield" to add the dividend yield to each date.
    df_merged = pd.merge_asof(df_main.sort_values("Date"), # merge_asof does a join of the main dataset with a selected column of the second.
                            df_dividends.sort_values("Date"), #params (left, right, fussion-column, direction)
                            on="Date", 
                            direction="nearest")

    # Fill NaN(NULL) boxes with the last known value.
    df_merged["Yield"].ffill(inplace=True) # inplace=true modifies the original file.

    # Change the format of 'Date' to %m/%d/%Y
    df_merged["Date"] = df_merged["Date"].dt.strftime("%m/%d/%Y") # Use the original fortmat.

    # Guardar el resultado
    df_merged.to_csv(output_path, index=False)
    print(f"Archivo guardado en: {output_path}")

# Function to merge two data sets. 
def merge_stock_data(file_old_data, file_new_data, output_folder="stock_return_csvs", output_filename="merged_stock_data.csv"):
    # Crear la carpeta si no existe
    os.makedirs(output_folder, exist_ok=True) # Si el folder esta no modifica.
    output_path = os.path.join(output_folder, output_filename)
    
    # Read CSV files
    df1 = pd.read_csv(file_old_data)
    df2 = pd.read_csv(file_new_data)
    
    # Quitar la primera fila del segundo archivo
    df1 = df1.iloc[1:]
    
    # Concatenar los datos
    merged_df = pd.concat([df2, df1], ignore_index=True)
    
    # Guardar el resultado
    merged_df.to_csv(output_path, index=False)
    print(f"Archivo guardado en: {output_path}")

# Function to add a "Change %" column to get n time price changes.
def add_change_percentage(file_base, output_folder="stock_return_csvs", output_filename="merged.csv"):
    output_path = os.path.join(output_folder, output_filename) # Output for the end file.

    # Read main file
    df_main = pd.read_csv(file_base)
    df_main['Date'] = pd.to_datetime(df_main['Date'], errors='coerce').dt.strftime("%m/%d/%Y")

    # Check if 'Open' and 'Close' columns exist
    if 'Open' in df_main.columns and 'Close' in df_main.columns:
        # Calculate percentage change: ((Close - Open) / Open) * 100
        df_main["Change %"] = (((df_main["Close"] - df_main["Open"]) / df_main["Open"]) * 100).round(5)
    else:
        print("Error: The CSV file must contain 'Open' and 'Close' columns.")
        return

    # Save the modified file
    df_main.to_csv(output_path, index=False)
    print(f"File saved successfully: {output_path}")

if __name__ == "__main__": # Se ejecuta solo en este archivo.
    #file2 = "stock_return_csvs/S&P500(1).csv"
    #merge_stock_data(file1, file2)
    file1 = "stock_return_csvs/aapl.csv"
    add_change_percentage(file1)