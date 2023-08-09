n = int(input('Enter variable : '))

def f(x):
    return x**5 + (2 * x**4) + x + 1


def g(x):
    return x**5 + (2 * x**4) + (x**2) - 1


print(f'f({n}) = ',  f(n))
print(f'g({n}) = ',  g(n))
