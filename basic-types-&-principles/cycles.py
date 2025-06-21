msg = "tell me a number of guests: "
#while(1):
#    try:
    #   if(input != 'quit'):
    #        num = int(input(msg))
    #        if num >= 8:
    #            print(f"sorry you'll have to wait...")
    #       else:
    #            print(f"ok have a seat please")
    #   else:
    #       break
#    except:
#        print(f"not a number")

c = []
c.extend('list')
print(sorted(c))
print(c.sort())
print(c)

dic = {'k1':1, 'k2':2, 'k3':[3,3,3], 'k4':(4,4,4), 'k5':5, (0,1):6}
print(type(dic.keys()))

s = set(['4','5','2','1','3'])
print(s)

for i in range(10,15):
    print(i)
print(type(range(4)))

sq = ["red","yellow","green","blue"]
for i,square in enumerate(sq):
    print(i)
    print(square)

Date = 2017
def Thriller():
    Date = 1982
    return Date

print(Thriller())
print(Date)