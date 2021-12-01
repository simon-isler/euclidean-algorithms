# euclidean algorithm
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# extended euclidean algorithm
# a * x + b * y = gcd(a, b)
x_set = [1, 0]
y_set = [0, 1]


def extended_euclidean_algorithm(a, b, index=2):
    if b > a:
        a, b = b, a

    quotient = a // b
    remainder = a % b
    x = x_set[index - 2] - quotient * x_set[index - 1]
    y = y_set[index - 2] - quotient * y_set[index - 1]

    if remainder == gcd(a, b):
        return x, y
    else:
        index += 1
        x_set.append(x)
        y_set.append(y)
        return extended_euclidean_algorithm(b, remainder, index)
