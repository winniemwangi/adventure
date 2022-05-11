name = input ("Type your name...")
print("Welcome", name, "to the adventure!!")

output = input("You are on the dark road, you can turn left or right (left/right)")

if output == "left":
    output = input("You have reachead to a river. You can swim or walk around it. (swim/walk)")

    if output == "swim":
        print("Didn't pass the river because you were eaten by a hippo")

    elif output == "walk":
        print("You passed out because you walked a long distance")

    else:
        print("Not a valid option. You lose!")

elif output == "right":
    output = input("You reached to the bridge and it dangerous you can go back or cross it.(back/cross)")

    if output == "cross":
        output == input("You cross and meet a stranger. Will you talk to him (yes/no)")

        if output == "yes":
            print("You talked to the stranger and they gave you a gold. You win!!")

        elif output == "no":
            print("You ignore the stranger and they get offended. You lose")

        else:
            print("Not a valid option. You lose!")

    elif output == "back":
        print("Don't wanna try. You lose hahaa!")

    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option")       

print("Thank you", name, "for taking an adventure with us yeppy!")