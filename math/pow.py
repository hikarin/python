def pow(x, n):
    value = 1
    while n > 0:
        value *= x
        n -= 1
    return value

print pow(2, 10)
