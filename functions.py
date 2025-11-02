# HISTORY
history = {}


# FUNCTIONS

def opening_menu():
    print("********************** CALCULATOR **********************")
    print("Operator types")
    print("--------------------------------------------------------")
    print("For addition, press --> '1'")
    print("For subtraction, press --> '2'")
    print("For multiplication, press --> '3'")
    print("For division, press --> '4'")
    print("For exponentiation, press --> '5'")
    print("For absolute value, press --> '6'")
    print("For matrix addition, press --> '7'")
    print("For matrix subtraction, press --> '8'")
    print("To view and edit history, press --> 'h'")
    print("To exit, press --> '*'")
    print("--------------------------------------------------------")

def operation_input():
    a = input("Please choose an operator type: ")
    if(a == "1"): addition()
    elif(a == "2"): subtraction()
    elif(a == "3"): multiplication()
    elif(a == "4"): division()
    elif(a == "5"): exponentiation()
    elif(a == "6"): absolute_value()
    elif(a == "7"): matrix_addition()
    elif(a == "8"): matrix_subtraction()
    elif(a == "h"): see_history()
    elif(a == "*"): return True
    else: print("Wrong input! Please try again")
    print("--------------------------------------------------------")

def test_the_input(input1):
    try:
        float(input1)
        return True
    except:
        print("Wrong input type! You need to enter a number.")
        return False

def addition():
    input_list = []
    while(True):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            break
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                print("Try again...")
                break
    if(i == "="):
        if(len(input_list) > 0):
            result = 0
            history_key = ""
            key_control = 1
            for n in input_list:
                result += n
                if(key_control == len(input_list)):
                    history_key += f"{n}"
                else:    
                    history_key += f"{n} + "
                key_control += 1
            history[history_key] = result
            print(result)
        else: print("You haven't entered any numbers yet!")

def subtraction():
    input_list = []
    while(True):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            break
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                print("Try again...")
                break
    if(i == "="):
        if(len(input_list) > 0):
            result = 2*input_list[0]
            history_key = ""
            key_control = 1
            for n in input_list:
                result -= n
                if(key_control == len(input_list)):
                    history_key += f"{n}"
                else:    
                    history_key += f"{n} - "
                key_control += 1
            history[history_key] = result
            print(result)
        else: print("You haven't entered any numbers yet!")

def multiplication():
    input_list = []
    while(True):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            break
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                print("Try again...")
                break
    if(i == "="):
        if(len(input_list) > 0):
            result = 1
            history_key = ""
            key_control = 1
            for n in input_list:
                result *= n
                if(key_control == len(input_list)):
                    history_key += f"{n}"
                else:    
                    history_key += f"{n} * "
                key_control += 1
            history[history_key] = result
            print(result)
        else: print("You haven't entered any numbers yet!")

def division():
    input_list = []
    while(True):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            break
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                print("Try again...")
                break
    if(i == "="):
        if(len(input_list) > 0):
            try:
                result = input_list[0]*input_list[0]
                history_key = ""
                key_control = 1
                for n in input_list:
                    result /= n
                    if(key_control == len(input_list)):
                        history_key += f"{n}"
                    else:    
                        history_key += f"{n} / "
                    key_control += 1
                history[history_key] = result
                print(result)
            except ZeroDivisionError:
                print("Numbers cannot be divided by 0")
        else: print("You haven't entered any numbers yet!")

def exponentiation():
    b = input("Please enter the bottom number: ")
    u = input("Please enter the top number: ")
    f1 = test_the_input(b)
    f2 = test_the_input(u)
    if (f1 and f2):
        if(float(b) == 0 and float(u) == 0):
            print("The expression 0^0 is undefined!")
        else:
            result = float(b) ** float(u)
            history[f"{b} ^ {u}"] = result
            print(result)
                
def absolute_value():
    n = input("Please enter a number: ")
    test_the_input(n)
    if(float(n) < 0):
        result = -float(n)
    else:
        result = float(n)
    history[f"|{n}|"] = result
    print(result)

