import calculatgame2
import wordsgame
import guessgame
class games:
    def __init__(self , name):
        self.name = name

    random_numbers()


game = games('lama')

game_user = input('what the game you want\n [1] [2]\n[3]\n')
if game_user == 1 :
    game.calculat_game()
elif game_user == 2 :
    game.words_game()
elif game_user == 3 :
    game.random_numbers()
elif game_user.isalpha():
    print('Please enter number')
else:
    print('Please enter correct')