from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
cond=True
option = menu.get_items()
while cond ==True:
    choice=input(f"What would you like to have? {option}: ")
    if choice == "off":
        cond=False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink)==True:
          if money.make_payment(drink.cost)==True:
            coffee.make_coffee(drink)


