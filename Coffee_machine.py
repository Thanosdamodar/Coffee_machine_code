MENU = {
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

profit = 0

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
  for items in order_ingredients:
      if order_ingredients[items] >= resources[items]:
          print(f"Sorry there is not enough {items}")
          return False
  return True


def process_coins():
  print("Please insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickels?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total


def is_transaction_successful(money_received, drink_cost):
  if money_received >= drink_cost:
      change = round(money_received - drink_cost, 2)
      print(f"Here's ${change} in change.")
      global profit
      profit += money_received
      return True
  elif money_received <= drink_cost:
      print("Sorry that's not enough money. Money Refunded")
      return False


def make_coffee(drink_name, order_ingredients):
  for i in order_ingredients:
      resources[i] -= order_ingredients[i]
  print(f"Here is your {drink_name}.☕")


is_on = True

while is_on:
  order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
  if order == "off":
      is_on = False

  elif order == "report":
      print(f"Water : {resources["water"]}ml")
      print(f"Milk : {resources["milk"]}ml")
      print(f"Coffee : {resources["coffee"]}gm")
      print(f"Money : ${profit}")

  else:
      drink = MENU[order]
      print(f"Cost :- ${drink['cost']}")
      if is_resource_sufficient(drink["ingredients"]):
          payment = process_coins()
          if is_transaction_successful(payment, drink["cost"]):
              make_coffee(order, drink["ingredients"])
