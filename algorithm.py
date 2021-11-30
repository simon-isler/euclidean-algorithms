# euclidean algorithm
def gcd(x, y):
    remainder = x % y

    if y % remainder == 0:
        return remainder
    else:
        return gcd(y, remainder)


# extended euclidean algorithm
# a * x + b * y = gcd(a, b)
x_set = [1, 0]
y_set = [0, 1]


def xk(k, quotient):
    return x_set[k - 2] - quotient * x_set[k - 1]


def yk(k, quotient):
    return y_set[k - 2] - quotient * y_set[k - 1]


def extended_euclidean_algorithm(x, y, index=2):
    quotient = x // y
    remainder = x % y
    a = xk(index, quotient)
    b = yk(index, quotient)

    if remainder == gcd(x, y):
        return a, b
    else:
        index += 1
        x_set.append(a)
        y_set.append(b)
        return extended_euclidean_algorithm(y, remainder, index)
