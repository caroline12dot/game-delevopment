import random
marks=[]
for i in range(20):
     marks.append(random.randint(0,100))
list1=[]
list2=[]
list3=[]
for i in marks:
     if i <=30:
          list1.append(i)
     elif 31<=i<=69:
          list2.append(i)
     else:
          list3.append(i)
print(list1)
print(list2)
print(list3)
