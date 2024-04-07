import generator

def mult_func(u_list):
    mult_result = 1
    for index, elem in enumerate(u_list):
        if index % 2 == 0 and elem % 2 == 0:
            mult_result *= abs(elem)
    return mult_result


def sum_func(u_list):
    sum_result = 0
    for elem in u_list:
        sum_result += elem
    return sum_result


def task_5():
    user_list = []

    user_choise = input("Do you want to create your own list? (1 - create): ")
    if user_choise == 1:
        user_list = generator.user_enter()
    else:
        user_list = generator.rand_list()

    current_element = None

    while True:
        current_element = input("Enter element: ")
        try:
            current_element = int(current_element)
            user_list.append(current_element)
        except:
            if(current_element == "S"):
                break
            print("ERROR, Enter INT NUMBER.")
    
    mult_result =  mult_func(user_list)
    sum_result = sum_func(user_list)
    return "Result of multiplication = " + str(mult_result) + " | Result of sum = " + str(sum_result)
