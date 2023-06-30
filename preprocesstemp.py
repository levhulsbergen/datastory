import pandas as pd

df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")

# Calculate the average temperature for each country in 2010
average_temperatures_2010 = df[df['dt'].str[:4] == '1950'].groupby('Country')['AverageTemperature'].mean()

# Create a DataFrame from the average temperatures
average_temperatures_2010_df = pd.DataFrame(average_temperatures_2010, columns=['AverageTemperature'])

# Add a 'Country' column based on the index
average_temperatures_2010_df['Country'] = average_temperatures_2010_df.index

# Reset the index of the DataFrame
average_temperatures_2010_df.reset_index(drop=True, inplace=True)

# Export the DataFrame to a CSV file
average_temperatures_2010_df.to_csv('average_temperatures_1950.csv', index=False)

