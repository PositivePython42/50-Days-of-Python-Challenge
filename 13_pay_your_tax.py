import emoji

def pay_your_tax():
    while True:
        try:
            nett = (input("Enter the price before VAT is added : "))
            vat = (input("Enter the rate of VAT : "))
            gross = int(nett) + (int(nett) * (int(vat) / 100))
            print(f"The gross price is {gross:.2f}.")
        
        except ValueError:
            print("You'll need to enter numbers please")
            break

pay_your_tax()

def python_snakes(n):
    character = emoji.emojize(":snake:")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print(character, end="")
        print()

size = int(input("How big would you like your pyramid? (1-20) : "))
python_snakes(size)