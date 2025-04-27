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

    # Check if 'Open' column exists
    if 'Open' in df_main.columns:
        # Calculate percentage change based on previous day's Open price
        df_main["Change %"] = df_main["Open"].pct_change().mul(100).round(5) # pct_change compares change from the immediate and previous row.
    else:
        print("Error: The CSV file must contain an 'Open' column.")
        return

    # Save the modified file
    df_main.to_csv(output_path, index=False)
    print(f"File saved successfully: {output_path}")

def clean_div_data(div_file, output_folder="stock_return_csvs", output_filename="clean.csv"):
    output_path = os.path.join(output_folder, output_filename) # Output for the end file.

    # Read the data (assuming you have it in a CSV file)
    df = pd.read_csv(div_file)

    # Ensure 'Date' is in datetime format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Filter only the months of interest (March, June, September, December)
    df_filtered = df[df["Date"].dt.month.isin([3, 6, 9, 12])]

    # Reset index for clarity
    df_filtered = df_filtered.reset_index(drop=True)

    # Save the cleaned data
    df_filtered.to_csv(output_path, index=False)

# Function to change the date format.
def format_date(file_base, output_folder="stock_return_csvs", output_filename="date_corrected.csv"):
    output_path = os.path.join(output_folder, output_filename) # Output for the end file.

    # Read the data
    df = pd.read_csv(file_base)

    # Ensure 'Date' is in datetime format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Date"] = df["Date"].dt.strftime("%m/%d/%Y")

    df.to_csv(output_path, index=False)

if __name__ == "__main__": # Se ejecuta solo en este archivo
    #file2 = "stock_return_csvs/S&P500(1).csv"
    #merge_stock_data(file1, file2)
    file1 = "stock_return_csvs/ftec.csv"
    #add_change_percentage(file1)
    #add_change_percentage(file1)
    add_change_percentage(file1)