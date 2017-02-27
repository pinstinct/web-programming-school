def send_message():
    username = input('username: ')
    message = input('message: ')
    print('{}님에게 보내는 메시지: {}'.format(username, message))

if __name__ == '__main__':
    send_message()
