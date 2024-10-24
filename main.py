from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

coffee_machine_is_ON = True

while coffee_machine_is_ON:

    user_selection = input(f"What would you like? {Menu.get_items()}: ").lower()

    if user_selection == "off":

        print("Coffee machine has been switched off. Goodbye.")

        coffee_machine_is_ON = False

    elif user_selection == 'report':

        CoffeeMaker.report()

    elif user_selection == 'espresso' or user_selection == 'latte' or user_selection == 'cappuccino':

        user_drink = Menu.find_drink(user_selection)

        if user_drink in Menu.menu:

            if CoffeeMaker.is_resource_sufficient(user_drink):

                transaction_is_successful = MoneyMachine.make_payment(user_drink.cost)

                MoneyMachine.report()

                if transaction_is_successful:

                    CoffeeMaker.make_coffee(user_drink)

                else:

                    coffee_machine_is_ON = False

            else:

                coffee_machine_is_ON = False

        else:

            coffee_machine_is_ON = False
