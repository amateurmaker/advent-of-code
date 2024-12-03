def compute_data(lst):
    if len(lst) == 1:
        return 1  # A single number is trivially "safe"

    is_increasing = None  # This will track if the sequence is increasing or decreasing
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]

        # Check if the difference is out of the allowed range (less than 1 or greater than 3)
        if abs(diff) < 1 or abs(diff) > 3:
            return 0
        
        if is_increasing is None:
            if diff > 0:
                is_increasing = True
            elif diff < 0:
                is_increasing = False
            continue

        # Check if direction is consistent (either all increasing or all decreasing)
        if (diff > 0 and not is_increasing) and (diff < 0 and is_increasing):
            return 0

    return 1  # If all checks pass, return 1 (safe)


# Open the file for reading and initialize report counter
report = 0

with open('input/day_two.txt', 'r') as file:
    for line in file:
        # Split the line into individual elements (assuming space separation)
        row = line.split()
        # Convert the elements to integers
        data = [int(x) for x in row]
        # Increment report count if the row is safe
        report += compute_data(data)

# Print the total number of safe reports
print(f"The report is: {report}")
