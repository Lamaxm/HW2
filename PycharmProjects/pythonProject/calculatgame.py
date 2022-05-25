import time
from threading import Timer
from random import randint , random ,choice
import operator
ops = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
timeout = 60
def calculat_game():
    print("Enter the number of the level that you want: \n [1] for Hard level \n [2] for Medium level \n [3] for Easy level \n")
    while True :
        user_input = input()
        if user_input == '1':
            print("You have %d seconds to complete the exercise...\n" % timeout)
            for number_answer in range(0, 10):
                number1 = randint(10, 20)
                number2 = randint(10, 20)
                operation = choice(list(ops.keys()))
                answer = ops.get(operation)(number1, number2)
                answer = int(answer)
                while True:
                    print( number1, operation, number2, ' = ')
                    t = Timer(timeout, print, ['Sorry, times up'])
                    t.start()
                    answer_user = input()
                    t.cancel()
                    answer_user = int(answer_user)
                    if answer_user == answer:
                        print('great !!')
                    else:
                        print("Incorrect answer")
                    break
            print("Good Job")
        elif user_input == '2':
            print("You have %d seconds to complete the exercise...\n" % timeout)
            for number_answer in range(0, 10):
                number1 = randint(5, 15)
                number2 = randint(5, 15)
                operation = choice(list(ops.keys()))
                answer = ops.get(operation)(number1, number2)
                answer = int(answer)
                while True:
                    print( number1, operation, number2, ' = ')
                    t = Timer(timeout, print, ['Sorry, times up'])
                    t.start()
                    answer_user = input()
                    t.cancel()
                    answer_user = int(answer_user)
                    if answer_user == answer:
                        print('great !!')
                    else:
                        print("Incorrect answer")
                    break
            print("Good Job")
        elif user_input == '3':
            print("You have %d seconds to complete the exercise...\n" % timeout)
            for number_answer in range(0, 10):
                number1 = randint(0, 10)
                number2 = randint(0, 10)
                operation = choice(list(ops.keys()))
                answer = ops.get(operation)(number1, number2)
                answer = int(answer)
                while True:
                    print( number1, operation, number2, ' = ')
                    t = Timer(timeout, print, ['Sorry, times up'])
                    t.start()
                    answer_user = input()
                    t.cancel()
                    answer_user = int(answer_user)
                    if answer_user == answer:
                        print('great !!')
                    else:
                        print("Incorrect answer")
                    break
                print("Good Job")
        else:
            print("please enter right number")

calculat_game()

