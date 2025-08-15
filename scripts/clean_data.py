import pandas as pd

def clean_sales_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    df = clean_sales_data("data/sales.csv")
    print(df.head())
