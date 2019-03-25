def sum_array(array):
    '''
    Calculate sum of array

    Args:
        n (int) items in array

    Returns:
            sum_array equal to sum of all items in array
    '''
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    """
    Calculate nth term in factorial

    Args:
        n (int): nth term in factorial sequence to calculate

    Returns:
        int: nth term of factorial sequence,
             equal product of all integers from 1 to nth term
    """
    if n == 1:
        return n
    elif: n  == 0:
            return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    '''
    Args:
        word (string)

    Returns:
     string: word in reverse
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
