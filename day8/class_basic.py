class Shop:
    def __init__(self, name, shop_type, address):
        self.name = name
        self.__shop_type = shop_type
        self.address = address

    
    def show_info(self):
        print('상점정보 ({})\n  유형: {}\n  주소: {}'.format(self.name, self.__shop_type, self.address))

    def change_type(self, new_type):
        self.shop_type = new_type

    @classmethod
    def change_description(cls, new_description):
        cls.description = new_description

    @staticmethod
    def print_test():
        print('staticmethod test!')


shop1 = Shop('롯데리아', '패스트푸드', '서울시 강남구')
#print(shop1.__shop_type)
print('__shop_type' in dir(shop1))
print('name' in dir(shop1))
# shop1이 가진 속성과  메소드 확인
for item in dir(shop1):
    print(item)
#print(shop1.shop_type)
shop1.__shop_type = 'new type test'
print(shop1._Shop__shop_type)

shop1.address = '미국'
print(shop1.address)
shop1.show_info()
