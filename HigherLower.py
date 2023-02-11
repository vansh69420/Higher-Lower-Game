from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_decr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_decr},from {account_country}"

def check_answer(guess,a_followers,b_followers):
    """Take the user guess and followers counts and return if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    


    
# Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatable.
while game_should_continue:
    # Generate a random acoount from the game_data.

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    # Format the account data into the printable format
    
    
    
    # Ask user a guess
    guess = input("Who has the more followers? Type 'A' or 'B' : ").lower()
    
    # Check if the user is correct.
    ## Get the followers count for each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_account,b_follower_account)

    # Clear the screen between rounds.
    clear()
    print(logo)
    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry you are wrong. Final score: {score}")
    