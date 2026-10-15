#22.	Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def calculate_stats(numbers):
    if not numbers:
        return None, None, 0, 0

    minimum = min(numbers)
    maximum = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    return minimum, maximum, total_sum, average
numbers = [10, 20, 30, 40, 50]
min_value, max_value, total_sum, avg = calculate_stats(numbers)
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Sum: {total_sum}")
print(f"Average: {avg}")