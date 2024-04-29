import pandas as pd

RTAcleaned = "../cleaned_data/RTA-Dataset-cleaned.csv"

df = pd.read_csv(RTAcleaned)

df = df.drop(df[df["Type_of_vehicle"].str.lower() == "other"].index)

VehicleCounts = df["Type_of_vehicle"].value_counts()

typesOfVehicle = VehicleCounts.head(10)

sumOfCounts = VehicleCounts.sum()

print(typesOfVehicle)
print(sumOfCounts)
