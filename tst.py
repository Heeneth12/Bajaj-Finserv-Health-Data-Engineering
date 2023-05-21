import pandas as pd
import json
# Read the JSON file
with open(r'C:\Users\nithi\OneDrive\Desktop\pro\Data1.json') as json_file:
    data = json.load(json_file)

# Flatten the nested structure
df = pd.json_normalize(data)

# Select the desired columns
selected_columns = ['appointmentId', 'phoneNumber', 'patientDetails.firstName', 'patientDetails.lastName',
                    'patientDetails.gender', 'patientDetails.birthDate', 'consultationData.medicines']
df_selected = df[selected_columns]

# Transform the gender column
df_selected['patientDetails.gender'] = df_selected['patientDetails.gender'].map({'M': 'Male', 'F': 'Female'})

# Print the resulting DataFrame
print(df_selected)
