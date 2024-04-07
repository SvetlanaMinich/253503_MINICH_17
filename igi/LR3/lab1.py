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
    letters_numb = 0
    digits_numb = 0
    user_str = input("Enter text to analize: ")
    for symb in user_str:
        if symb.isalpha() and symb.isascii():
            letters_numb += 1
        elif symb.isdigit():
            digits_numb += 1
    return "Number of latin letters = " + str(letters_numb) + " | " + "Number of digits = " + str(digits_numb)

def task_4():
    user_str = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether " +\
    "the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit " +\
    "with pink eyes ran close by her."

    user_str = user_str.replace(",", "")
    user_str = user_str.replace(".", "")

    words_in_str = user_str.split(" ")

    numb_of_words_start_with_vowel = 0
    vowels = "aeiouAEIOU"

    dict_for_words_with_double_letters = {}

    for index, word in enumerate(words_in_str):
        if word[0] in vowels:
            numb_of_words_start_with_vowel += 1
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                dict_for_words_with_double_letters[word] = index
    
    user_str = user_str.lower()
    words_in_str = user_str.split(" ")
    words_in_str.sort()

    return "Number of words with first vowel = " + str(numb_of_words_start_with_vowel) + "\n" +\
    "Words with double letters and their numbers in str = " + str(dict_for_words_with_double_letters.items()) + "\n" +\
    "Sorted words by alphabet = " + str(words_in_str)

def task_5():
    print("Enter list of INT numbers. If you want to stop, enter S.")
    user_list = []
    current_element = None
    mult_result = 1
    sum_result = 0
    while True:
        current_element = input("Enter element: ")
        try:
            current_element = int(current_element)
            user_list.append(current_element)
        except:
            if(current_element == "S"):
                break
            print("ERROR, Enter INT NUMBER.")
    for index, elem in enumerate(user_list):
        if index % 2 == 0 and elem % 2 == 0:
            mult_result *= abs(elem)
        sum_result += elem
    return "Result of multiplication = " + str(mult_result) + " | Result of sum = " + str(sum_result)

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