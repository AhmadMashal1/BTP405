
def print_stats_decorator(func):
    def wrapper(numbers):
        print(f"Numbers: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Average: {sum(numbers) / len(numbers)}")
        print(f"Maximum: {max(numbers)}")
        print("--------------------")
        return func(numbers)
    return wrapper

@print_stats_decorator
def printStats(numbers):
    # The decorator handles printing statistics
    pass


file_path = 'q4_data.txt'   # sample data for q4 print_stats_decorator
with open(file_path, 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.strip().split()]
        printStats(numbers)
