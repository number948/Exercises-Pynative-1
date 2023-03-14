def calculateIncomeTax():
    income = 45000
    tax = 0

    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax += 10000 * (10/100)
        income = income - tax
    else:
        tax += 25000 * (20/100)
        income = income - tax

        print(tax)

calculateIncomeTax()