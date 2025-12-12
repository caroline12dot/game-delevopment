#create dictionary
dict1={"cake":"food","sweets":"candy","pasta":"carbs"}
print(dict1)
#print keys
print(dict1.keys())
#print values
print(dict1.values())
#check if key exists in dictionary
if "tea" in dict1:
    print("key exists")
else:
    print("key doesnt exist")
#access value in dictionary
print(dict1["sweets"])
#add to dictionary
dict1["hydration"]="water"
print(dict1)
#updating values in dictionary
dict1["cake"]="chocolate"
print(dict1)
#delete a key value from dictionary
del(dict1["pasta"])
print (dict1)
#add list as value into dictionary
dict1["tea"]=["peppermint","milk","sugar"]
print(dict1)
#access a value in the list stored inside dictionary
print(dict1["tea"][2])