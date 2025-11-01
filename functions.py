# HISTORY
history = {}


# FUNCTIONS

def opening_menu():
    print("********************** CALCULATOR **********************")
    print("Operator types")
    print("--------------------------------------------------------")
    print("For addition press --> '1'")
    print("For subtraction press --> '2'")
    print("For multiplication press --> '3'")
    print("For division press --> '4'")
    print("For exponentiation press --> '5'")
    print("For absolute value press --> '6'")
    print("For matrix addition press --> '7'")
    print("For matrix subtraction press --> '8'")
    print("For seeing and editing history press --> 'h'")
    print("For exit press --> '*'")
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
        print("Wrong input type!")
        return False

def addition():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            end = False
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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
        return result
    else: print("You haven't input any numbers yet!")

def subtraction():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            end = False
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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
        return result
    else: print("You haven't input any numbers yet!")
def multiplication():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            end = False
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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
        return result
    else: print("You haven't input any numbers yet!")

def division():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number(Press '=' to find the result.): ")
        if(i == "="):
            end = False
        else:
            f = test_the_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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
            return result
        except ZeroDivisionError:
            #if(history_key != ""):
                #history.popitem()
            print("Numbers cannot be divided by 0")
    else: print("You haven't input any numbers yet!")

def exponentiation():
    b = input("Please enter the bottom number: ")
    u = input("Please enter the top number as integer: ")
    f1 = test_the_input(b)
    f2 = test_the_input(u)
    result = 1
    if (f1 and f2):
        if (int(u) < 0):
            for i in range(-int(u)):
                result *= int(b)
            result = 1/result
        else:
            for i in range(int(u)):
                result *= int(b)
        history[f"{b} ^ {u}"] = result
        print(result)
        return result
                
def absolute_value():
    n = input("Please enter a number: ")
    test_the_input(n)
    if(float(n) < 0):
        result = -float(n)
    else:
        result = float(n)
    history[f"|{n}|"] = result
    print(result)
    return result

def creating_matrix(c, r):
    f1 = test_the_input(c)
    f2 = test_the_input(r)
    if (f1 and f2):
        matrix = [[0 for j in range(int(c))] for i in range(int(r))]
        row_number = 1
        for rows in matrix:
            column_number = 1
            for nums in rows:
                try:
                    num = input(f"row{row_number}, column{column_number}: ")
                    matrix[row_number-1][column_number-1] = float(num)
                except ValueError:
                    print("Wrong input!")
                column_number += 1
            row_number += 1
    else: print("Wrong input type!")
    return matrix

def matrix_addition():
    column = input("Please enter the column number: ")
    row = input("Please enter the row number: ")
    print("MATRİX 1:")
    print("--------------------------------------------------------------")
    matrix_1 = creating_matrix(column, row)
    print("--------------------------------------------------------------")
    print("MATRİX 2:")
    print("--------------------------------------------------------------")
    matrix_2 = creating_matrix(column, row)
    print("--------------------------------------------------------------")
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

def matrix_subtraction():
    column = input("Please enter the column number: ")
    row = input("Please enter the row number: ")
    print("MATRIX 1:")
    print("--------------------------------------------------------------")
    matrix_1 = creating_matrix(column, row)
    print("--------------------------------------------------------------")
    print("MATRIX 2:")
    print("--------------------------------------------------------------")
    matrix_2 = creating_matrix(column, row)
    print("--------------------------------------------------------------")
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

def see_history():
    if (len(history) > 0):
        key_to_index = []
        index_num = 0
        for k, v in history.items():
            key_to_index.append(k)
            print(f"{index_num}) --> {k} : {v}")
            index_num += 1
        cont = input("Do you want to delete history? (Y/N)")
        if (cont == "Y"):
            deleted_item_index = int(input("Please enter the operation number: "))
            deleted_item_key = key_to_index[deleted_item_index]
            del(history[deleted_item_key])
    else: print("The history is empty")
