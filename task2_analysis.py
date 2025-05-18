import pandas as pd
import matplotlib.pyplot as plt

# Load the Benin dataset
file_path_benin = r'C:\Users\rebir\Downloads\Week 0-20250517T101621Z-1-001\Week 0\Technical Content\data\data\benin-malanville.csv'
df_benin = pd.read_csv(file_path_benin)

# Basic Exploration
print("First few rows of Benin data:")
print(df_benin.head())
print("\nInfo about Benin data:")
print(df_benin.info())

# Convert Timestamp
df_benin['Timestamp'] = pd.to_datetime(df_benin['Timestamp'])

# Plot GHI over time
plt.figure(figsize=(12, 6))
plt.plot(df_benin['Timestamp'], df_benin['GHI'])
plt.xlabel('Timestamp')
plt.ylabel('GHI')
plt.title('GHI over Time for Benin')
plt.grid(True)
plt.show()
plt.savefig('benin_ghi_timeseries.png')
