import os
import random
from hangman_stages import stages

word_list=["cat","monkey","dog"]

end_game = False
lives = 6

word = random.choice(word_list)

print (word)

display = []
length_word = len(word)
print(length_word)




for _ in range (length_word):
    display += "_"

print (display)

while not end_game:
    input_letter = input("Input letter. - ")
    print(input_letter)
