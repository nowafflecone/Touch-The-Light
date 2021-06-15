def main():
    print("Are you going to pass your class?\n")
    
    toBeat = float(input("Enter the minimum to pass the class(%): "))
    while toBeat <= 49 or toBeat >= 100:
        print("Usually classes give a little bit of wiggle room.\nPlease put in the correct amount.\n")
        toBeat = float(input("Enter the minimum to pass the class(%): "))        
    grade = float(input("Enter your current grade: "))
    print("")
    if toBeat > grade:
        print("You're not going to pass the class.")
   
    elif grade >= toBeat: 
        print("You will pass the class.")
   
           
main()
