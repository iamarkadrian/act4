max = int(input("Enter a number: "))
counter = 2
tab = False

while counter <= max:
    if tab:
        print(f"\t{counter}")
    else:
        print(counter)
    tab = not tab
    counter += 2