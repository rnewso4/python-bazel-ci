
def add(num_1, num_2):
    '''
    Adds two numbers
    Parameters:
      a (int or float): Any real number
      b (int or float): Another real number
    
    Returns:
      a + b (int or float): the sum of a and b
    '''
    return num_1 + num_2


def subtract(num_1, num_2):
    '''
    Subtracts two numbers
    Parameters:
      a (int or float): Any real number
      b (int or float): Another real number
    
    Returns:
      a - b (int or float): the subtraction of b from a
    '''
    return num_1 - num_2

def multiply(num_1, num_2):
    '''
    Multiplies two numbers
    Parameters:
      a (int or float): Any real number
      b (int or float): Another real number
      
    Returns:
      a * b (int or float): the multiplication of a and b
    '''
    return num_1 * num_2

def divide(num_1, num_2):
    '''
    Divides two numbers
    Parameters:
      a (int or float): Any real number
      b (int or float): Another real number
      
    Returns:
      a / b (int or float): the result of the division of a by b
    '''
    assert(num_2 < 0 or num_2 > 0)
    return num_1 / num_2