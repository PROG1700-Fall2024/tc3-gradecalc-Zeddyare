# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #variable initializing
    letterGrade=""
    numGrade=0.0
    modVal=0.3 
    modifier=""
    finGrade=0.0

    #greeting print command and explanation
    print("Grade Point Calculator\n")
    print("""Valid letter grades that can be entered: A, B, C, D, F.
Valid grade modifiers are +, - or nothing. 
All letter grades except F can include a + or - symbol.
Calculated grade point value cannot exceed 4.0\n
""")
    #input commands
    letterGrade=input("Please enter a letter grade: ").lower()
    modifier=input("Please enter a modifier (+, - or nothing): ") 

    #if statements for conversion 
    if letterGrade == "a":
        numGrade=4.0 
    elif letterGrade == "b":
        numGrade=3.0
    elif letterGrade == "c":
        numGrade=2.0
    elif letterGrade == "d":
        numGrade=1.0
    elif letterGrade == "f":
        numGrade=0.0  
    else: 
        print("You entered an invalid letter grade.") 
    
    #math for grade output 
    if (numGrade==4.0 and modifier=="+") or numGrade==0.0 or modifier=="":
        finGrade=numGrade 
    elif modifier=="+":
        finGrade=numGrade+modVal
    elif modifier=="-":
        finGrade=numGrade-modVal
    else:
        print("Not a valid modifier.")
    
    #outout 
    print("The numeric value is: {0:.1f}".format(finGrade))
    # YOUR CODE ENDS HERE

main()
