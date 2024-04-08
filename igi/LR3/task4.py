def count_vowels(words):
    '''func for counting vowels in text'''
    numb_of_words_start_with_vowel = 0
    vowels = "aeiouAEIOU"
    for word in words:
        if word[0] in vowels:
            numb_of_words_start_with_vowel += 1
    return numb_of_words_start_with_vowel


def words_with_double_letters(words):
    '''func for counting words with double letters in them'''
    dict_for_words_with_double_letters = {}
    for index, word in enumerate(words):
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                dict_for_words_with_double_letters[word] = index
    return dict_for_words_with_double_letters


def task_4():
    '''Task 4 - count number of words with 1st vowel; words with double letters in them; serted list'''

    user_str = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether " +\
    "the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit " +\
    "with pink eyes ran close by her."

    user_str = user_str.replace(",", "")
    user_str = user_str.replace(".", "")

    words_in_str = user_str.split(" ")

    numb_of_words_start_with_vowel = count_vowels(words_in_str)
    dict_for_words_with_double_letters = words_with_double_letters(words_in_str)
    
    user_str = user_str.lower()
    words_in_str = user_str.split(" ")
    words_in_str.sort()

    return "Number of words with first vowel = " + str(numb_of_words_start_with_vowel) + "\n" +\
    "Words with double letters and their numbers in str = " + str(dict_for_words_with_double_letters.items()) + "\n" +\
    "Sorted words by alphabet = " + str(words_in_str)

