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
    if doorOpenClose.capitalize() == "Yes":
        print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
        goFurther = input("\nDo you want to go further?(Yes/No): ")
        if goFurther.capitalize() == "Yes": # come back here
            print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
            print("\nYou look up at the sky. \nIt's almost like an ocean of deep purple. \nThere are no clouds. \nThere is no sun.")
            print("Somehow it's still light out, the grass is shiny. \nAs you look around you see a figure off to the side of you.")
            print("\nThe figure approaches slowly.\n")
            print("It seems like a black blob, and as it gets closer, he doesn't get any clearer.")
            dontRun = input("\nDo you run back to the room?(Yes/No): ")
            if dontRun.capitalize() == "Yes":
                print("You run back to the room. \nA feeling of horror overcomes you.\nThe room is filled with darkness.\n")
                print("\t","-"*45)
                print("\t", "--", "                                  ", "     --")
                print("\t", "--", "                                  ", "     --")
                print("\t", "--", "\t\tIt Consumes You", " \t    --")
                print("\t", "--", "                                  ", "     --")
                print("\t", "--", "                                  ", "     --")
                print("\t","-"*45)
                input()                
            if dontRun.capitalize() == "No":
                print("The figure gets close to you. \nAs it stands in front of you, you feel a little comfort.")
                print("'OH HELLO. I SEE YOU.'")
                print("*\nHow will you respond?:")
                print("1. 'You see me?'\t\t2.'I didn't realize the blobs could see.'")
                print("3. 'Where am I?'\t\t4. 'Who are you?'")
                choicesSEEN = int(input("Enter a response from above: "))
                while choicesSEEN != 1 or choicesSEEN != 2 or choicesSEEN != 3 or choicesSEEN != 4:
                    print("Please input a number.")
                    choicesSEEN = int(input("Enter a response from above: "))
                    if choicesSEEN == 1:
                        print("\n'OF COURSE I SEE YOU. I HAVE EYES.'")
                        print("From what you could tell, the figure didn't have eyes. But okay?")
                    elif choicesSEEN == 2: 
                        print("\n'I AM NOT A BLOB. I AM JUST LIKE YOU.'")
                        print("You look down at your hands, then back at the figure. Not really.")
                    elif choicesSEEN == 3:
                        print("'YOU ARE IN THE BEYOND. WELCOME TO THE BEYOND'")
                        print("The beyond? Did you die? The figure looks like he wants to keep talking.")
                        print("'IT IS VERY QUIET HERE. UP UNTIL YOU CAME RECENTLY. IT GOT LOUD.'")
                        print("'YOU'VE BEEN IN THAT ROOM FOR WEEKS.'")
                        print("'IT FELT LIKE CENTURIES FOR ME THOUGH.'")
                        print("*\nHow will you respond?:")
                        print("1. 'Weeks? How did I get here?'\t\t\n2.'Did you wait for me?'")
                        centuriesResponse = int(input("Enter a response from above: "))
                        while centuriesResponse != 1 or centuriesResponse != 2: 
                            print("Please input a number.")
                            centuriesResponse= int(input("Enter a response from above: "))                            
                        if centuriesResponse == 1:
                            print("'IT IS A MYSTERY HOW ANYONE GETS HERE. COME WITH ME'")
                            goWith = input("Do you go with him?: ")
                            if goWith.capitalize == "Yes": 
                                print("***AUTHOR COME BACK HERE JESUS CHRIST I DIDN'T THINK I'D GET THIS FAR")
                            if goWith.capitalize == "No":
                                print("INSEWT")
                        elif centuriesResponse == 2: 
                            print("'I DID. I HAVE BEEN WAITING FOR CENTURIES. I'VE BEEN WAITING FOR YOU TO JOIN ME.'")
                            print("'COME WITH ME.'")
                    elif choicesSEEN == 4: 
                        print("\n'I AM MAGNUS. I AM THE LIVING.'")
                        print("\nYou look at your hands. You were pretty sure you are living too.\n")
                        name = input("\n'WHAT IS YOUR NAME?': ")
                        print("'AH I SEE.", name.upper(),", OF THE DEAD'")
                    break
                 
        # route 2 route 2 route 2 route 2 route 2
        elif goFurther.capitalize() == "No":
            print("You look back at the light. \nYou get up and try to reach for it. \nYou just barely touch it but you notice its cold.")
            print("As you touch the light, you feel something crumbling in your hand.\n \nYour skin is falling off.\n")
            print("In place of your skin is a black and empty void, \nbut its just your fingertips. \nSo it should be okay.")
            youShould = input("\nYou look back to the door, should you go?(Yes/No): ")
            if youShould.capitalize() == "Yes":
                print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
                print("You flex your, now, half-void hand. It feels like nothing. Like part of you is lost.")
                print("You're kind of glad you didn't stay in there.")
            elif youShould.capitalize() == "No":
                print("\nAs you wait, a piece of your shoulder falls off. \nIt doesn't hurt. Its just empty.\n")
                GOGO = input("Should you go?(Yes/No): ")
                if GOGO.capitalize() == "No":  
                    print("\nYour skin continues to fall off. \nAs you look around, you notice a mirror.")
                    print("You see your reflection, \nyour face is peeling off into the black void.")
                    print("Dread begins to fill you as your skin falls off.\n")
                    doubleGOGO = input("Should you go?(Yes/No): ")
                    if doubleGOGO.capitalize == "No":
                        print("\nYour skin falls off more rapidly, until you are nothing but dust.")
                        print("The world feels like and endless void of nothing.")
                        print("You feel nothing, and you are nothing.")
                        print("You shouldn't have touched the light.")
                        input()
                elif GOGO.capitalize == "Yes": 
                    print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
                    print("\nYou look up at the sky. \nIt's almost like an ocean of deep purple. \nThere are no clouds. \nThere is no sun.")
                    print("Somehow it's still light out, the grass is shiny. \nAs you look around you see a figure off to the side of you.")
                    print("\nThe figure approaches slowly.\n")
                    print("It seems like a black blob, and as it gets closer, he doesn't get any clearer.")
                    dontRun = input("\nDo you run back to the room?(Yes/No): ")
                    if dontRun.capitalize() == "Yes":
                        print("You run back to the room. \nA feeling of horror overcomes you.\nThe room is filled with darkness.\n")
                        print("\t","-"*45)
                        print("\t", "--", "                                  ", "     --")
                        print("\t", "--", "                                  ", "     --")
                        print("\t", "--", "\t\tIt Consumes You", " \t    --")
                        print("\t", "--", "                                  ", "     --")
                        print("\t", "--", "                                  ", "     --")
                        print("\t","-"*45)
                        input()                
                    if dontRun.capitalize() == "No":
                        print("The figure gets close to you. \nAs it stands in front of you, you feel a little comfort.")
                        print("'OH HELLO. I SEE YOU.'")
                        print("*\nHow will you respond?:")
                        print("1. 'You see me?'\t\t2.'I didn't realize the blobs could see.'")
                        print("3. 'Where am I?'\t\t4. 'Who are you?'")
                        choicesSEEN = input("Enter a response from above: ")
                        if choicesSEEN == "1":
                            print("'OF COURSE I SEE YOU. I HAVE EYES.'")
                            print("From what you could tell, the figure didn't have eyes. But okay?")
                        elif choicesSEEN == "2": 
                            print("'I AM NOT A BLOB. I AM JUST LIKE YOU.'")
                            print("You look down at your void-like hands, and the back to the figure. Maybe?")
                        elif choicesSEEN == "3":
                            print("'YOU ARE IN THE BEYOND. WELCOME TO THE BEYOND'")
                            print("The beyond? Did you die? The figure looks like he wants to keep talking.")
                            print("'IT IS VERY QUIET HERE. UP UNTIL YOU CAME RECENTLY. IT GOT LOUD.'")
                        elif choicesSEEN == "4": 
                            print("'I AM MAGNUS. I AM THE LIVING.'")
                            print("\nYou look at your hands. You arent so sure you're living anymore.\n")
                            name = input("\n'WHAT IS YOUR NAME?': ")
                            print("'AH I SEE.", name.upper(),", OF THE DEAD'")                    
            
            
            
    elif doorOpenClose.capitalize() == "No": # route 1
        print("\nYou look back at the room, it has nothing on the walls. \nNo pictures, no nothing.")
        keepLooking = input("\nDo you want to keep looking?(Yes/No): ")
        if keepLooking.capitalize() == "No":
            openDoor = input("\nDo you want to go open the door?(Yes/No): ")
            if openDoor.capitalize() == "Yes":
                print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                goFurther = input("\nDo you want to go further?(Yes/No): ")
                if goFurther.capitalize() == "Yes":
                    print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                 
            while openDoor.capitalize() == "No":
                print("There is still nothing on the walls.")
                keepLooking3 = input("\nDo you want to keep looking?(Yes/No): ")
                if keepLooking3.capitalize() == "No":
                    openDoor2 = input("\nDo you want to go open the door?(Yes/No): ")
                    if openDoor2.capitalize() == "Yes":
                        print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                        goFurther3 = input("\nDo you want to go further?(Yes/No): ")
                        if goFurther3.capitalize() == "Yes": # come back here
                            print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                                     
                        
                        elif goFurther3.capitalize() == "No": # alt route 2
                            print("You look back at the light. \nYou get up and try to reach for it. \nYou just barely touch it but you notice its cold.")
                            print("As you touch the light, you feel something crumbling in your hand.\n \nYour skin is falling off.\n")
                            print("In place of your skin is a black and empty void, \nbut its just your fingertips. \nSo it should be okay.")
                            youShould = input("\nYou look back to the door, should you go?(Yes/No): ")
                            if youShould.capitalize() == "Yes":
                                print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")
                                print("You flex your, now, half-void hand. It feels like nothing. Like part of you is lost.")
                            elif youShould.capitalize() == "No":
                                print("")
                                print("As you wait, a piece of your shoulder falls off. \nIt doesn't hurt. Its just empty.")
                                GOGO = input("Should you go?(Yes/No): ")
                                if GOGO.capitalize() == "No":  # come back here
                                    print("\nYour skin continues to fall off.\nAs you look around, you notice a mirror.")
                                    print("You see your reflection, \nyour face is peeling off into the black void.")
                                    print("Dread begins to fill you as your skin falls off.")
                                    doubleGOGO = str(input("Should you go?(Yes/No): "))
                                    if doubleGOGO.capitalize() == "No":
                                        print("Your body deteriorates, until you are nothing but dust.")
                                        print("\t","-"*45)
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t", "--", "\t\tYou Shouldn't Have Touched", " \t    --")
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t", "--", "                                  ", "     --")
                                        print("\t","-"*45)
                                        input()
                                    elif doubleGOGO.capitalize() == "Yes":                                            
                                        print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?\nYour body aches like nothing you've ever \nfelt before. ")
                                elif GOGO.capitalize() == "Yes":  # come back here
                                    print("As you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?\nYour body aches like nothing you've ever \nfelt before.")
                                                    
                
        
        elif keepLooking.capitalize() == "Yes": # route 1
            print("There is still nothing on the walls.")
            keepLooking2 = input("\nDo you want to keep looking?(Yes/No): ")
            if keepLooking2.capitalize() == "No":
                openDoor = input("\nDo you want to go open the door?(Yes/No): ")
                if openDoor.capitalize() == "Yes":
                    print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                    goFurther = input("\nDo you want to go further?(Yes/No): ")
                    if goFurther.capitalize() == "Yes":
                        print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                                      
                elif openDoor.capitalize == "No":
                    print("There is still nothing on the walls.")
                    keepLooking2 = input("\nDo you want to keep looking?(Yes/No): ")
                    if keepLooking2.capitalize() == "No":
                        openDoor = input("\nDo you want to go open the door?(Yes/No): ")
                        while openDoor.capitalize() == "No":
                            print("There is still nothing on the walls.")
                            keepLooking3 = input("\nDo you want to keep looking?(Yes/No): ")
                            if keepLooking3.capitalize() == "No":
                                print("A darkness fills your lungs. \nYou feel as if you can't breathe.")
                                print("\t","-"*45)
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "\tYou Shouldn't Have Waited", " \t    --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t","-"*45)
                                input()
                        if openDoor.capitalize() == "Yes":
                            print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                            goFurther = input("\nDo you want to go further?(Yes/No): ")
                            if goFurther.capitalize() == "No":
                                print("There is still nothing on the walls.")
                                goFurther2 = input("\nDo you want to go further?(Yes/No): ")
                                if goFurther2.capitalize() == "No":
                                    print("A darkness fills your lungs. \nYou feel as if you can't breathe.")
                                    print("\t","-"*45)
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t", "--", "\tYou Shouldn't Have Waited", " \t    --")
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t", "--", "                                  ", "     --")
                                    print("\t","-"*45)
                                    input()                                    
                                if goFurther2.capitalize() == "Yes":
                                    print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                            
                            elif goFurther.capitalize() == "Yes":  # come back here
                                print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                            
            
            while keepLooking2 != "Yes": # route 1
                print("There is still nothing on the walls.")
                keepLooking2 = input("\nDo you want to keep looking?(Yes/No): ")
                if keepLooking2.capitalize() == "No":
                    openDoor = input("\nDo you want to go open the door?(Yes/No): ")
                    while openDoor.capitalize() == "No": 
                        print("There is still nothing on the walls.")
                        openDoor2 = input("\nDo you want to go open the door?(Yes/No): ")
                        if openDoor2.capitalize() == "Yes":
                            print("\nWhen you open the door you see tall lush grass, \nyou think if you were to stand in it, \nit would be much taller than you.")
                            goFurther = input("\nDo you want to go further?(Yes/No): ")
                            if goFurther.capitalize() == "No": 
                                print("A darkness fills your lungs. \nYou feel as if you can't breathe.")
                                print("\t","-"*45)
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "\tYou Shouldn't Have Waited", " \t    --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t", "--", "                                  ", "     --")
                                print("\t","-"*45)
                                input()                                                                    
                            if goFurther.capitalize() == "Yes":  # come back here
                                print("\nAs you take a step out into the grass, you notice that it feels nothing like it. \nIt feels silky and smooth? \nWhere did you wake up at?")                                                     
                            
        
        
main()