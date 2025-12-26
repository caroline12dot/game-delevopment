#count the occurance of vowels in the string
word=input("Enter the string ")
voweldict={"a":0,"e":0,"i":0,"o":0,"u":0}
for i in word:
    if i in voweldict:
        voweldict[i]+=1
print(voweldict)
#count the occurance of each letter in the string
word=input("Enter the string ")
letterdict={}
for i in word:
    if i.isalpha():
        if i in letterdict:
          letterdict[i]+=1
        else:
            letterdict[i]=1
print(letterdict)
