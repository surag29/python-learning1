import random

num = random.randint(1, 10)
tries = 0

while tries < 5:
    guess = int(input("Enter your guess between 1 and 10: "))
    tries += 1  

    if guess == num:
        print(f"🎉 Congratulations! You guessed it right: {num} in {tries} tries!")
        break
    elif guess < num:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
else:
    print(f"Game over! The correct number was {num}.")


