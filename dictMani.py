from operator import itemgetter

cart = [{"name":"hamburger","price":5,"quantity":1,"totalprice":3},{"name":"sushi","price":5,"quantity":1,"totalprice":7},{"name":"pizza","price":5,"quantity":1,"totalprice":1}]
cartTest = {"hamburger":{"price":5.00,"quantity":1,"totalprice":5.00}}
gameState = True

def Start():
    global cart, gameState

    while gameState:
        print("\nWelcome to Generic E-Commerce Store!\nWhich of the following would you like to do?")

        possibleCommands = ["Add Item","Update Item", "Delete Item", "Display Items by Name", "Display Items by Total Price", "Quit"]
        for i in range(len(possibleCommands)):
            print(f"{i+1}: {possibleCommands[i]}")
        
        userChoice = input()
        if userChoice == "1":
            AddItem()
        elif userChoice == "2":
            UpdateItem()
        elif userChoice =="3":
            DeleteItem()
        elif userChoice =="4":
            DisplayItems("name")
            input("Enter to continue...")
        elif userChoice =="5":
            DisplayItems("TotalPrice")
            input("Enter to continue...")
        elif userChoice =="6":
            Completion()
        else:
            input("Unknown Input. Try again.\nEnter to continue...")

def AddItem():
    name = str(input("Enter the name of the item to add: ").lower())
    price = float(input(f"Enter the price of {name}: $"))
    quantity = int(input(f"Enter the quantity of {name}: "))
    totalPrice = price*quantity
    cart.append({"name":name, "price":price, "quantity":quantity, "totalprice":totalPrice})

def DeleteItem():
    DisplayItems("name")
    name = input("Enter the name of the item you would like to remove: ")
    itemKicked = 0
    for i in range(len(cart)-1):
        if cart[i]["name"] == name:
            cart.pop(i)
            itemKicked = itemKicked+1
    if itemKicked>=1:
        print(f"'{name}' was removed from the shopping cart.")
    else:
        print(f"No item called '{name}' was found.")
    input("Enter to continue...")

def UpdateItem():
    DisplayItems("name")
    name = input("Enter the name of the item that you want to update: ")
    existence=False
    for i in range(len(cart)):
        if cart[i]["name"] == name:
            existence = True
            print(f"Current attributes:\nName: {cart[i]['name']}\nPrice: {cart[i]['price']:.2f}\nQuantity: {cart[i]['quantity']}")
            correction = input("What value would you like to change? ").lower().rstrip()
            if correction in ['name']:
                cart[i][correction] = input(f"replace {correction}:'{cart[i][correction]}' with: ")
            elif correction in ['price','quantity']:
                if correction in ['price']:
                    cart[i][correction] = float(input(f"replace {correction}:'{cart[i][correction]}' with: $"))
                elif correction in ['quantity']:
                    cart[i][correction] = int(input(f"replace {correction}:'{cart[i][correction]}' with: "))
                cart[i]['totalprice'] = cart[i]['quantity']*cart[i]['price']
            else:
                print("Attribute unknown.")
    
    if existence == False:
        input(f"Item '{name}' does not exist.\nEnter to continue...")

def DisplayItems(standard):
    print()
    if standard =="name":
        sortedList = sorted(cart, key=itemgetter('name'))             
    elif standard =="TotalPrice":
        sortedList = sorted(cart, key=itemgetter('totalprice'), reverse=True)

    for i in range(len(sortedList)):
        name,price,quantity,totalPrice = sortedList[i]['name'], sortedList[i]['price'], sortedList[i]['quantity'], sortedList[i]['totalprice']
        print(f"Item {i+1}: '{name}' ({quantity} at ${price:.2f}): ${totalPrice:.2f}") # ERROR

def Completion():
    global gameState
    print("FINAL DATA DUMP:\n", cart)
    gameState = False


Start()