import random, math

random_numbers = []

def odd_and_even(input_list):
    odd_numbers = []
    even_numbers = []
    for element in input_list:
        if element % 2 == 0:
            even_numbers.append(element)
        elif element % 2 != 0:
            odd_numbers.append(element)
    
    sorted_even_numbers = sorted(even_numbers, reverse=True)
    sorted_odd_numbers = sorted(odd_numbers)
    
    print(f"The sorted even numbers are : {sorted_even_numbers}.")
    print(f"The sorted odd numbers are  : {sorted_odd_numbers}.")

    return sorted_even_numbers[0] - sorted_odd_numbers[0]

def prime_numbers(test):
    prime_number_list = []
    for element in range(1, test):
        if is_prime(element) is True:
            prime_number_list.append(element)
    return prime_number_list

def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    
    # 2 and 3 are prime numbers
    if number <= 3:
        return True
    
    # Numbers divisible by 2 or 3 are not prime
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Check for prime numbers using 6k ± 1 rule
    # All prime numbers greater than 3 can be written in the form 6k ± 1.
    # We only need to check divisors up to sqrt(number).
    sqrt_num = int(math.sqrt(number))
    for i in range(5, sqrt_num + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
        
    return True

# Generate 20 random numbers and append them to the list
for _ in range(20):
    random_number = random.randint(1, 100)
    random_numbers.append(random_number)
print(f"The list of random numbers is : {random_numbers}.")
print(f"The difference between the largest even number and smallest odd number is : {odd_and_even(random_numbers)}.")

test_number =  int(input("\nEnter an integer and I will give the prime numbers from 1 to your number : "))
print(f"The prime numbers in the range from 1 to {test_number} are : {prime_numbers(test_number)}.")