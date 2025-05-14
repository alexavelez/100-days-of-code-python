menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

# TODO 2: Print report
def report(resources, money):
    for item, amount in resources.items():
        unit = "ml" if item != "coffee" else "g"
        print(f"{item.capitalize()}: {amount} {unit}")
    print(f"Money: ${money}")

# TODO 3: Check resources

def check_resources(drink, resources, menu):
    for item, amount_needed in menu[drink]["ingredients"].items():
        if resources.get(item, 0) < amount_needed:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True

# TODO 4: Prompt user to insert coins and evaluate quantity inserted
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


# TODO 5 check transaction successful

def transaction_successful(drink, menu, user_money):
    cost = menu[drink]["cost"]
    if user_money >= cost:
        change = user_money - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True, cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0

# TODO 6 Deduct resources used to make the coffee
def deduct_resources(drink, resources, menu):
    for item, amount_needed in menu[drink]["ingredients"].items():
        resources[item] -= amount_needed

# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):” or print report / turn off
machine_on = True

while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        machine_on = False
        print("Turning off the coffee machine. Goodbye!")
    elif user_input == "report":
        report(resources, money)
    elif user_input in menu:
        if check_resources(user_input, resources, menu):
            user_money = process_coins()
            transaction_ok, profit = transaction_successful(user_input, menu, user_money)
            if transaction_ok:
                money += profit
                deduct_resources(user_input, resources, menu)
                print(f"Here is your {user_input} ☕, enjoy!")
    else:
        print("Invalid selection.")
