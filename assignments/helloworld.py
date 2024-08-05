print('hello')
def add(a,b):
    c = a+b
    return c

sum=add(1,2)
print(sum)

print (7 * 7)
print ((10 * 10) + (10 * 10) - 100)
print (2+3)

a= 10
print(a)

a= 20
print(a)

a= a + a
print(a)

a= a + 10
print(a)
print(type(a))

mystr='manvitha'
print(mystr[1:6])
print(mystr[7])

x='learning python'
print(x.split())

if 3>2:
    print("true")

hungry = True
if (hungry):
    print("i'm hungry")
else:
    print("i'm not hungry")

mylist = [1,2,3]
for num in mylist:
    print(num)
for num in mylist:
    if(num%2==0):
        print(f'even:{num}')
    else:
        print(f'odd : {num}')

d={'k1':1,'k2':3}
for value in d.keys():
    print(value)

input('enter your name')
