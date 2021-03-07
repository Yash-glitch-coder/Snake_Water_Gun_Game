import random

user_score = 0
comp_score = 0
count = 0
print("\t\nTHE SNAKE, WATER & GUN GAME!\n")
print("""'RULES':-
SNAKE vs. WATER: SNAKE drinks the WATER hence WINS.
WATER vs. GUN: The GUN will drown in WATER, hence a point for WATER.
GUN vs. SNAKE: GUN will kill the SNAKE and WIN.""")
print("\t\nNOTE:-You have only 5 chances to play!\n")
print("\t\nLet's play...\n")
opt = ["s", "w", "g"]

for i in range(5):
    count += 1
    comp_turn = random.choice(opt)
    user_turn = input("What do you choose?\n'S' -> Snake\n'W' -> Water\n'G' -> Gun\n----->")

    if user_turn == "s" or user_turn == "S":
        if comp_turn == "s":
            print("\nAhhhh...  it's a draw!")
        elif comp_turn == "w":
            user_score += 1
            print("\nYou WIN!")
        else:
            comp_score += 1
            print("\nLoser!!!!\nTry again!")

    elif user_turn == "w" or user_turn == "W":
        if comp_turn == "w":
            print("\nAhhhh...  it's a draw!")
        elif comp_turn == "g":
            user_score += 1
            print("\nYou WIN!")
        else:
            comp_score += 1
            print("\nLoser!!!!\nTry again!")

    elif user_turn == "g" or user_turn == "G":
        if comp_turn == "g":
            print("\nAhhhh...  it's a draw!")
        elif comp_turn == "s":
            user_score += 1
            print("\nYou WIN!")
        else:
            comp_score += 1
            print("\nLoser!!!!\nTry again!")
    else:
        print("Invalid input buddy!\n Try again:\n")

print(" * " * 55)
if comp_score > user_score:
    print("LOSER....GAME OVER....GO HOME!....WATCH CARTOON!")
    print("Your score: " + str(user_score) + "\nMy score: " + str(comp_score))
elif comp_score < user_score:
    print("Ohh....\nShits....\nYou WIN....\nIT WON'T HAPPEN AGAIN, SEE YOU SOON!...\n")
    print("Your score: " + str(user_score) + "\nMy score: " + str(comp_score))
else:
    print("I am Shocked..it's a TIE!\n")
    print("Press 'Ctrl+shift+f10' to play again!")
print(" * " * 55)
