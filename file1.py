def total_odds(nums):
    """
    Returns the sum of all odd values in a given list
    """
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

# Clue 1 Execution - DO NOT CHANGE
num_list = [2, 4, 6, 8, 10, 12, 3, 5, 7, 9, 11, 13, 15]
print(total_odds(num_list))
