print("Welcome to Treasure Island. \n"
      "Your mission is to find the treasure.")
left_right = (input("Left or Right?\n:")).lower()
swim_wait = (input("Swim or Wait?\n:")).lower()
door = (input("Which door? Red, Blue or Yellow?\n:")).lower()

if left_right == "right":
    print("Game Over")
elif left_right == "left":
    if swim_wait == "swim":
        print("Game Over")
    elif swim_wait == "wait":
        if door == "red" or door == "blue":
            print("Game Over")
        elif door == "yellow":
            print("You win!")
        else:
            print("Your input is not correct")
    else:
        print("Your input is not correct.")
else:
    print("Your input is not correct.")