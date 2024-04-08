from task1 import task_1
from task2 import task_2
from task3 import task_3
from task4 import task_4
from task5 import task_5

'''Lab 3 - Default data types, collections, functions, modules. Minich S.V.'''

while True:
    
    chosen_task = input("Enter int number of the task (from 1 to 5): ")

    try:
        chosen_task = int(chosen_task)
        if(chosen_task < 1 or chosen_task > 5):
            print("ERROR, Enter int number from 1 to 5.")
            continue
        if(chosen_task == 1):
            task_1()
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