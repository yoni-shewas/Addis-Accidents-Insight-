import pandas as pd

RTAraw = "../data/RTA-Dataset.csv"


def clean_data(filename):
    try:
        # read csv file
        df = pd.read_csv(filename)

        # remove missing and duplicates value
        df = df.dropna()
        df = df.drop_duplicates()
        df = df.reset_index(drop=True)

        df = df.drop('Cleaning (1 or 0)', axis=1)

        # Save cleaned data to a new CSV file
        cleaned_filename = f"cleaned_data/{filename}"
        df.to_csv(cleaned_filename, index=False)
        print("Data cleaned and saved to cleaned_data")

    except Exception as e:
        print(f'An error occurred: {e}')


clean_data(RTAraw)
