print((5**2)+75+(1-0.75))
s='hello'
#give the index command that returns 'e'
print(s[1])
#reverse the string 'hello' using slicing
print(s[::-1])
#two methods to print 'o' using index
print(s[4])
print(s[-1])
#using slicing
print(s[4:])
#lists 
#build list in 2 seperate ways [0,0,0]
lst=[0,0,0]
print(lst)
#method2
print([0,0,0])
#reassign 'hello' in the nested list to say goodbye instead
list3=[1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)
#sort the list in
list4 = [3,5,4,2,6]
list4.sort()
print(list4)
#grab hello 
d= {'simple_key':'hello'}
print(d['simple_key'])
#grab new
d={'k1':{'k2':'iam new to python'}}
print(d['k1']['k2'][4:7])
#grab hello
d={'k1':[{'nestkey':['this is deep',['hello']]}]}
print(d['k1'][0]['nestkey'][1])
#set to find unique values
lst5=[1,2,2,4,5,6,6,7,8,2,3]
print(set(lst5))
