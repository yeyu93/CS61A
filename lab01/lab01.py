"""Lab 1: Expressions and Control Structures"""


# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0  # You can replace this line!


# Q4
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    # floor division:整除得一个整数 modulo:求余数
    a = []
    total = 0
    if n < 0:
        return False
    elif 0 <= n < 10:
        return n
    else:
        while n // 10 != 0:
            b = n % 10
            n = n // 10
            a.append(b)
            if n < 10:
                a.append(n)
        for i in range(0, len(a)):
            total = total + a[i]
        return total
