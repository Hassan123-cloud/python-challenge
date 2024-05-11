# Modules
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# Initialize variables
month_count = 0
total_profit = 0
changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Loop through each row of data
    for i, row in enumerate(csvreader):
        # Count months and add up profits
        month_count += 1
        total_profit += int(row[1])

        # Calculate changes in profit
        if i > 0:
            change = int(row[1]) - int(prev_row[1])
            changes.append(change)
        prev_row = row

    # Calculate average change
    avg_change = sum(changes) / len(changes)

    # Find greatest increase and decrease in profits
    max_change = max(changes)
    min_change = min(changes)

    # Reset file pointer
    csvfile.seek(0)
    next(csvreader)  # Skip the header row

    # Find months corresponding to greatest increase and decrease
    for row in csvreader:
        if int(row[1]) - int(prev_row[1]) == max_change:
            max_month = row[0]
        if int(row[1]) - int(prev_row[1]) == min_change:
            min_month = row[0]
        prev_row = row

# Generate output
output = f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

# Print output to console
print(output)

# Write output to a text file
with open("output_booth.txt", "w") as f:
    f.write(output)
