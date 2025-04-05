print("Temperature Converter")
temperature_choose = int(input("Convert Celsius in Kelvin 1\nConvert Kelvin in Celsius 2\nPress 1 or 2"+" "))



if temperature_choose == 1: 
    temp = isinstance(temperature_choose, (int, float))
    temperature_celsius = float(input("I will convert Celsius in Kelvin. Please write the temperature in Celsius:\n"))
    temperature_kelvin = 273.15 + temperature_celsius
    print(f"The converted temperature is: {temperature_kelvin}")
elif temperature_choose == 2: 
    temp_kelvin = float(input("I will convert Kelvin in Celsius. Please write the temperature in Kelvin:\n"))
    temperature_celsius1 = temp_kelvin - 273.15
    print(f"The converted temperature is: {temperature_celsius1}")
else:
    print("No correct value, press 1 or 2")


