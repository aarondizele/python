### Interest rate

invest = float(input("Enter amount money to invest: "))
interest_rate = float(input("What's the interest rate: "))

interest_rate = interest_rate * .01

for i in range(10): ### Cycle through 10 years using a 'for' loop and range from 0 to 9
    invest = invest + (invest*interest_rate)
print("Investment after 10 years: {:.2f}".format(invest))