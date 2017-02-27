class Shop:

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
        print('Set new name: {}'.format(self.__name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
        print('Set new name ({})'.format(self.__name))


shop1 = Shop('롯데리아', '서울시 강남구')
shop1.get_name()
shop1.set_name('bugerking')

shop2 = Shop('맥도날드', '서울시 논현동')
# property에 접근할 때, .name으로 호출 
print(shop2.name)
shop2.name = '버거킹'

