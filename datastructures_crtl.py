list = [1,2,3,4]

# control statements
# for loop
for i in list:
    print(i)

print('----------------')
for i in range(len(list)):
    print(list[i])

print('----------------')
for i in range(0,len(list)):
    print(list[i])

print('----------------')
for i in range(0,len(list),2):
    print(i)

#break
print('-------Break---------')
for i in range(10):
    if i != 5:
        print(i)
        if i == 2:
            break
print('after break')


#continue
print('-------continue---------')
for i in range(10):
    if i == 5:
        print(i)
        continue
    if i == 9:
        break
print('after continue')

#match
print('-------match---------')
i=1
match i:
    case 1: print(i)
    case 2: print(i)

print('after match')

#while
print('-------while---------')



