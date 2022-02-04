def multiplierGenerator(multiplier):
    return lambda x: x* multiplier

multiplyby3 = multiplierGenerator(3)
multiplyby2 = multiplierGenerator(2)
print(multiplyby3(4))
print(multiplyby2(3))

choice = input("""Which choice would you like
    Volunteer



""")