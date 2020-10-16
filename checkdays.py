month=input('enter month ')
month=month.strip()

list1= ['jan','mar','may','jul','aug','oct','dec']
list2=['apr','june','sep']

print('USER SHOULD ENTER STRINGS LIKE "jan"')

for i in  list1:
    if i==month:
        print('days are ', 31)


for j in list2:

    if j==month:
        print('days are',30)
    elif month=='feb':
        print('days are', 28 and  29)
    else:
        print('invalid month please follow the format as mentioned above')







