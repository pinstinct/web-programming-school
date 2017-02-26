champion = 'Lux'

def change_global_champion():
    global champion
    champion = 'Ahri'
    print('after change_global_champion: {}'.format(champion))
    print('id :{}'.format(id(champion)))


change_global_champion()
print('print global champion: {}'.format(champion))
print('id: {}'.format(id(champion)))

