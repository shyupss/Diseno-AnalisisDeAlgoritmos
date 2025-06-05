def fibonacci_dp_2vars(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a = 1  # F(1)
    b = 1  # F(2)
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b