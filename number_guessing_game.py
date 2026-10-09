import random


def display_menu():
    print("\n" + "=" * 30)
    print("   NUMBER GUESSING GAME")
    print("=" * 30)
    print("1. Play Game")
    print("2. View Leaderboard")
    print("3. Quit")
    return input("Select an option (1-3): ").strip()


def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Out of bounds! Please enter a number between 1 and 100.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number, not text.\n")


def play_game(leaderboard):
    print("\n--- New Game ---")
    name = input("Enter your name: ").strip()
    if not name:
        name = "Player1"

    number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = get_valid_guess()
        attempts += 1

        if user_guess == number:
            print(f"\nCorrect! You guessed the number in {attempts} attempts.")
            if name not in leaderboard or attempts < leaderboard[name]:
                print("*** New personal best! ***")
                leaderboard[name] = attempts
            break
        elif user_guess < number:
            print("Guess higher!\n")
        else:
            print("Guess lower!\n")


def display_leaderboard(leaderboard):
    print("\n" + "-" * 30)
    print("          LEADERBOARD")
    print("-" * 30)
    if not leaderboard:
        print("No scores yet. Be the first to play!")
    else:
        sorted_board = sorted(leaderboard.items(), key=lambda item: item[1])
        print(f"{'Player Name':<15} | {'Best Score'}")
        print("-" * 30)
        for player, score in sorted_board:
            print(f"{player:<15} | {score} attempts")


def main():
    leaderboard = {}

    while True:
        choice = display_menu()

        if choice == "1":
            play_game(leaderboard)
        elif choice == "2":
            display_leaderboard(leaderboard)
        elif choice == "3":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

    main()
