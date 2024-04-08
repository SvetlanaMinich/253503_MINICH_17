def task_2():
    '''Task 2 - calculate sum of all list's elements; count number of even positive elements '''
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

