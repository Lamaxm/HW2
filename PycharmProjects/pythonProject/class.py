#word game page

letters = ['s','l','e','m','n','o','u','t','d','a','i','r','w','c']
words = ['sum','sun','soul','sure','seem','see','sale','stare', 'time', 'man', 'woman', 'out', 'without', 'with', 'star', 'start', 'window',
         'lemon', 'cat', 'car', 'salt', 'cow', 'two', 'air','moon', 'coconut','tree', 'latte', 'camel', 'mountain'] #words for checked from in
item = 0
counter = 0
word_entred =[]
def check(input_user):
    for i in range(0,len(words)):
        if input_user == words[i]:
            return True

            return  False

def words_game():
    global item , counter
    user_input_level = input("Enter the number of the level that you want: \n [1] for Hard level (20 Words)\n [2] for Medium level (15 Words) \n [3] for Easy level (10 Words)\n")
    print(letters)
    print('Make a word from the above letters: ')
    print('Note: you can use the letter many times in a sigle word')
    if int(user_input_level) == 1 :
            while counter < 20:
                input_user = input()
                input_user = input_user.lower()
                if check(input_user):
                    print("Correct answer")
                else:
                    print('Incorrect answer \n Game Over !')
                    break
                counter = counter + 1
            print('If you want play again enter [1]\nIf you want return to main page enter [2]\nIf you want exsit enter [3]')
            while True:
                next_step = int(input())
                if next_step == 1:
                    words_game()
                elif next_step == 2:
                    import mainprogram
                elif next_step == 3:
                    exit()
                else:
                    print('Please enter correct number')
    if int(user_input_level) == 2 :
        while counter < 15:
            input_user = input()
            input_user = input_user.lower()
            if check(input_user):
                print("Correct answer")
            else:
                print('Incorrect answer \n Game Over !')
                break
            counter = counter + 1
        print('If you want play again enter [1]\nIf you want return to main page enter [2]\nIf you want exsit enter [3]')
        while True:
            next_step = int(input())
            if next_step == 1:
                words_game()
            elif next_step == 2:
                import mainprogram
            elif next_step == 3:
                exit()
            else:
                print('Please enter correct number')
    if int(user_input_level) == 3:
        while counter<10:
            input_user = input()
            input_user = input_user.lower()
            if check(input_user):
                print("Correct answer")
            else:
                print('Incorrect answer \n Game Over !')
                break
            counter = counter+1
        print('If you want play again enter [1]\nIf you want return to main page enter [2]\nIf you want exsit enter [3]')
        while True :
            next_step = int(input())
            if next_step == 1:
                words_game()
            elif next_step == 2:
                import mainprogram
            elif next_step == 3:
                exit()
            else:
                print('Please enter correct number')

words_game()