from task1.task1_menu import Menu1
from task1.student import Student

while True:
    numb_task = input("Enter task number (from 1 to 5): ")
    numb_task = int(numb_task)
    if numb_task == 1:
        Menu1()
    elif numb_task == 2:
        print("task 2")
    elif numb_task == 3:
        print("task 3")
    elif numb_task == 4:
        print("task 4")
    elif numb_task == 5:
        print("task 5")
    else:
        break