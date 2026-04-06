import random

while True:
    print("Game started")
    num = random.randint(1, 10)
    attempt = 0
    max_attempt = 5

    print("You have only 5 attempts")

    while attempt < max_attempt:
        guess = int(input("Guess a number: "))
        attempt += 1

        if guess == num:
            print("Correct")
            print("You have guessed it in",attempt,"attempt")
        elif guess > num:
            print("Too High")
        else:
            print("Too Low")

    else:
        print("Sorry ! You have lost this game")
        print("The number was", num)

    choice = input("Do you want to play again? (yes/no): ")

    if choice == "no":
        break