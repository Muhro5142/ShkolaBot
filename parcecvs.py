import pandas as pd

# Load the CSV file
file_path = 'school.csv'  # Replace with your file path
data = pd.read_csv(file_path, header=None)

# Extract header rows and reset index
header = data.iloc[:3].fillna("").values
data = data.iloc[3:].reset_index(drop=True)

# Clean and update column headers
columns = [
    f"{header[0][i]}{header[1][i]}{header[2][i]}".strip(",") for i in range(len(header[0]))
]
data.columns = columns

# Reset the row numbering and clean up
data.columns = ["Month", "Day", "Hebrew Day", "Layer 10", "Layer 11", "Layer 12", "General"]
data["Month"] = data["Month"].ffill()
data = data.dropna(how="all").reset_index(drop=True)

# Drop NaN values when converting to dictionary
data_dict = [
    {k: v for k, v in row.items() if pd.notna(v)} for row in data.to_dict(orient="records")
]

# Save to a new CSV file
output_path = "formatted_calendar.csv"
data.to_csv(output_path, index=False, encoding="utf-8-sig")

# Output
print(data_dict)
print(f"Reformatted data saved to {output_path}")
