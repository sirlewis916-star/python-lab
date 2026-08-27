from utils import square, is_even, celsius_to_fahrenheit

num = float(input("Enter a number: "))

print(f"Square: {square(num)}")
print(f"Is Even: {is_even(num)} - {'Even' if is_even(num) else 'Odd'}")
print(f"{num}°C in Fahrenheit is {celsius_to_fahrenheit(num)}°F")
