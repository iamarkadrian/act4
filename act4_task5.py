temp_input = input("Enter the temperature value: ")

if temp_input.replace('.', '', 1).isdigit():
    temperature = float(temp_input)
    direction = input("Convert to (C)elsius or (F)ahrenheit? ").lower()
    
    if direction == 'c' or direction == 'celsius':
        fahrenheit = (temperature * 9/5) + 32
        print(f"{temperature}°C is {fahrenheit:.2f}°F.")
    elif direction == 'f' or direction == 'fahrenheit':
        celsius = (temperature - 32) * 5/9
        print(f"{temperature}°F is {celsius:.2f}°C.")
    else:
        print("Invalid conversion choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("Invalid temperature value. Please enter a numeric value.")