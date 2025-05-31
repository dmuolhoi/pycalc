"""
Division module.
Provides functions for dividing numbers.
"""

def divide_numbers(numbers):
    """
    Divide the first number by all subsequent numbers.
    
    Args:
        numbers (list): List of numbers where the first is divided by the rest
        
    Returns:
        float: Result of the division
        
    Raises:
        ZeroDivisionError: If any divisor is zero
    """
    if not numbers:
        return 0
        
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result /= num
        
    return result