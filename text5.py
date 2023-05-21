import pandas as pd
from datetime import datetime

# Read the JSON file
df = pd.read_json(r'C:\Users\nithi\OneDrive\Desktop\pro\Data1.json')

# Flatten the nested structure of patientDetails
df_patientDetails = pd.json_normalize(df['patientDetails'])

# Flatten the nested structure of consultationData
df_consultationData = pd.json_normalize(df['consultationData'])

# Combine the flattened dataframes
df_selected = pd.concat([df[['appointmentId', 'phoneNumber']], df_patientDetails[['firstName', 'lastName', 'gender', 'birthDate']], df_consultationData['medicines']], axis=1)

# Transform the gender column
df_selected['gender'] = df_selected['gender'].map({'M': 'Male', 'F': 'Female'})
df_selected['gender'].fillna('Others', inplace=True)

# Rename the birthDate column as DOB
df_selected.rename(columns={'birthDate': 'DOB'}, inplace=True)

# Create the fullName column
df_selected['fullName'] = df_selected['firstName'] + ' ' + df_selected['lastName']

# Convert DOB to datetime objects
df_selected['DOB'] = pd.to_datetime(df_selected['DOB'], utc=True)

# Calculate age based on current date
current_date = pd.to_datetime('now', utc=True)
df_selected['Age'] = (current_date - df_selected['DOB']).dt.days // 365

# Calculate the number of medicines prescribed
df_selected['noOfMedicines'] = df_selected['medicines'].apply(lambda x: len(x) if isinstance(x, list) else 0)

# Calculate the number of active medicines prescribed
df_selected['noOfActiveMedicines'] = df_selected['medicines'].apply(lambda x: sum(1 for med in x if isinstance(med, dict) and med.get('IsActive', False)) if isinstance(x, list) else 0)

# Calculate the number of inactive medicines prescribed
df_selected['noOfInactiveMedicines'] = df_selected['medicines'].apply(lambda x: sum(1 for med in x if isinstance(med, dict) and not med.get('IsActive', False)) if isinstance(x, list) else 0)

# Group by appointmentId and aggregate the columns
df_aggregated = df_selected.groupby('appointmentId').agg({
    'noOfMedicines': 'sum',
    'noOfActiveMedicines': 'sum',
    'noOfInactiveMedicines': 'sum'
}).reset_index()

# Print the resulting DataFrame
print(df_aggregated)
