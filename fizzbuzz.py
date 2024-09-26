import random

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

def player1():
    random_num = random.randint(1, 100)
    correct_answer = fizzbuzz(random_num)
    print(f"Number is: {random_num}")
    user_input = input("What's the answer (Fizz,buzz, Fizzbuzz, or the num itself)? ").lower()

    if user_input == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong answer! It should be{correct_answer}")
        return False

print()
print("---Fizz Buzz Game--")

while True:
    choice = input("\nPress Enter to play or type 'exit' to quit: ").lower()

    if choice == "exit":
        print("Thanks for playing!")
        break
    else:
        if not player1():
            break
