import os
import pandas as pd

RTAraw = "data/RTA-Dataset.csv"


def clean_data(filename):
    try:
        # read csv file
        df = pd.read_csv(filename, na_values=[
            'na', 'NaN'])

        # remove missing and duplicates value
        df = df.dropna()
        df = df.drop_duplicates()
        df = df.reset_index(drop=True)

        df['Hr_time'] = df['Time'].str.split(':').str[0]

        to_drop = [
            'Sex_of_casualty',
        ]

        # Remove specified columns without inplace=True
        df.drop(columns=to_drop, inplace=True)

        # Create directory if it doesn't exist
        cleaned_dir = "../cleaned_data"
        if not os.path.exists(cleaned_dir):
            os.makedirs(cleaned_dir)

        # Save cleaned data to a new CSV file
        cleaned_filename = os.path.join(
            cleaned_dir, os.path.basename("RTA-Dataset-cleaned.csv"))
        df.to_csv(cleaned_filename, index=False)
        print("Data cleaned and saved to cleaned_data")

    except Exception as e:
        print(f'An error occurred: {e}')


clean_data(RTAraw)
