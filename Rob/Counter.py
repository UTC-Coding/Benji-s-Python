qnt = 0
total = 0

def qst(denomination, value):
    global total
    qnt = input("How many " + denomination + "? ")
    qnt = float(qnt)
    value = float(value)
    subtotal = value * qnt
    total = total + subtotal
    return total

qst("pennies", 0.01)
qst("5 pence pieces", 0.05)
qst("10 pence pieces", 0.1)
qst("20 pence pieces", 0.2)
qst("50 pence pieces", 0.5)
qst("1 pound coins", 1)
qst("2 pound coins", 2)
qst("5 pound coins", 5)

total = str(total)
print("You have: " + total)