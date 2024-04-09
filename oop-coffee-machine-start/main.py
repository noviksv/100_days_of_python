from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




if __name__ =='__main__':
    coffee_machine = CoffeeMaker()
    #coffee_machine.report() 
    menu = Menu()
    money_machine = MoneyMachine()
    while True:
        print(f"What would you like? ({menu.get_items()})")
        input_order = str(input())
        if input_order == 'report':
            coffee_machine.report()
            money_machine.report()
        elif input_order == 'off':
            break
        else:
            order = menu.find_drink(input_order)
            if order:
                if coffee_machine.is_resource_sufficient(order):
                    if money_machine.make_payment(order.cost):
                        coffee_machine.make_coffee(order)

