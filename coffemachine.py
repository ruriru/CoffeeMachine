constant = 0
water_quantity = 400
milk_quantity = 540
coffee_quantity = 120
cups_quantity = 9
money = 550

def chk_espresso():
    global water_quantity, milk_quantity, coffee_quantity, cups_quantity
    #capacity = min(water_quantity // 250, coffee_quantity // 16)
    if water_quantity >= 250 and coffee_quantity >= 16 and milk_quantity > 0:
        print("I have enough resources, making you a coffee!")
        espresso()
    elif water_quantity < 250 and coffee_quantity < 16 and milk_quantity <= 0:
        print("Sorry, not enough water and coffee beans!")
    elif water_quantity < 250:
        print("Sorry, not enough water!")
    elif coffee_quantity < 16:
        print("Sorry, not enough coffee beans!")
        
def chk_latte():
    global water_quantity, milk_quantity, coffee_quantity, cups_quantity
    #capacity = min(water_quantity // 350, milk_quantity // 75, coffee_quantity // 20)
    if water_quantity >= 350 and milk_quantity >= 75 and coffee_quantity >= 20:
        print("I have enough resources, making you a coffee!")
        latte()
    elif water_quantity < 350 and milk_quantity < 75 and coffee_quantity < 20:
        print("Sorry, not enough water, milk and coffee beans!")
    elif water_quantity < 350 and milk_quantity < 75:
        print("Sorry, not enough water and milk!")
    elif milk_quantity < 75 and coffee_quantity < 20:
        print("Sorry, not enough milk and coffee beans!")
    elif water_quantity < 350 and coffee_quantity < 20:
        print("Sorry, not enough water and coffee beans!")
    elif water_quantity < 350:
        print("Sorry, not enough water!")
    elif milk_quantity < 75:
        print("Sorry, not enough milk!")
    elif coffee_quantity < 20:
        print("Sorry, not enough coffee beans!")

def chk_cappuccino():
    global water_quantity, milk_quantity, coffee_quantity, cups_quantity
    #capacity = min(water_quantity // 200, milk_quantity // 100, coffee_quantity // 12)
    if water_quantity >= 200 and milk_quantity >= 100 and coffee_quantity >= 12:
        print("I have enough resources, making you a coffee!")
        cappuccino()
    elif water_quantity < 200 and milk_quantity < 100 and coffee_quantity < 12:
        print("Sorry, not enough water, milk and coffee beans!")
    elif water_quantity < 200 and milk_quantity < 100:
        print("Sorry, not enough water and milk!")
    elif milk_quantity < 100 and coffee_quantity < 12:
        print("Sorry, not enough milk and coffee beans!")
    elif water_quantity < 200 and coffee_quantity < 12:
        print("Sorry, not enough water and coffee beans!")
    elif water_quantity < 200:
        print("Sorry, not enough water!")
    elif milk_quantity < 100:
        print("Sorry, not enough milk!")
    elif coffee_quantity < 12:
        print("Sorry, not enough coffee beans!")

"""
machine performs three basic operations
1) 'buy' means dispensing coffee
2) 'fill' means fill up raw material
3) 'take' means collect money from machine
"""
# this function will print the current status of the coffee machine
def status():
    global money, water_quantity, milk_quantity, coffee_quantity, cups_quantity
    print("\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} disposable cups\n{} of money".format(water_quantity,milk_quantity,coffee_quantity,cups_quantity,money))
    
def mode_select():
    global constant
    select = input("Write action ('buy', 'fill', 'take', 'remaining', or 'exit'): ")
    if select == 'buy':
        buy()
    elif select == 'fill':
        fill()
    elif select == 'take':
        take()
    elif select == 'remaining':
        status()
    elif select == 'exit':
        constant += 1

def buy():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choice == '1':
        chk_espresso()
    elif choice == '2':
        chk_latte()
    elif choice == '3':
        chk_cappuccino()
    elif choice == 'back':
        mode_select()
        
def espresso():
    global money, water_quantity, milk_quantity, coffee_quantity, cups_quantity
    # for one cup of 'espresso' requires 250ml of water, and 16gram of coffee beans
    # it costs $ 4
    water_quantity -= 250
    coffee_quantity -= 16
    cups_quantity -= 1
    money += 4
    # print("Enjoy your Expresso!\n")

def latte():
    global money, water_quantity, milk_quantity, coffee_quantity, cups_quantity
    # for one cup of 'espresso' requires 350ml of water, 75ml of milk and 20gram of coffee beans
    # it costs $ 7
    water_quantity -= 350
    milk_quantity -= 75
    coffee_quantity -= 20
    cups_quantity -= 1
    money += 7
    # print("Enjoy your Latte!\n")

def cappuccino():
    global money, water_quantity, milk_quantity, coffee_quantity, cups_quantity
    # for one cup of 'espresso' requires 200ml of water, 100ml of milk and 12gram of coffee beans
    # it costs $ 6
    water_quantity -= 200
    milk_quantity -= 100
    coffee_quantity -= 12
    cups_quantity -= 1
    money += 6
    # print("Enjoy your Cappuccino!\n")
    
def fill():
    global water_quantity, milk_quantity, coffee_quantity, cups_quantity
    water_in = int(input("Write how many ml of water do you want to add: "))
    milk_in = int(input("Write how many ml of milk do you want to add: "))
    coffee_in = int(input("Write how many grams of coffee beans do you want to add: "))
    cups_in = int(input("Write how many disposable cups do you want to add: "))
    water_quantity += water_in
    milk_quantity += milk_in
    coffee_quantity += coffee_in
    cups_quantity +=  cups_in

def take():
    global money
    print("I gave you $", money)
    money = 0

while constant == 0:
    mode_select()