import random
import pygame
import os
import sys

total = 36

def welcome():
    pygame.mixer.init()
    pygame.mixer.music.load('awesomeness.wav')
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1)
    print("\nWelcome To Times Test \n")
    x = input("Which number do you want to test on? (1-12) __")
    y = is_valid(int(x))
    test(str(y))


def is_valid(num):
    while num <= 0 or num > 12 or num == None:
        print("Invalid number please try agian (1-12)")
        num = int(input("Which number do you want to test on? (1-12) __"))
    return num

def valid_int(num, ques):
    while num.isnumeric() == False or len(num) == 0 or num == None:
        print("Invalid number please try agian")
        num = input(ques)
    return num


def test(number):
    print("\nLets Now Begin \n")
    print("There are 36 questions total \n")
    correct = 0
    wrong = 0
    i = 0
    set = 10
    good_loser = pygame.mixer.Sound('good_loser.wav')
    good_loser.set_volume(1)

    while i < total:
        if i < 12:
            rand = str(i + 1)

        else:
            rand = str(random.randint(1, 12))
        
        question = "\n" + str(i + 1) + ") " + number + " * " + rand + " = __ "
        ans = input(question)
        answer = valid_int(ans, question)
        corr = check(int(answer), int(number), int(rand), True)
        
        if corr == False:
            wrong += 1
        
        elif corr == True:
            correct += 1
            if correct == set:
                good_loser.play()
                set += 4
        
        i += 1
    
    score =  (correct, wrong)
    display(score)

def check(answer, num, mult, corr):
    boo = pygame.mixer.Sound('boo.wav')
    boo.set_volume(1)
    if int(num) * int(mult) != int(answer):
        boo.play()
        corr = False
        print("\nIncorrect, Try Agian\n")
        ques = str(num) + " * " + str(mult) + " = __ "
        ans = input(ques)
        answer = valid_int(ans, ques)
        check(int(answer), int(num), int(mult), corr)
    return corr
    

def display(score):
    print("You Got " + str(score[0]) + " Correct")
    print("You Got " + str(score[1]) + " Wrong")
    print("You SCORED: " + str(score[0]) + "/36")
    print(str(int((score[0]/total) * 100)) + "%")
    if int((score[0]/total) * 100) == 100:
        os.system("python snake_game.py")


def hard_mode():
    #100 questions
    pass

def harder_mode():
    #500 question
    pass

def hardest_mode():
    #100000000 question
    pass

if __name__ == "__main__":
    welcome()

