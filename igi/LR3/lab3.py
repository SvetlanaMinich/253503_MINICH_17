def task_1():
    return 0

def task_2():
    odd_numb_count = 0
    sum = 0
    item = None
    while item != 0:
        item = input("Enter element: ")
        try:
            item = int(item)
            sum += item
            if item % 2 == 1 and item > 0:
                odd_numb_count += 1
        except:
            print("ERROR, Enter int number.")
    return "Sum = " + str(sum) + " | " + "Number of odd positive numbers = " + str(odd_numb_count)

def task_3():
    return 0

def task_4():
    return 0

def task_5():
    return 0

def interface():
    while True:
        chosen_task = input("Enter int number of the task (from 1 to 5): ")
        try:
            chosen_task = int(chosen_task)

            if(chosen_task < 1 or chosen_task > 5):
                print("ERROR, Enter int number from 1 to 5.")
                continue
            if(chosen_task == 1):
                print(task_1())
            elif(chosen_task == 2):
                print(task_2())
            elif(chosen_task == 3):
                print(task_3())
            elif(chosen_task == 4):
                print(task_4())
            elif(chosen_task == 5):
                print(task_5())
            
            stop_choise = input("Do you wanna stop this program? (If yes - enter Y): ")
            if(stop_choise == "Y"):
                break
        except:
            print("ERROR, You must enter INT NUMBER.")

interface()