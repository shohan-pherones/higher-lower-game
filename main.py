import random

data = [
    {"name": "Instagram", "description": "Social media platform", "followers": 346},
    {"name": "Cristiano Ronaldo", "description": "Footballer", "followers": 215},
    {"name": "Dwayne Johnson", "description": "Actor and former wrestler", "followers": 187},
    {"name": "Kylie Jenner", "description": "Reality TV star and businesswoman", "followers": 222},
]

def get_random_account():
    return random.choice(data)

def check_answer(guess, account_a, account_b):
    if account_a["followers"] > account_b["followers"]:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Ensure accounts are unique
        while account_a == account_b:
            account_b = get_random_account()

        # Display the two accounts
        print(f"Compare A: {account_a['name']}, a {account_a['description']}.")
        print(f"Against B: {account_b['name']}, a {account_b['description']}.")

        # Player guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if the player's guess is correct
        is_correct = check_answer(guess, account_a, account_b)

        # Feedback and score keeping
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            # Set account_a to the winner for the next round and choose a new account_b
            account_a = account_b
            account_b = get_random_account()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

def main():
    print("Welcome to the Higher Lower Game!")
    while input("Do you want to play? Type 'yes' or 'no': ").lower() == "yes":
        play_game()
    print("Thanks for playing!")

main()