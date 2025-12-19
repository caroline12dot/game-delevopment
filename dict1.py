
dict1={}
while True:
    print("1.insert")
    print("2.get all countries")
    print("3.get all capitals")
    print("4.get the capital for a country")
    print("5.delete")
    print("6.exit")
    option=int(input("pick an option "))

    if 1==option:
        countrychoice=(input("enter the country name "))
        capitalchoice=(input("enter the capital name "))
        dict1[countrychoice]=capitalchoice
    elif 2==option:
        print(dict1.keys())
    elif 3==option:
        print(dict1.values())
    elif 4==option:
        countryname=(input("enter the name of the country "))
        print(dict1[countryname])
    elif 5==option:
        countryname=(input("what is the country name you want to delete "))
        dict1.pop(countryname)
    elif 6==option:
        break
