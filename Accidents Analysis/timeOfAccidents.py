import pandas as pd


# Classify dates based on time give
def period_group(hour):
    hour = int(hour)
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"


RTAcleaned = "../cleaned_data/RTA-Dataset-cleaned.csv"

df = pd.read_csv(RTAcleaned)

df['time_periods'] = df['Hr_time'].apply(period_group)
