menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}

def check(order):
    try:
        print(f"Your total is {menu[order]}")
    except KeyError:
        print("That item is not on the menu.")
        
check('drip')       # Your total is 1.95
check('tea')        # That item is not on the menu.