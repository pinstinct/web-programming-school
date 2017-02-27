from func import game
from func import shop
from friends import chat

def turn_on():
    print('= Turn on game =')

    while True:
        choice = int(input('What would you like to do? \n 1: Go to Shop, 2: Play Game, 3: Send message, 0: Exit \n input : '))
        if isinstance(choice, int):
            if choice == 0:
                break
            elif choice == 1:
                shop.buy_item()
            elif choice == 2:
                game.play_game()
            elif choice == 3:
                chat.send_message()
            else:
                print('Choice not exsit')
            print('-----------')
        else:
            print('올바른 값이 주어지지 않았습니다.')
            break


if __name__ == '__main__':
    turn_on()
