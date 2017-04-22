from string import Template

class MyTemplate(Template):
    delimiter = '#'


def Cart():

    cart = []
    num = 0
    numberItems = int(input("How many items do you want to buy? "))
    for x in range(0,numberItems):
        items = str(input("Enter product's name : "))
        prices = float(input("Enter product's price $: "))
        qtys = int(input("Enter quantity : "))

    #     cart.append(dict(item=items, price=prices, qty=qtys))
       
    #     # for k in cart.keys():
    #     #     print(k," -> ",cart[k])

        cart.append(dict(item=items.capitalize(), price=prices, qty=qtys, sum=prices*qtys))
    # cart.append(dict(item="Cake", price=12, qty=1))
    # cart.append(dict(item="Fish", price=32, qty=4))

    t = MyTemplate("#qty x #item ($#price/item) = $#sum")
    total = 0
    print("\nCart: \n")

    for data in cart:
        print(t.substitute(data))
        total += data["sum"]
    print("Total = "+str(total)+"$\n")
    









def main():

    Cart()
    # cart = {"item":"items", "price": 0, "qty":0}
    # for k in cart.keys():
    #     print(k," -> ",cart[k])

if __name__ == '__main__':
    main()