import game
import shop

def turn_on():
    print('= Turn on game =')

    while True:
        choice = input('What would you like to do? \n 1: Go to shop, 2: Play game, 0: Exit \n input: ')
        if choice == '0':
            break
        elif choice == '1':
            shop.buy_item()
        elif choice == '2':
            game.play_game()
        else:
            print('Choice is not exist')
        print('--------------')

if __name__ == '__main__':
    turn_on()
