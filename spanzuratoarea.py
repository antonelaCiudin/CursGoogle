# word = "onomatopee"
import random
from random_word import list_of_random_word
word = random.choice(list_of_random_word)
word_list = []
unique_list = set(word)
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())

print(" ".join(word_list))
word_len = len(unique_list) - 2
# word_len = len(unique_list)

count_nr = 1
list_already_checked = []
new_word = word
while count_nr <= word_len:
    user_letter = input("Alege o litera: ").lower()
    if user_letter == "":
        print("Introdu o litera")
        continue
    if user_letter in word_list:
        print("Litera deja afisata pe ecran")
    elif user_letter in list_already_checked:
        print(f"Litera a fost deja incercata, lista literelor incercate: {' '.join(list_already_checked)}")
    else:
        if user_letter in word:
            word_list[word.index(user_letter)] = user_letter
            # for iterator, value in enumerate(word):
            #     if user_letter == value:
            #         word_list[iterator] = user_letter

            print(" ".join(word_list))
        else:
            count_nr += 1
        if '_' not in word_list:
            print("Ai castigat!")
            break
        elif count_nr > word_len:
            print(f"Ai pierdut! Cuvantul era: {word}")
        list_already_checked.append(user_letter)