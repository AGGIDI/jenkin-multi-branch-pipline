def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        check_odd_even(num)
    except ValueError:
        print("Please enter a valid integer.")
