import random

def user_enter():
    '''func for user's input'''
    u_list = []
    while True:
        numb_of_elements = input("What number of elements do you want to enter? (int numb): ")
        try:
            numb_of_elements = int(numb_of_elements)
            if numb_of_elements <= 0:
                print("Enter POSITIVE int number.")
                continue
            for i in range(numb_of_elements):
                while True:
                    elem = input(f"Enter element {i}: ")
                    try:
                        elem = int(elem)
                        break
                    except:
                        print("Enter INT number.")
                u_list.append(elem)
            break
        except:
            print("Enter INT number.")
    return u_list

def rand_list():
    '''func for random list creation'''
    while True:
        numb_of_elements = input("What number of elements do you want to enter? (int numb): ")
        try:
            numb_of_elements = int(numb_of_elements)
            if numb_of_elements <= 0:
                print("Enter POSITIVE int number.")
                continue
            break
        except:
            print("Enter INT number.")

    for i in range(numb_of_elements):
        rand_elem = random.randint(-100, 100)
        yield rand_elem