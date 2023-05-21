import pandas as pd


df = pd.read_json(r'C:\Users\nithi\OneDrive\Desktop\pro\Data1.json')


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

# Define a function to check phone number validity
def is_valid_mobile(phone_number):
    if phone_number.startswith('+91') or phone_number.startswith('91'):
        digits = phone_number[-10:]  # Extract the last 10 digits
        if digits.isnumeric() and 6000000000 <= int(digits) <= 9999999999:
            return True
    return False

# Apply the function to create the isValidMobile column
df_selected['isValidMobile'] = df_selected['phoneNumber'].apply(is_valid_mobile)

# Print the resulting DataFrame
print(df_selected)
