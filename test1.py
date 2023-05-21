import pandas as pd

# Read the JSON file
df = pd.read_json(r'C:\Users\nithi\OneDrive\Desktop\pro\Data1.json')

# Flatten the nested structure of patientDetails
df_patientDetails = pd.json_normalize(df['patientDetails'])


df_consultationData = pd.json_normalize(df['consultationData'])


df_selected = pd.concat([df[['appointmentId', 'phoneNumber']], df_patientDetails[['firstName', 'lastName', 'gender', 'birthDate']], df_consultationData['medicines']], axis=1)


df_selected['gender'] = df_selected['gender'].map({'M': 'Male', 'F': 'Female'})
df_selected['gender'].fillna('Others', inplace=True)

# Rename the birthDate column as DOB
df_selected.rename(columns={'birthDate': 'DOB'}, inplace=True)

# Print the resulting DataFrame
print(df_selected)
