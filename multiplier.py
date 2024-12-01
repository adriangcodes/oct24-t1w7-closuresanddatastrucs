def multiply(multiplier):
    return lambda x: x * multiplier

doubler = multiply(2)
tripler = multiply(3)

print(doubler(10))
print(tripler(5))


def adrian(num, multi):
    return num * multi

print(adrian(2, 4))

