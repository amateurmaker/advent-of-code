def is_valid_sequence(lst):
    # Check if a sequence is either strictly increasing or strictly decreasing
    # and the differences are between 1 and 3.
    if len(lst) <= 1:
        return True  # A single element or empty list is trivially valid

    is_increasing = None
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        
        # Check if the difference is valid
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        # Determine if the sequence is increasing or decreasing
        if is_increasing is None:
            if diff > 0:
                is_increasing = True
            elif diff < 0:
                is_increasing = False
        else:
            # If it was increasing and now decreases, or vice versa, it's invalid
            if is_increasing and diff < 0:
                return False
            if not is_increasing and diff > 0:
                return False

    return True

def compute_data(lst):
    # Check if the entire sequence is already valid
    if is_valid_sequence(lst):
        return 1  # The sequence is already safe
    
    # Try removing each element and check if the remaining sequence is valid
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]  # Remove the i-th element
        if is_valid_sequence(new_lst):
            return 1  # The sequence is valid after removing one element

    return 0  # No valid sequence found, return unsafe

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
