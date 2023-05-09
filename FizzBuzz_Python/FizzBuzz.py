#FizzBuzz Problem
#by Steven Partlow
#This was a project that was part of the 2022 Complete Python Bootcamp from Zero to Hero in Python Course on Udemy
#https://www.udemy.com/course/complete-python-bootcamp/

'''This small program is my version of the famous 'FizzBuzz' problem where by we ask the user for a whole number
    and we output all numbers that are either divisable by 3 or 5 and BOTH 3 and 5 upto and including the entered number.'''

if __name__ == "__main__": #The main script

    while True: #We keep looping until the user enters a whole number and the program runs successully
        try: #We ask the user to enter a number
            num = int(input("Please enter a whole number: ")) #We take the user input and convert back to an integer
        except: #If we get an error we inform the user and ask them to enter a number again
            print("You must enter a whole number, please try again!")
            continue #We restart the while loop
        else: #Once we have a correct input
            for num in range(1,num+1): #We iterate through the number starting at 1 and upto and including the entered number
                if num % 3 == 0 and num % 5 == 0: #If the number is divisable by BOTH 3 and 5 we display 'FizzBuzz'
                    print("FizzBuzz, number {} is divisable by both 3 and 5".format(num))
                elif num % 3 == 0: #If the number is only divisable by 3 we display 'Fizz'
                    print("Fizz, number {} is divisable by 3".format(num))
                elif num % 5 == 0: #If the number is only divisable by 5 we display 'Buzz'
                    print("Buzz, number {} is divisable by 5".format(num))
        break #We break the loop and end the program