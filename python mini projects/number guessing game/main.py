import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the secret number between 1 and 100 (or type 'exit' to quit): "))
    
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number!")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")