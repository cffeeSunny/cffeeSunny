# Write a Python function named previous_odd_number takes a number n and returns the previous odd number before n.
# You should not use if-elif-else constructs.
def previous_odd_number(n):
    return n - (n % 2) - 1
