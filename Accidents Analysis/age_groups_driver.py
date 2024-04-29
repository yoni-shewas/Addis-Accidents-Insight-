import pandas as pd


# Classify dates based on time give
def classify_age(age):
    if age < 18:
        return "Young"
    elif 18 <= age <= 30:
        return "Adult"
    elif 31 <= age <= 50:
        return "Middle-aged"
    else:
        return "Senior"


RTAcleaned = "../cleaned_data/RTA-Dataset-cleaned.csv"

df = pd.read_csv(RTAcleaned)

df['age_classification'] = df['Hr_time'].apply(classify_age)
