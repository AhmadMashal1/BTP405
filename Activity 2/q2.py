import matplotlib.pyplot as plt

def graphSnowfall(file_path):
    # Read snowfall data from the text file
    with open(file_path, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file if line.strip().isdigit()]

   
    ranges = [0] * 6  # 0-10, 11-20, 21-30, 31-40, 41-50, 51 and above

    # Aggregate snowfall data into ranges
    for snowfall in snowfall_data:
        if snowfall <= 10:
            ranges[0] += 1
        elif 11 <= snowfall <= 20:
            ranges[1] += 1
        elif 21 <= snowfall <= 30:
            ranges[2] += 1
        elif 31 <= snowfall <= 40:
            ranges[3] += 1
        elif 41 <= snowfall <= 50:
            ranges[4] += 1
        else:
            ranges[5] += 1

    # Plotting the bar chart
    x_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51+']
    plt.bar(x_labels, ranges, color='skyblue')
    plt.xlabel('Snowfall Ranges (in cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Ranges')
    plt.show()

# Example usage:
file_path = 'q2_data.txt'  # text file with the data 
graphSnowfall(file_path)
