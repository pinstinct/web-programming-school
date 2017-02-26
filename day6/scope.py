champion = 'Lux'

def show_global_champion():
    print('show_global_champion: {}'.format(champion))
    print('show_global_champion ID: {}'.format(id(champion)))
    print(locals())

def change_global_champion():
    # UnboundLocalError
    # print('before change_global_champion: {}'.format(champion))
    champion = 'Ahri'
    print('change_global_champion: {}'.format(champion))
    print('change_global_champion ID: {}'.format(id(champion)))
    print(locals())


show_global_champion()
print('=====')
print('print champion: {}'.format(champion))
print('=====')
change_global_champion()
