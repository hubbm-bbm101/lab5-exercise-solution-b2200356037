import random
random_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Increase your number.")
    elif guess > random_number:
        print("Decrease your number.")
    else:
        print("You guessed the number!")
        break