import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("Survey Analyzer is ready!")
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)

# This ofc Reads the CSV file
data = pd.read_csv('annual_enterprise_survey_2024.csv')

# Filtered data to a specific industry (default to 'All industries', but defs modifiable)
industry_filter = 'All industries'
data = data[data['Industry_name_NZSIOC'] == industry_filter]

# Year as x-axis value (used numeric system for simplicity)
data['year'] = data['Year']

# Sorted data by year and reset index
data = data.sort_values('year').reset_index(drop=True)

# Selected key variables to plot
key_variables = ['Total income', 'Surplus before income tax', 'Total expenditure']
data = data[data['Variable_name'].isin(key_variables)]

# Replaced 'C' with NaN for plotting
data['Value'] = pd.to_numeric(data['Value'].replace('C', pd.NA), errors='coerce')

# Did this for line plot
pivot_data = data.pivot(index='year', columns='Variable_name', values='Value').reset_index()

# This Prints parsed and sorted data
print(f"Parsed and sorted data for {industry_filter} with key variables:")
print(pivot_data)

# Creates a line plot for survey data
plt.figure(figsize=(12, 6))  # Here i just increased the size for readability
for column in key_variables:
    if column in pivot_data.columns:
        plt.plot(pivot_data['year'], pivot_data[column], marker='o', label=column, linewidth=2)

plt.xlabel('Year', fontsize=12)
plt.ylabel('Value (Millions of Dollars)', fontsize=12)
plt.title(f'Survey Data Trends for {industry_filter}', fontsize=14, pad=15)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.xticks(pivot_data['year'], rotation=45)  # Rotated x-axis labels for more clarity

# This is to add value annotations
for column in key_variables:
    if column in pivot_data.columns:
        for i, value in enumerate(pivot_data[column]):
            if pd.notna(value):
                plt.text(pivot_data['year'][i], value, f'{int(value)}', 
                         ha='center', va='bottom', fontsize=9)

plt.tight_layout()

# This saves the plot as a PNG file
plt.savefig('survey.png', dpi=300)  # Higher DPI for sharper image
print("Survey saved as 'survey.png' in the project folder!")

# Shows the plot interactively
plt.show()
