import time
from threading import Timer
from random import randint , random ,choice
import operator
ops = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

def numbers():
    user_input = input("Enter the number of the level that you want: \n [1] for Hard level \n [2] for Medium level \n [3] for Easy level \n")
    timeout = 60
    print("You have %d seconds to complete the exercise...\n" % timeout)
    if user_input == '1':
        number_answer = 0
        while number_answer < 5 :
            number1 = randint(0, 10)
            number2 = randint(0, 10)
            operation = choice(list(ops.keys()))
            answer = ops.get(operation)(number1, number2)
            answer = int(answer)
            while True:
                print('What is ', number1, operation, number2, '?')
                t = Timer(timeout, print, ['Sorry, times up'])
                t.start()
                answer_user = input()
                t.cancel()
                answer_user = int(answer_user)
                if answer_user == answer:
                    print('great !!')
                else:
                    print("try again")
                number_answer = number_answer+1
                break
        print("Good Job")
    if user_input == '2' :
        number_answer = 0
        while number_answer < 11:
            number1 = randint(0, 20)
            number2 = randint(0, 20)
            operation = choice(list(ops.keys()))
            answer = ops.get(operation)(number1, number2)
            answer = int(answer)
            while True:
                print('What is ', number1, operation, number2, '?')
                t = Timer(timeout, print, ['Sorry, times up'])
                t.start()
                answer_user = input()
                t.cancel()
                answer_user = int(answer_user)
                if answer_user == answer:
                    print('great !!')
                else:
                    print("try again")
                number_answer = number_answer + 1
                break
        print("Good Job")
    if user_input == '3' :
        number_answer = 0
        while number_answer < 5:
            number1 = randint(0, 15)
            number2 = randint(0, 15)
            operation = choice(list(ops.keys()))
            answer = ops.get(operation)(number1, number2)
            answer = int(answer)
            while True:
                print('What is ', number1, operation, number2, '?')
                t = Timer(timeout, print, ['Sorry, times up'])
                t.start()
                answer_user = input()
                t.cancel()
                answer_user = int(answer_user)
                if answer_user == answer:
                    print('great !!')
                else:
                    print("try again")
                number_answer = number_answer + 1
                break
        print("Good Job")

numbers()
