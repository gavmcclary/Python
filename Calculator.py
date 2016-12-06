########################################CALCULATOR############################

import sys
import time

def calculator():
    'A multi-choice calculator program.'

    while True:
        print ("Options:\n", "1: Squared\n","2: To the power of\n", "3: Square root of\n", "4: Floor division \n",
               "5: Exit")

        choice = int (input("Choose an option: "))

        if choice == 1:
            print ("Enter a number you want to square: ")
            num = int(sys.stdin.readline())
            result = num ** 2
            print(str(num) + " squared is " + str(result))
            time.sleep(2)
            
            
        elif choice == 2:
            print ("Enter the first number: ")
            num2 = int(sys.stdin.readline())
            print ("Enter the second number: ")
            num3 = int(sys.stdin.readline())
            result = (num2 ** num3)
            print(str(num2) + " to the power of " + str(num3) + " is " + str(result))
            time.sleep(2)
            

        elif choice == 3:
            print ("Enter the number you want to know the square root of: ")
            num4 = int(sys.stdin.readline())
            result = num4**(1/2.0)
            print("The square root of " + str(num4) + " is " + str(result))
            

        elif choice == 4:
            print ("Enter the number you want to floor divide ")
            num5 = int(sys.stdin.readline())
            print ("Enter the second number: ")
            num6 = int(sys.stdin.readline())
            result = (num5 // num6)
            print(str(num5) + " floor divided by " + str(num6) + " is " + str(result))
            
        elif choice == 5:

            break

calculator()