def creating_matrix(c, r):
    f1 = test_the_input(c)
    f2 = test_the_input(r)
    if (f1 and f2):
        if(int(c) != 0 and int(r) != 0):
            matrix = [[0 for j in range(int(c))] for i in range(int(r))]
            row_number = 1
            for rows in matrix:
                column_number = 1
                for nums in rows:
                    while(True):
                        try:
                            num = input(f"row{row_number}, column{column_number}: ")
                            matrix[row_number-1][column_number-1] = float(num)
                            break
                        except ValueError:
                            print("Wrong input type in matrix! Enter a number!")
                            continue
                    column_number += 1
                row_number += 1
            return matrix
        else: print("The number of rows and columns must be greater than 0!")
    else: print("column and row input types are Wrong !")

def matrix_addition():
    column = input("Please enter the column number: ")
    row = input("Please enter the row number: ")
    if(column != "" and row != ""):
        print("MATRİX 1:")
        print("--------------------------------------------------------------")
        matrix_1 = creating_matrix(column, row)
        print("--------------------------------------------------------------")
        print("MATRİX 2:")
        print("--------------------------------------------------------------")
        matrix_2 = creating_matrix(column, row)
        print("--------------------------------------------------------------")
        try:
            if(int(column) != 0 and int(row) != 0):
                matrix_last = [[0 for j in range(int(column))] for i in range(int(row))]
                row_number = 1
                for rows in matrix_last:
                    column_number = 1
                    for nums in rows:
                        matrix_last[row_number-1][column_number-1] = matrix_1[row_number-1][column_number-1] + matrix_2[row_number-1][column_number-1]
                        column_number += 1
                    row_number += 1
                print(f"The last matrix:\n" + "\n".join(map(str, matrix_last)))
                history_key = f"{matrix_1} + {matrix_2}"
                history[history_key] = matrix_last
                return matrix_last
        except: print("Wrong input type!")
    else: print("You haven't entered any numbers yet!")

def matrix_subtraction():
    column = input("Please enter the column number: ")
    row = input("Please enter the row number: ")
    if(column != "" and row != ""):
        print("MATRIX 1:")
        print("--------------------------------------------------------------")
        matrix_1 = creating_matrix(column, row)
        print("--------------------------------------------------------------")
        print("MATRIX 2:")
        print("--------------------------------------------------------------")
        matrix_2 = creating_matrix(column, row)
        print("--------------------------------------------------------------")
        try:
            if(int(column) != 0 and int(row) != 0):
                matrix_last = [[0 for j in range(int(column))] for i in range(int(row))]
                row_number = 1
                for rows in matrix_last:
                    column_number = 1
                    for nums in rows:
                        matrix_last[row_number-1][column_number-1] = matrix_1[row_number-1][column_number-1] - matrix_2[row_number-1][column_number-1]
                        column_number += 1
                    row_number += 1
                print(f"The last matrix:\n" + "\n".join(map(str, matrix_last)))
                history_key = f"{matrix_1} - {matrix_2}"
                history[history_key] = matrix_last
                return matrix_last
        except: print("Wrong input type!")
    else: print("You haven't entered any numbers yet!")

def see_history():
    if (len(history) > 0):
        key_to_index = []
        index_num = 1
        for k, v in history.items():
            key_to_index.append(k)
            print(f"{index_num}) --> {k} : {v}")
            index_num += 1
        cont = input("Press 'Y' to delete operations from history (Press anything else to exit): ")
        if (cont == "Y" or cont == "y"):
            while(True):
                deleted_item_index = input("Please enter the operation index number: ")
                try:
                    deleted_item_key = key_to_index[int(deleted_item_index)-1]
                    del(history[deleted_item_key])
                    see_history()
                    break
                except:
                    print("Wrong input!")
                    continue
    else: print("The history is empty")
