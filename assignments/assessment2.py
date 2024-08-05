#using for,split,if to create stmnt that will print the words start with s
st = 'print only the stmnt that start with S'
for word in st.split():
    if(word[0]=='s' or word[0]=='S'):
        print(word)

#other way
for word in st.split():
    if(word[0].lower()=='s'):
        print(word)

# print the even numbers in range of 0 to 10

print(list(range(0,11,2)))

#using for
for i in range(0,11,2):
    print(i)

# print numbers divisible by 3 from 0 to 50

for num in range(0,51):
    if (num % 3==0):
        print(f'{num}:the number is divisible by 3')
    else:
     print('the number is not divisible by 3')     

print('---------------')
#list format
print([num for num in range(0,51) if num%3==0])

#print the word if that word length is even
st = 'print only the stmnt that start with S'
for word in st.split():
    if len(word) %2 == 0:
        print(f'{word} is even')

#print 1 to 100 , multiples of 3 print fizz, 5 multiples buzz, 5 and 3 multiples fizzbuzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)

#list comparision to print first letter of every word
st= 'print only first letter of every word'
print([word[0] for word in word.split(st)])

#
st = 'print only first letter of every word'
print([word[0] for word in st.split()])
