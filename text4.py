import pandas as pd
from datetime import datetime

# Read the JSON file
df = pd.read_json(r'C:\Users\nithi\OneDrive\Desktop\pro\Data1.json')


df_patientDetails = pd.json_normalize(df['patientDetails'])


df_consultationData = pd.json_normalize(df['consultationData'])


df_selected = pd.concat([df[['appointmentId', 'phoneNumber']], df_patientDetails[['firstName', 'lastName', 'gender', 'birthDate']], df_consultationData['medicines']], axis=1)

# Transform the gender column
df_selected['gender'] = df_selected['gender'].map({'M': 'Male', 'F': 'Female'})
df_selected['gender'].fillna('Others', inplace=True)


df_selected.rename(columns={'birthDate': 'DOB'}, inplace=True)

# Create the fullName column
df_selected['fullName'] = df_selected['firstName'] + ' ' + df_selected['lastName']


df_selected['DOB'] = pd.to_datetime(df_selected['DOB'], utc=True)


current_date = pd.to_datetime('now', utc=True)
df_selected['Age'] = (current_date - df_selected['DOB']).dt.days // 365

# Print the resulting DataFrame
print(df_selected)
