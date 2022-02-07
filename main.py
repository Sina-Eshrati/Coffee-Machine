from data import MENU
from data import resources

continue_process = True
is_on = True


def check_ingredients(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def get_money(cost):
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    wallet = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if cost > wallet:
        print("sorry that's not enough money, Money refunded.")
        return False
    else:
        change = wallet - cost
        print(f"Here is your change ${change}")
        resources['money'] += cost
        return True


def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice}☕. Enjoy!")


while is_on:
    choice = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif choice == 'off':
        is_on = False
        print("Coffee Machine is turned off.")
    else:
        continue_process = check_ingredients(MENU[choice]['ingredients'])
        if continue_process:
            continue_process = get_money(MENU[choice]['cost'])
            if continue_process:
                make_coffee(MENU[choice]['ingredients'])
