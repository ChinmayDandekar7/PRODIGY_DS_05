# Importing necessary libraries for data manipulation and visualization                             
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Step 1: Load the dataset
df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\PRODIGY_DS_05\US_Accidents_March23_sampled_500k.csv')

# Step 2: Data Cleaning
# Dropping rows with missing values in key columns
df_cleaned = df.dropna(subset=['Weather_Condition', 'Start_Time', 'Temperature(F)', 'Start_Lat', 'Start_Lng'])

# Converting 'Start_Time' to datetime, handling inconsistent formats
df_cleaned['Start_Time'] = pd.to_datetime(df_cleaned['Start_Time'], errors='coerce')

# Extracting hour of the day from 'Start_Time'
df_cleaned['Hour'] = df_cleaned['Start_Time'].dt.hour

# Step 3: Visualizing Accidents by Weather Condition (Top 10)
top_weather_conditions = df_cleaned['Weather_Condition'].value_counts().nlargest(10).index
df_top_weather = df_cleaned[df_cleaned['Weather_Condition'].isin(top_weather_conditions)]

plt.figure(figsize=(12, 6))  
sns.countplot(data=df_top_weather, y='Weather_Condition', order=df_top_weather['Weather_Condition'].value_counts().index, palette="coolwarm")
plt.title('Top 10 Accidents by Weather Condition', fontsize=16)
plt.xlabel('Number of Accidents', fontsize=12)
plt.ylabel('Weather Condition', fontsize=12)
plt.xticks(fontsize=10)  
plt.tight_layout()  # Adjusts the plot for better fit
plt.show()

# Step 4: Visualizing Accidents by Time of Day (Hour) with Sampling to Speed Up
# Sample the data for faster plotting (use 10% of the data)
df_sampled = df_cleaned.sample(frac=0.1, random_state=42)

plt.figure(figsize=(12, 6))  
sns.countplot(data=df_sampled, x='Hour', palette="coolwarm")
plt.title('Accidents by Time of Day', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Number of Accidents', fontsize=12)
plt.xticks(fontsize=10)  
plt.tight_layout()  # Ensures that the plot elements fit properly
plt.show()

# Step 5: Visualizing Accident Hotspots on Map
# Initialize a map centered on the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Prepare data for heatmap (using Start_Lat and Start_Lng)
heat_data = [[row['Start_Lat'], row['Start_Lng']] for index, row in df_cleaned.iterrows()]

# Add HeatMap layer to the map
HeatMap(heat_data).add_to(m)

# Save the map as an HTML file for interactive viewing
m.save('accident_hotspots.html')

# Step 6: Correlation Between Temperature and Accidents by Time of Day
plt.figure(figsize=(12, 6))  
sns.scatterplot(data=df_cleaned, x='Temperature(F)', y='Hour', hue='Weather_Condition', palette='coolwarm')
plt.title('Temperature vs Time of Day with Weather Conditions', fontsize=16)
plt.xlabel('Temperature (F)', fontsize=12)
plt.ylabel('Hour of the Day', fontsize=12)
plt.legend(title='Weather Condition', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjusted legend position
plt.tight_layout()  # Ensures that the plot elements fit properly
plt.show()
