import json
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: JSON parsing with nested columns
json_file_path = r'C:\Users\nithi\OneDrive\Desktop\pro\Data1.json'
with open(json_file_path) as json_file:
    data = json.load(json_file)

# Task 2: Data transformation and aggregations
df = pd.DataFrame(data)  # Convert JSON data to DataFrame

plt.show()
