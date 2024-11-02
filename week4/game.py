import random
word_list = ["cat", "wolf", "monkey", "cow"]

end_game =  False
lives = 6

word = random.choice(word_list)
print (word)
display = []
lengt_word = len(word)
print (lengt_word)

for _ in range (lengt_word):
    display += "_"
print (display)

while not end_game:
    input_letter = input ("Input letter. - ")
    print (input_letter)

    for position in range (lengt_word):
        letter = word[position]
        # print (f"position = {position} , letter = {letter}")
        if letter == input_letter:
            display[position] = letter

    if input_letter not in word:
        #lives -=1
        lives = lives -1
        
        if lives == 0:
            end_game = True
            print("You lose")
            
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_game = True
        print ("You win")

