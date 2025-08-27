import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("Survey Analyzer is ready!")
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)

# Read the CSV file
data = pd.read_csv('annual_enterprise_survey_2024.csv')

# Filter to a specific industry (default to 'All industries', modifiable)
industry_filter = 'All industries'  # Change this to e.g., 'Horticulture and Fruit Growing'
data = data[data['Industry_name_NZSIOC'] == industry_filter]

# Use Year as the x-axis value (numeric for simplicity)
data['year'] = data['Year']

# Sort data by year and reset index
data = data.sort_values('year').reset_index(drop=True)

# Select key variables to plot
key_variables = ['Total income', 'Surplus before income tax', 'Total expenditure']
data = data[data['Variable_name'].isin(key_variables)]

# Replace 'C' with NaN for plotting
data['Value'] = pd.to_numeric(data['Value'].replace('C', pd.NA), errors='coerce')

# Pivot data for line plot
pivot_data = data.pivot(index='year', columns='Variable_name', values='Value').reset_index()

# Print parsed and sorted data
print(f"Parsed and sorted data for {industry_filter} with key variables:")
print(pivot_data)

# Create a line plot for survey data
plt.figure(figsize=(12, 6))  # Increased size for readability
for column in key_variables:
    if column in pivot_data.columns:
        plt.plot(pivot_data['year'], pivot_data[column], marker='o', label=column, linewidth=2)

plt.xlabel('Year', fontsize=12)
plt.ylabel('Value (Millions of Dollars)', fontsize=12)
plt.title(f'Survey Data Trends for {industry_filter}', fontsize=14, pad=15)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.xticks(pivot_data['year'], rotation=45)  # Rotate x-axis labels for clarity

# Add value annotations
for column in key_variables:
    if column in pivot_data.columns:
        for i, value in enumerate(pivot_data[column]):
            if pd.notna(value):
                plt.text(pivot_data['year'][i], value, f'{int(value)}', 
                         ha='center', va='bottom', fontsize=9)

plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('survey.png', dpi=300)  # Higher DPI for sharper image
print("Survey saved as 'survey.png' in the project folder!")

# Show the plot interactively
plt.show()