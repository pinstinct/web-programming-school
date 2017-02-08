champion = 'Lux'

def local1():
    champion = 'Ahri'
#    print('local1 champion : {}'.format(champion))
    print('local1 locals : {}'.format(locals()))
 #   print('local1 dir : {}'.format(dir()))

    def local2():
        champion = 'Ezreal'
 #       print('local2 champion : {}'.format(champion))
        print('local2 locals : {}'.format(locals()))
  #      print('local2 dir :{}'.format(locals()))

    local2()
    print('local1 locals :{}'.format(locals()))

#print('global champion : {}'.format(champion))
print('global locals():{}'.format(locals()))
#print(dir())
local1()
