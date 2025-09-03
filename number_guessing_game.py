import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = 0

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number!")

# Run the game
number_guessing_game()
