from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Format the account data into printable data."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def clear():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Display art.
print(logo)
score = 0
game_should_continue = True
account_a = random.choice(data)
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Ensure account_a and account_b are not the same.
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask a user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get the follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds.
    clear()
    print(logo)

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        account_a = account_b
        account_b = random.choice(data)
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")



