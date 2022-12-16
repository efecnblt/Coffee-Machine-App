import os
from prettytable import PrettyTable

menu = [
    {"Name": "Espresso",
     "Water": 50,
     "Coffee" : 18,
     "Milk": 0,
     "Price": 1.50},
    {"Name": "Latte",
     "Water": 200,
     "Coffee" : 24,
     "Milk": 150,
     "Price": 2.50},
    {"Name": "Cappuccino",
     "Water": 250,
     "Coffee" : 24,
     "Milk": 100,
     "Price": 3.00}
]

water = 1000
milk = 2000
coffee = 1000
money = 0
table = PrettyTable()

def report():
    global table
    table.clear()
    table.add_column("MENU", [f"Water: {water}ml", f"Milk: {milk}ml", f"Coffee: {coffee}gr", f"Money: ${money}"])
    print(table)


def check_tank(check_water, check_coffee, check_milk):
    global water, milk, coffee
    if check_water > water:
        print("Sorry there is not enough water.")
        return False
    elif check_coffee > coffee:
        print("Sorry there is not enough water.")
        return False
    elif check_milk > milk:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: $"))
    dimes = int(input("How many dimes?: $"))
    nickles = int(input("How many nickles?: $"))
    pennies = int(input("How many pennies?: $"))
    total = round(quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01, 2)
    return total


def check_coins(exchange, water2, coffee2, milk2):
    global water, coffee, money, milk

    water -= water2
    coffee -= coffee2
    milk -= milk2
    money += exchange
    coin = insert_coins()
    if coin - exchange < 0:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif coin - exchange == 0:
        return True
    else:
        print(f"\nHere is ${round(coin - exchange, 2)} in change.")
        return True


os.system("clear")


def game():
    while True:
        global water, milk, coffee, money
        caffe_choose = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        if caffe_choose == "report":
            report()
        elif caffe_choose == "espresso":
            if check_tank(50, 18, 0):
                if check_coins(1.50, 50, 18, 0):
                    print(f"Here is your Espresso. \U00002615 Enjoy!")

        elif caffe_choose == "latte":
            if check_tank(200, 24, 150):
                if check_coins(2.50, 200, 24, 150):
                    print(f"Here is your Latte. \U00002615 Enjoy!")

        elif caffe_choose == "cappuccino":
            if check_tank(250, 24, 100):
                if check_coins(3.00, 250, 24, 100):
                    print(f"Here is your Cappuccino. \U00002615 Enjoy!")

        elif caffe_choose == "off":
            break
        else:
            print("Please enter valid syntax.")
            game()


game()
