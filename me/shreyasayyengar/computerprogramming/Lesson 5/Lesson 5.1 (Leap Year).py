# check if inputs can be casted to primitive types eg (int, string, double)


# PSUEDO CODE

# Using the modulus we can check if the REMAINDER == 0
# if (getInput) % (constant we want to check) == 0
# either return the leap year, in which we execute
# print("{0} is a leap year".format(inYear))
#
#
# or return the nested if.


inYear = int(input("What year would you like to check?\n\n")) # Asking for the year and defining it as an integer, int

year = inYear # creating a varibale

if (inYear % 4) == 0: #checking
   if (inYear % 100) == 0: #checking
       if (inYear % 400) == 0: #checking
           print("{0} is a leap year".format(inYear)) #output
       else:
           print("{0} is not a leap year".format(inYear)) #output
   else:
       print("{0} is a leap year".format(inYear))#output
else:
   print("{0} is not a leap year".format(inYear))#output
