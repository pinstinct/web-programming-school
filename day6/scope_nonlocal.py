champion = 'Lux'

def local1():
    champion = 'Ahri'
    print('local1 locals: {}'.format(locals()))

    def local2():
        nonlocal champion
        champion = 'Ezreal'
        print('local2 locals: {}'.format(locals()))
    local2()
    print('local1 locals(): {}'.format(locals()))

print('global locals(): {}'.format(locals()))
local1()
