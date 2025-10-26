import random
def guess_game():
    min_num = int(input("Enter min number: "))
    max_num = int(input("Enter max number: "))

    if min_num > max_num:
        print(" Minimum number can't be greater than maximum! Please try again.")
        return guess_game()  

    random_num = random.randint(min_num, max_num)

    
    hint = input("Do you want a hint? (Enter Yes or No): ").lower()
    if hint == "no":
        print("Okay, continue!")
    elif hint == "yes":
        if random_num > max_num / 2:
            print("Your number is greater than half of the max.")
        else:
            print("Your number is less than half of the max.")
    else:
        print("You entered wrong input. You won't get any hint.")

    
    level = input("Enter level (Easy, Medium, Hard): ").lower()
    if level == "easy":
        chances = 5
    elif level == "medium":
        chances = 3
    elif level == "hard":
        chances = 1
    else:
        print("Invalid level! Defaulting to Easy mode.")
        chances = 5

    print(f"You selected {level.capitalize()}. Now you have {chances} chances.")

    while chances > 0:
        user_input = int(input(f"Guess the number between {min_num} and {max_num}: "))
        chances -= 1

        if user_input == random_num:
            print("You Won!")
            break
        elif user_input < random_num:
            print("Too low!")
        else:
            print("Too high!")

        if chances > 0:
            print(f"You have {chances} chances left.")
        else:
            print(f" You lost. The correct number was {random_num}.")


guess_game()
