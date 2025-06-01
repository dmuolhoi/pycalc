"""
Multiplication module.
Provides functions for multiplying numbers.
"""

def multiply_numbers(numbers):
    """
    Multiply multiple numbers together.
    
    Args:
        numbers (list): List of numbers to multiply
        
    Returns:
        float: Product of all numbers
    """
    if not numbers:
        return 0
        
    result = 1
    for num in numbers:
        result *= num
        
    return result