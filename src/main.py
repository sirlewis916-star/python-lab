from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        num = float(input("Enter a number: "))
        print(f"Square of {num} is: {square(num)}")
        if is_even(int(num)):
            print(f"{int(num)} is even.")
        else:
            print(f"{int(num)} is odd.")
        print(f"{num}°C is {celsius_to_fahrenheit(num)}°F")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    