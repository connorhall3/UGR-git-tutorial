#!/usr/bin/env python
# coding: utf-8

# In[42]:


from random import randint
from IPython.display import clear_output

t = ["Rock", "Paper", "Scissors"]

def main():
    computer = t[randint(0,2)]
    while True:
        player = input("Rock, Paper, Scissors?")
        print('You chose', player)
        if ((player == 'Rock') or (player == 'Paper') or (player == 'Scissors')):
            print('Computer chose', computer)
            print()
            if player == computer:
                print("Tie!")
                break
            else:
                if player == 'Paper':
                    if computer == 'Rock':
                        print('You Win. Paper Covers Rock')
                        break
                    else:
                        print('You lose. Scissors Cut Paper')
                        break
                if player == 'Rock':
                    if computer == 'Paper':
                        print('You lose. Paper covers Rock')
                        break
                    else: 
                        print('You win. Rock smashes scissors')
                        break
                if player == 'Scissors':
                    if computer == 'Rock':
                        print('You lose. Rock smashes scissors')
                        break
                    else: 
                        print('You win. Scissors cut paper')
                        break
        else:
            print('That is not a valid move. Check your spelling')

main()
while True: #infinite loop until broken
    answer = input('Do you want to play again? (Y/N)') #answer is an input from user
    if answer.lower() == 'y' or answer.lower == 'yes': #if answer is 'y' or 'yes', clear output and restart main function
        print('-----------------------------------')
        clear_output()
        main()
    else:
        break


# In[ ]:




