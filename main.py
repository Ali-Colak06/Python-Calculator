import functions

functions.opening_menu()

f1 = functions.operation_input()
if (f1 == True):
    print("See you next time!")
else:
    f2 = False
    while(True):
        if (f2 == True):
            print("See you next time!")
            break
        else:
            print("--------------------------------------------------------")
            cont = input("Do you want to continue with another operation? (Y/N)")
            if(cont == "Y" or cont == "y"):
                f2 = functions.operation_input()
            elif(cont == "N" or cont == "n"):
                print("See you next time!")
                break
            else:
                print("Wrong input! Please try again.")
                continue
