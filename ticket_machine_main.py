 # simulate the arrival of a new client for cosmotics

def cosmotics():
    number1 = 1
    number2 = 0
    while True:
        yield number1
        number1, number2 = number1 + 1, number2 + 1

# simulate the arrival of a new client for perfume
def perfume():
    number1 = 1
    number2 = 0
    while True:
        yield number1
        number1, number2 = number1 + 1, number2 + 1

# simulate the arrival of a new client for pharmacy
def pharmacy():
    number1 = 1
    number2 = 0
    while True:
        yield number1
        number1, number2 = number1 + 1, number2 + 1
























