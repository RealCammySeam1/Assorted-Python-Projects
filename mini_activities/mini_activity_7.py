###Ask the age. Is the user is 18 or older, they do not require parential permission.
###If they are over 14, but under 18, ask if they have parential permission.
###If they don't, they cannot watch the movie.
###If they do have, they can watch the movie.

#Get age
age = int(input("Your age: "))

#Check if age is greater than or equal to 14
if age >= 14:

    #If age is greater than 18, skip permission check
    if age >= 18:
        print("You can watch the movie!")

    #If age is less than 18, ask permission
    if age < 18:
        permission = input("Do you have parential permission? (y/n)")
        if permission == "y":
            print("You can watch the movie!")

        else:
            print("You cannot watch the movie.")

#If age is less than 14, they can not watch the movie
else:
    print("You cannot watch the movie.")