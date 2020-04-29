def make_pizza(size, *topp):
    print("\nMakeing a " + str(size) + " pizza with the following toppings:")
    for top in topp:
        print("- " + top)