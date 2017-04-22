from string import Template

def Cart():

    cart = []
    num = 0
    numberItems = int(input("How many items do you want to buy? "))
    for x in range(0,numberItems):
        items = str(input("Enter product's name : "))
        prices = float(input("Enter product's price $: "))
        qtys = int(input("Enter quantity : "))

        cart.append(dict(item=items.capitalize(), price=prices, qty=qtys, sum=prices*qtys))

    t = Template("$qty x ${item} ($price/item) = ${sum}")
    total = 0
    print("\nCart: \n")

    for data in cart:
        print(t.substitute(data))
        total += data["sum"]
    print("Total = "+str(total)+"$\n")
    
def main():

    Cart()

if __name__ == '__main__':
    main()