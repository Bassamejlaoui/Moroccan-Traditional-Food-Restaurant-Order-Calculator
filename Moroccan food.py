foods = {
    "Couscous": 4.25,
    "Rfissa": 7.50,
    "Tajin Kefta": 8.50,
    "Tajin Djjaj": 11.00,
    "Pastilla": 8.50,
    "Mrouzia": 8.50,
    "Harira": 9.50,
    "Merguez": 3.00,
    "Maaqouda": 8.00
}

total_cost = 0

while True:
    try:
        item = input("Enter the Moroccan dish you'd like to order: ").title().strip()
        # No need to check if item in foods. KeyError is handled separately.
        total_cost += foods.get(item, 0)
        print(f"Total Cost: ${total_cost:.2f}")
    except EOFError:
        print("\nOrder completed. Enjoy your Moroccan meal!")
        break
    except KeyError:
        print("Sorry, the entered dish is not on the menu. Please try again.")
