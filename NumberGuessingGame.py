import random
num = random.randint(1, 100)
attempts = 0
while True:
    guess = input("Guess a number 1-100: ")
    if not guess.isdigit():
        continue
    guess = int(guess)
    attempts += 1
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print(f"You guessed it in ",attempts," tries!")
        break
