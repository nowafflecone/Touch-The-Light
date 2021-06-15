# the only ways to get to route 2 is if you say "yes" to door open close, the "no" to go further. The only other way is to say "No" to
# doorOpenClose then say No to keeplooking and then say No to opening the door, and then eventually say yes to opening the door. 
def main():
    print("\t","-"*45)
    print("\t", "--", "                                  ", "     --")
    print("\t", "--", "                                  ", "     --")
    print("\t", "--", "\t\tTouch The Light", " \t    --")
    print("\t", "--", "                                  ", "     --")
    print("\t", "--", "                                  ", "     --")
    print("\t","-"*45)
    
    print("\nYou wake up in a plain white room, the light bright in your eyes.\nAs you look away from the light, you notice a door.")
    doorOpenClose = input("\nDo you open it?(Yes/No): ")
    # route 1
    if doorOpenClose == "Yes":
        print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
        goFurther = input("\nDo you want to go further?(Yes/No): ")
        if goFurther == "Yes": # come back here
            print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
            print("\nYou look up at the sky. \nIt's almost like an ocean of deep purple. \nThere are no clouds. \nThere is no sun.")
            print("Somehow it's still light out, the grass is shiny. \nAs you look around you see a figure off to the side of you.")
            print("\nThe figure approaches slowly.\n")
            print("It seems like a black blob, and as it gets closer, he doesn't get any clearer.")
            dontRun = input("\nDo you run back to the room?(Yes/No): ")
            if dontRun == "Yes":
                print("You run back to the room. \nA feeling of horror overcomes you.\nThe room is filled with darkness.\n")
                print("\t","-"*45)
                print("\t", "--", "                                  ", "     --")
                print("\t", "--", "                                  ", "     --")
                print("\t", "--", "\t\tIt Consumes You", " \t    --")
                print("\t", "--", "                                  ", "     --")
                print("\t", "--", "                                  ", "     --")
                print("\t","-"*45)
                input()                
                
        # route 2
        elif goFurther == "No":
            print("You look back at the light. \nYou get up and try to reach for it. \nYou just barely touch it but you notice its cold.")
            print("As you touch the light, you feel something crumbling in your hand.\n \nYour skin is falling off.\n")
            print("In place of your skin is a black and empty void, \nbut its just your fingertips. \nSo it should be okay.")
            youShould = input("\nYou look back to the door, should you go?(Yes/No): ")
            if youShould == "Yes":
                print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
                print("You flex your, now, half-void hand. It feels like nothing. Like part of you is lost.")
                print("You're kind of glad you didn't stay in there.")
            elif youShould == "No":
                print("\nAs you wait, a piece of your shoulder falls off. \nIt doesn't hurt. Its just empty.\n")
                GOGO = input("Should you go?(Yes/No): ")
                if GOGO == "No":  
                    print("\nYour skin continues to fall off. \nAs you look around, you notice a mirror.")
                    print("You see your reflection, \nyour face is peeling off into the black void.")
                    print("Dread begins to fill you as your skin falls off.\n")
                    doubleGOGO = input("Should you go?(Yes/No): ")
                    if doubleGOGO == "No":
                        print("\nYour skin falls off more rapidly, until you are nothing but dust.")
                        print("The world feels like and endless void of nothing.")
                        print("You feel nothing, and you are nothing.")
                        print("You shouldn't have touched the light.")
                        input()
                elif GOGO == "Yes": 
                    print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
            
            
            
    elif doorOpenClose == "No": # route 1
        print("\nYou look back at the room, it has nothing on the walls. \nNo pictures, no nothing.")
        keepLooking = input("\nDo you want to keep looking?(Yes/No): ")
        if keepLooking == "No":
            openDoor = input("\nDo you want to go open the door?(Yes/No): ")
            if openDoor == "Yes":
                print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                goFurther = input("\nDo you want to go further?(Yes/No): ")
                if goFurther == "Yes":
                    print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                 
            while openDoor == "No":
                print("There is still nothing on the walls.")
                keepLooking3 = input("\nDo you want to keep looking?(Yes/No): ")
                if keepLooking3 == "No":
                    openDoor2 = input("\nDo you want to go open the door?(Yes/No): ")
                    if openDoor2 == "Yes":
                        print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                        goFurther3 = input("\nDo you want to go further?(Yes/No): ")
                        if goFurther3 == "Yes": # come back here
                            print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                                     
                        
                        elif goFurther3 == "No": # alt route 2
                            print("You look back at the light. \nYou get up and try to reach for it. \nYou just barely touch it but you notice its cold.")
                            print("As you touch the light, you feel something crumbling in your hand.\n \nYour skin is falling off.\n")
                            print("In place of your skin is a black and empty void, \nbut its just your fingertips. \nSo it should be okay.")
                            youShould = input("\nYou look back to the door, should you go?(Yes/No): ")
                            if youShould == "Yes":
                                print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
                                print("You flex your, now, half-void hand. It feels like nothing. Like part of you is lost.")
                            elif youShould == "No":
                                print("")
                                print("As you wait, a piece of your shoulder falls off. \nIt doesn't hurt. Its just empty.")
                                GOGO = input("Should you go?(Yes/No): ")
                                if GOGO == "No":  # come back here
                                    print("\nYour skin continues to fall off.\nAs you look around, you notice a mirror.")
                                    print("You see your reflection, \nyour face is peeling off into the black void.")
                                    print("Dread begins to fill you as your skin falls off.")
                                    doubleGOGO = str(input("Should you go?(Yes/No): "))
                                    if doubleGOGO == "No":
                                        print("Your body deteriorates, until you are nothing but dust.")
                                        print("\t","-"*45)
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t", "--", "\t\tYou Shouldn't Have Touched", " \t    --")
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t","-"*45)
                                        input()
                                    elif doubleGOGO == "Yes":                                            
                                        print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?\nYour body aches like nothing you've ever \nfelt before. ")
                                elif GOGO == "Yes":  # come back here
                                    print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?\nYour body aches like nothing you've ever \nfelt before.")
                                                    
                
        
        elif keepLooking == "Yes": # route 1
            print("There is still nothing on the walls.")
            keepLooking2 = input("\nDo you want to keep looking?(Yes/No): ")
            if keepLooking2 == "No":
                openDoor = input("\nDo you want to go open the door?(Yes/No): ")
                if openDoor == "Yes":
                    print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                    goFurther = input("\nDo you want to go further?(Yes/No): ")
                    if goFurther == "Yes":
                        print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                                      
                elif openDoor == "No":
                    print("There is still nothing on the walls.")
                    keepLooking2 = input("\nDo you want to keep looking?(Yes/No): ")
                    if keepLooking2 == "No":
                        openDoor = input("\nDo you want to go open the door?(Yes/No): ")
                        while openDoor == "No":
                            print("There is still nothing on the walls.")
                            keepLooking3 = input("\nDo you want to keep looking?(Yes/No): ")
                            if keepLooking3 == "No":
                                print("A darkness fills your lungs. \nYou feel as if you can't breathe.")
                                print("\t","-"*45)
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "\tYou Shouldn't Have Waited", " \t    --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t","-"*45)
                                input()
                        if openDoor == "Yes":
                            print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                            goFurther = input("\nDo you want to go further?(Yes/No): ")
                            if goFurther == "No":
                                print("There is still nothing on the walls.")
                                goFurther2 = input("\nDo you want to go further?(Yes/No): ")
                                if goFurther2 == "No":
                                    print("A darkness fills your lungs. \nYou feel as if you can't breathe.")
                                    print("\t","-"*45)
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t", "--", "\tYou Shouldn't Have Waited", " \t    --")
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t","-"*45)
                                    input()                                    
                                if goFurther2 == "Yes":
                                    print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                            
                            if goFurther == "Yes":  # come back here
                                print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                            
            
            while keepLooking2 != "Yes": # route 1
                print("There is still nothing on the walls.")
                keepLooking2 = input("\nDo you want to keep looking?(Yes/No): ")
                if keepLooking2 == "No":
                    openDoor = input("\nDo you want to go open the door?(Yes/No): ")
                    while openDoor == "No": 
                        print("There is still nothing on the walls.")
                        openDoor2 = input("\nDo you want to go open the door?(Yes/No): ")
                        if openDoor2 == "Yes":
                            print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                            goFurther = input("\nDo you want to go further?(Yes/No): ")
                            if goFurther == "No": 
                                print("A darkness fills your lungs. \nYou feel as if you can't breathe.")
                                print("\t","-"*45)
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "\tYou Shouldn't Have Waited", " \t    --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t","-"*45)
                                input()                                                                    
                            if goFurther == "Yes":  # come back here
                                print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                                     
                            
        
        
main()