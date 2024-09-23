Traffic Accident Data Analysis and Visualization
This project involves the analysis of a large dataset of U.S. traffic accidents, aiming to identify patterns related to weather conditions, road conditions, and time of day. The analysis utilizes visualizations to highlight key factors contributing to accidents.

Objective :
The project is designed to:
Analyze traffic accident data to uncover patterns related to weather and time.
Visualize accident hotspots across the U.S. using geographic data.
Explore the relationship between weather conditions and accident occurrence.

Dataset :
The dataset used in this analysis consists of 500,000 sampled records of traffic accidents in the U.S., containing fields such as:
Date and time of the accident 
Geographic location (latitude, longitude)
Weather conditions (e.g., temperature, visibility)
Road and traffic conditions
The original dataset can be accessed via Kaggle - [US Accidents Dataset](https://drive.google.com/file/d/1U3u8QYzLjnEaSurtZfSAS_oh9AT2Mn8X/edit).

Key Features :
Data Cleaning: Handling missing values and parsing timestamps.
Accident by Weather Condition: Visualizing accidents under different weather conditions.
Time of Day Analysis: Understanding how accidents are distributed by hour of the day.
Heatmap: Displaying accident hotspots using geographic data (latitude and longitude).
Temperature Correlation: Examining how weather conditions like temperature affect accident occurrence at different times of the day.

Requirements :
The project is implemented using Python. The following libraries are required:
pandas
seaborn
matplotlib
folium

To install the necessary libraries, 
run :
pip install pandas matplotlib seaborn folium

How to Run :
Clone the repository:
git clone https://github.com/ChinmayDandekar7/traffic-accident-analysis.git

Navigate to the project directory:
cd traffic-accident-analysis

Execute the Python script:
python TA.py

Outputs :
Bar Plot: Accidents by top 10 weather conditions.
Histogram: Accidents by hour of the day.
Interactive Heatmap: Geographic visualization of accident hotspots (saved as accident_hotspots.html).
Scatter Plot: Correlation between temperature and accident time, categorized by weather conditions.
Future Enhancements
Accident Severity Analysis: Further investigation into how accident severity correlates with weather and time of day.
Predictive Modeling: Building a machine learning model to predict the likelihood of accidents based on environmental factors.
Additional Visualizations: Incorporating more advanced geospatial analysis tools for a deeper understanding of accident locations.

Conclusion :
This project provides valuable insights into how environmental conditions and time influence traffic accidents. The visualizations and findings can serve as a foundation for more advanced studies and improvements in traffic safety planning.
