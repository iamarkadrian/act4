char = input("Enter a character: ")
height = int(input("Enter the maximum peak of the triangle: "))

for i in range(1, height + 1):
    spaces = height - i
    stars = 2 * i - 1
    print(' ' * spaces + char * stars)