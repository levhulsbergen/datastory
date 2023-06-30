# Select the columns for the visualization
columns = ['country', 'fossil_fuel_consumption', 'renewables_consumption', 'nuclear_consumption', 'year']
data = worldenergycons_clean[columns]

# Filter out rows with missing values in the selected columns
data = data.dropna(subset=['fossil_fuel_consumption', 'renewables_consumption', 'nuclear_consumption'])

# Select the top 10 countries with the most data
top_10_countries = data['country'].value_counts().nlargest(10).index
data = data[data['country'].isin(top_10_countries)]

# Select the most recent year for each country
data = data.groupby('country').max()

# Calculate the total consumption by summing up the energy sources
data['total_consumption'] = data['fossil_fuel_consumption'] + data['renewables_consumption'] + data['nuclear_consumption']

# Calculate the proportions of energy source consumption
data['fossil_fuel_proportion'] = data['fossil_fuel_consumption'] / data['total_consumption']
data['renewables_proportion'] = data['renewables_consumption'] / data['total_consumption']
data['nuclear_proportion'] = data['nuclear_consumption'] / data['total_consumption']

# Sort the data by total consumption in descending order
data = data.sort_values('total_consumption', ascending=False)

# Plot the stacked bar chart
plt.figure(figsize=(10, 6))
plt.bar(data.index, data['fossil_fuel_proportion'], label='Fossil Fuels')
plt.bar(data.index, data['renewables_proportion'], bottom=data['fossil_fuel_proportion'], label='Renewables')
plt.bar(data.index, data['nuclear_proportion'], bottom=data['fossil_fuel_proportion'] + data['renewables_proportion'], label='Nuclear')

plt.xlabel('Country')
plt.ylabel('Proportion of Energy Consumption')
plt.title('Comparison of Energy Sources Consumption by Country')
plt.legend()

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()