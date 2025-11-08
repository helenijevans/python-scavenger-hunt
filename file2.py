def sum_non_consonants(text):
    """
    Returns the binary sum of ASCII values of all non-consonant characters in the string.
    """
    total = 0
    for char in text:
        if char not in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            total = ord(char)
    return bin(total)[2:]

# Clue 2 Execution - DO NOT CHANGE
text = "LENGTHS!"
print(sum_non_consonants(text))