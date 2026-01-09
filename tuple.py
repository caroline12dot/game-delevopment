#packing the values
animal=(4,3,2,1,0)
for i in animal:
    print(i)
#unpacking the values
number,ant,inide,eat,ate=animal 
print()
print(number)
print(ant)
print(inide)
print(eat)
print(ate)
#tuple without bracket
tea="coffee","house",49
print(tea)
#nested tuple
run=("eat",[1,2,3,4],("water",15,24))
print(run)
#indexing
print(run[0][2])
print(run[2][1])