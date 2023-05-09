# Binary and Decimal Number Converter
# by Steven Partlow
#
# This was a project that was part of the 2022 Complete Python Bootcamp from Zero to Hero in Python Course on Udemy
# https://www.udemy.com/course/complete-python-bootcamp/
#
# This was one of the smaller projects I choose to to do as I really enjoyed coding in python and also really enjoy computer science and binary math is one of the things I actually enjoyed doing so I decided to combine the two things together and make a binary number calculator
# This program gives the user the option to convert a number from either from decimal to binary or vice versa

def decimal_to_binary():
    ''' This function converts a whole number to binary'''

    num = int(input("Enter a whole number: ")) # Ask the user to enter a whole number
    binary_number = '' # We are going to store the binary number as a string this so we can record the remainder after each division by 2 which will be our binary number

    while num > 0:   # We keep dividing our number by 2 until we reach zero
        print("{} divided by 2 is {} with a remainder of {}".format(num,num // 2, num % 2)) # Here we show our working
        binary_number = binary_number + str(num % 2) # We take the current value of num and divide by 2 and then add the result to our binary number string
        num = num // 2 # We then take num and divide it by 2 and overwrite 'num  with the new value

    binary_number = binary_number + str(0) # We then add the zero to the end of the string to finish the sequence
    print("\nThe number converted to binary is " + binary_number[::-1]) # The binary string will be our binary number but backwards so we use slicing to reverse the string and we the answer

def binary_to_decimal():
    '''This function converts a binary number back to decimal'''

    binary_number = int(input("Enter a binary number: ")) # Ask the user to enter a binary number
    binary_list = list(str(binary_number)[::-1]) # We convert the binary number to a list and we flip it backwards so we can iterate through it in the sequence we need to 
                                                 # calculate the powers correctly

    total = 0 # This is the running total which at the enter will be the binary number converted to decimal

    for n in range(0,len(binary_list)): # We iterate through our list, the value of 'n' will be the value we use for the postion which we calulate to the power of 2
                                        # this is why we reversed the list in the above code
        if int(binary_list[n]) == 1: # We convert the current selected element of the list back to a integer then if it equals 1
            print('Number: {} Position {} to Power of 2: {}'.format(binary_list[n],n,2**n)) # We print if the the current element is a 1, the current value of n and 2 to the power of n
            total = total + 2**n # if the current element is a '1' we calulate 2 to the power of n and add it the current total, as we are iterating through the number starting from
                                 #zero, 'n' is the position in our number system, the current element of 'binary_list' is our digit and we know our base is 2 as we are using binary.

    print("\nThe number converted to decimal is "+str(total)) # We print the final total which is our binary number converted back to decimal.

# This is the main part of the script which will ask the user which type of conversion they wish to perform.
# Utilises a try / except block
if __name__ == "__main__":

    # We display the choices for the user
    print("Binary and Decimal Number Converter")
    print("-----------------------------------")
    print("1. Convert from Decimal to Binary")
    print("2. Convert from Binary to Decimal")
    print("-----------------------------------")

while True: # We loop until the user makes the correct choice
    try:
        option = int(input("Select an option: ")) # Ask the user to enter either 1 or 2
    except:
        print("You must enter either 1 or 2, please try again!") # If they enter a letter, ask the user to try again and restart the loop
        continue
    else:
        if option == 1: # If they enter '1' we are converting a number from decimal to binary and then breaking the loop
            decimal_to_binary()
            break   
        elif option == 2: # If they enter '2' we are converting a number from binary to decimal and then breaking the loop
            binary_to_decimal()
            break
        else:
            print("You must enter either 1 or 2, please try again!") # If they enter any other number, ask the user to try again and restart the loop
            continue