def reverse_string(s):
    '''
    Reverses the given string.
    Parameters:
        s (str): The string to reverse.
    Returns:
        str: The reversed string.
    '''
    return s[::-1]

def is_palindrome(s):
    '''
    Checks if the given string is a palindrome.
    Parameters:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    '''
    return s == reverse_string(s)

def count_vowels(s):
    '''
    Counts the number of vowels in the given string.
    Parameters:
        s (str): The string to count vowels in.
    Returns:
        int: The number of vowels in the string.
    '''
    return sum(1 for char in s if char.lower() in 'aeiou')
