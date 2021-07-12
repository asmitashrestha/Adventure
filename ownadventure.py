name= input("Enter your name :")
print("welcome",name, "to this adventure!!")

answer =input("You are on a dirt road, it has come to an end and you can go right,left or straight.Which way would you like to go(right/left/straight)?").lower()

if answer=="right":
    answer=input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across:")

    if answer=="swim":
        print("You swam across and were eaten by an crocodile.")
   
    elif answer=="walk":
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print("Enter a valid option.You loose the game!!")

elif answer=="left":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)?")

    if answer=="back":
        print("You go back and loose!!")

    elif answer=="cross":
        answer=input("You cross the bridge and meet a stranger.Do you talk to them(yes/no) ?")

        if answer=="yes":
            print("You talk to stranger and they gave you $1000.You WIN!!")

        elif answer=="no":
            print("You ignore the stranger and they are offended and you lose!!")

        else:
             print("Enter a valid option.You lose!!")

    else:
         print("Enter a valid option. You lose!!")        

elif answer=="straight":
     answer==input("You come to a top of a hills,it looks difficult,do you want to reach at the top of the hills or return back(reach/back)?")

     if answer=="back":
         print("You go back and lose game !!")

     elif answer=="go":
          answer==input("You reach at the top of the hills and found horse.Do you want to take with you(yeah/nah)?")

          if answer=="yeah":
              print("Horse was a magical and you become rich.You win!!")

          elif answer=="nah":
               print("You lose the game!!")

          else:
               print("Enter a valid option.You lose game!!")
     else:
          print("Enter a valid option.You lose game!!")

else:
    print("Enter a valid option.You lose game!!")

print("Thank you",name,"for trying this adventure!!")                                                                    