from task1.task1_menu import Menu1
from task2.task2_menu import Menu2
from task3.task3_menu import Menu3
from task4.task4_menu import Menu4
from task5.task5_menu import Menu5
from checking.intchecking import IntChecking

def Task():
    numb_task = input("Enter task number (from 1 to 5): ")
    while not IntChecking(numb_task):
        numb_task = input("Enter int number from 1 to 5: ")
    numb_task = int(numb_task)
    if numb_task == 1:
        Menu1()
    elif numb_task == 2:
        Menu2()
    elif numb_task == 3:
        Menu3()
    elif numb_task == 4:
        Menu4()
    elif numb_task == 5:
        Menu5()