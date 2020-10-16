import collections

list=['vinay','vijay','vikram','siva','vishnu','jas','kas','mas','las','tes','nes','vinay','jas','kas','kas']

## initializing string

## initializing a list to append all the duplicate characters
duplicates = []
for char in list:
    print(char,list.count(char),'1')

    if list.count(char) > 1:
        duplicates.append(char)
        #print(char.count())

print(duplicates)






