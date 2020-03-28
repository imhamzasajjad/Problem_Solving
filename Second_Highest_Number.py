

# Program 1: Find the Second Highest number from input data.

            # Getting list value from User
            # Taking an empty list in which we will store data element from user.
            lst=[]
            # How many elements a user want to enter in the list?
            element= int(input("Enter more Then 2 Element"))
            # For Loop for iteration
            if(element>2):
                for i in range(0, element):
                    ele = int(input("Enter the list element:"))
            # Adding Elements into the list
                    lst.append(ele)
            else:
                print("you entered invalid")
                exit()
            print("Your entered list is:", lst)

            # Sorting the list
            lst.sort()
            # Getting the second Highest Number by using Index number
            print("Second Highest number is:", lst[-2])

#Program 2: Without user input.

            lst= [4, 85, 27, 52, 90]
            lst.sort()
            print("Second Highest Number is:", lst[-2])

