import generator

def mult_func(u_list):
    '''func for counting multiplication of list's even elements with even indexes'''
    mult_result = 1
    for index, elem in enumerate(u_list):
        if index % 2 == 0 and elem % 2 == 0:
            mult_result *= abs(elem)
    return mult_result


def sum_func(u_list):
    '''func for counting sum of list's elements'''
    sum_result = 0
    for elem in u_list:
        sum_result += elem
    return sum_result


def task_5():
    '''Task 5 - calculate multiplication of even elements with even indexes; sum of all list's elements'''
    user_list = []

    user_choise = input("Do you want to create your own list? (1 - create): ")
    if user_choise == 1:
        user_list = generator.user_enter()
    else:
        user_list = generator.rand_list()
        user_list = list(user_list)

    
    mult_result =  mult_func(user_list)
    sum_result = sum_func(user_list)

    for elem in user_list:
        print(elem)

    return "Result of multiplication = " + str(mult_result) + " | Result of sum = " + str(sum_result)
