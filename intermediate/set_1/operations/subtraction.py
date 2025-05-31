"""
Subtraction module.
Provides functions for subtracting numbers.
"""

def subtract_numbers(numbers):
    """
    Subtract numbers from the first number.
    
    Args:
        numbers (list): List of numbers where the first number is the minuend
                        and the rest are subtracted from it
        
    Returns:
        float: Result of the subtraction
    """
    if not numbers:
        return 0
        
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
        
    return result