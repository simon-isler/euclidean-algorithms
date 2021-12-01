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


def extended_euclidean_algorithm(x, y, index=2):
    quotient = x // y
    remainder = x % y
    a = x_set[index - 2] - quotient * x_set[index - 1]
    b = y_set[index - 2] - quotient * y_set[index - 1]

    if remainder == gcd(x, y):
        return a, b
    else:
        index += 1
        x_set.append(a)
        y_set.append(b)
        return extended_euclidean_algorithm(y, remainder, index)
