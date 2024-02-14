from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#MoneyMachine Class.
money_machine = MoneyMachine()
#MoneyMachine Class End.
#CoffeeMaker Class.
coffee_maker = CoffeeMaker()
#CoffeeMaker Class End.
#coffee_maker.report()
#money_machine.report()
#Menu Class.
menu = Menu()
#print(menu.get_items())
#Menu Class End.
#MenuItem Class.
#MenuItem Class End.
###################.
#money_machine.make_payment(cost=menu_item.cost)
##################.
while True:
    input_user=input(f"What would you like? ({menu.get_items()}): ").lower()
    if input_user=="report":
        coffee_maker.report()
        money_machine.report()
    elif input_user=="off":
        break
    else:
        m = menu.find_drink(input_user)
        menu_item = MenuItem(name=m.name,
                             water=m.ingredients["water"],
                             milk=m.ingredients["milk"],
                             coffee=m.ingredients["coffee"],
                             cost=m.cost)
        if coffee_maker.is_resource_sufficient(menu_item):
            money_machine.make_payment(cost=menu_item.cost)
            coffee_maker.make_coffee(menu_item)
###############################################
###############################################








