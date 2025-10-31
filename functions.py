# HISTORY
history = {}


# FUNCTİONS

def opening_menu():
    print("********************** CALCULATOR **********************")
    print("Operator types")
    print("--------------------------------------------------------")
    print("For addition press --> '1'")
    print("For suubtraction press --> '2'")
    print("For multiplication press --> '3'")
    print("For division press --> '4'")
    print("For exponentiation press --> '5'")
    print("For absolute value press --> '6'")
    print("For matrix addition press --> '7'")
    print("For matrix subtraction press --> '8'")
    print("For matrix multiplication press --> '9'")
    print("For history press --> 'h'")
    print("For exit press --> '*'")

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
    elif(a == "9"): matrix_multiplication
    elif(a == "h"): see_history()
    elif(a == "*"): return True
    else: print("Wrong input! Please try again")

def test_thee_input(input1):
    flag1= False
    try:
        float(input1)
        flag1 = True
    except:
        print("Wrong input type!")
    return flag1

def addition():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number: ")
        if(i == "="):
            end = False
        else:
            f = test_thee_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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

def subtraction():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number: ")
        if(i == "="):
            end = False
        else:
            f = test_thee_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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
    
def multiplication():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number: ")
        if(i == "="):
            end = False
        else:
            f = test_thee_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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

def division():
    end = True
    input_list = []
    while(end):
        i = input("Please enter a number: ")
        if(i == "="):
            end = False
        else:
            f = test_thee_input(i)
            if(f == True):
                input_list.append(float(i))
            else:
                end = False
                print("Try again...")
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
    except(ZeroDivisionError):
        if(history_key != ""):
            history.popitem
        print("Numbers cannot be divided by 0")
    return result

def exponentiation():
    b = input("Please enter the bottom number: ")
    u = input("Please enter the top number as integer: ")
    f1 = test_thee_input(b)
    f2 = test_thee_input(u)
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
    test_thee_input(n)
    if(float(n) < 0):
        result = -float(n)
    else:
        result = float(n)
    history[f"|{n}|"] = result
    print(result)
    return result

def creating_matrix(c, r):
    f1 = test_thee_input(c)
    f2 = test_thee_input(r)
    if (f1 and f2):
        matrix = [[0 for j in range(int(c))] for i in range(int(r))]
        row_number = 1
        for rows in matrix:
            column_number = 1
            for nums in rows:
                num = input(f"row{row_number}, column{column_number}: ")
                matrix[row_number-1][column_number-1] = float(num)
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
    row_number = 1
    for rows in matrix_1:
        column_number = 1
        for nums in rows:
            matrix_1[row_number-1][column_number-1] += matrix_2[row_number-1][column_number-1]
            column_number += 1
        row_number += 1
    print(f"The last matrix:\n{matrix_1}")
    return matrix_1

def matrix_subtraction():
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
    row_number = 1
    for rows in matrix_1:
        column_number = 1
        for nums in rows:
            matrix_1[row_number-1][column_number-1] -= matrix_2[row_number-1][column_number-1]
            column_number += 1
        row_number += 1
    print(f"The last matrix:\n{matrix_1}")
    return matrix_1
    

def matrix_multiplication():
    print("Matrix multiplication")

def see_history():
    print(history)
    
