customers = []
while True:
    entry = str(input("Enter Customer (Yes/No) : "))
    entry = entry[0].lower()

    if (entry == 'n'):
        break
    else:
        fname, lname = str(input("Enter customer name : ")).split()
        customers.append({'fname':fname, 'lname':lname})

for cus in customers:
    print(cus['fname'], cus['lname'])