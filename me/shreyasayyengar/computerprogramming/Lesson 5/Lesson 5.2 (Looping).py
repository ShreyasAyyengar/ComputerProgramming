
#
#
# Sudo Code!
#
# Defining the (input) as a string
# Defining a list with all possible valid answers (but not the answers themselves)
# The while: keeps the programe running as long as we tell it too.
# As long as the input is not "June" then proceed to analyse the answer.
# If the answer is not stored in the ArrayList[], deny the answer with a print.
# If the answer is in the list but is not the correct answer, deny with a print.
# If the answer is correct, accept with a print, and close with exit code {0}



birthdaymonth = input("Guess my birthday month (Capitalise the first letter)\n\n")

while birthdaymonth != "June":

    birthday_List = ["January", "February", "March", "April", "May", "July", "August", "September", "October",
                     "November",
                     "December", ]

    if birthdaymonth not in birthday_List:
        print("Oops! You did not enter a valid month. Please try again!")

    else:
        print("Incorrect! Please try again")

    birthdaymonth = input("Guess my birthday month (Capitalise the first letter)\n\n")

    # birthdaymonth = input("Guess my birthday month (Capitalise the first letter)\n\n")

if birthdaymonth == "June":
    print("Well Done! You have guessed my birthday month.")
