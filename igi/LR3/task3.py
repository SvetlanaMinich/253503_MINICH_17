from decorator import decorator_func

@decorator_func
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
