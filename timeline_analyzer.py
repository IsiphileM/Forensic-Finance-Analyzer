import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("Timeline Analyzer is ready!")
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)

# Read the CSV file
data = pd.read_csv('browser_history.csv')

# Convert timestamp column to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Sort data by timestamp and reset index for clean display
data = data.sort_values('timestamp').reset_index(drop=True)

# Calculate time differences between events (in minutes)
data['time_diff'] = data['timestamp'].diff().dt.total_seconds() / 60.0

# Print parsed and sorted data
print("Parsed and sorted data with time differences (in minutes):")
print(data)

# Create the timeline plot
plt.figure(figsize=(10, 4))  # Set figure size
for i, row in data.iterrows():
    plt.plot([row['timestamp'], row['timestamp']], [0, 1], 'b-', linewidth=2)  # Vertical line for each event
    plt.text(row['timestamp'], 1.1, f"{row['website']} ({row['action']})", 
             rotation=45, ha='right', va='bottom', fontsize=8)  # Label above each event
plt.yticks([])  # Hide y-axis
plt.xlabel('Time')
plt.title('User Activity Timeline')
plt.grid(True)
plt.tight_layout()

# Customize x-axis to show full date and time
plt.gcf().autofmt_xdate()  # Auto-format dates for readability

# Save the plot as a PNG file
plt.savefig('timeline.png')
print("Timeline saved as 'timeline.png' in the project folder!")

# Show the plot interactively
plt.show()