# year = int(input('enter year'))
#
# def checkleap():
#
#     if year%4==0 and(year%100!=0 or year%400==0) :
#         print('leap year')
#     else:
#         print('not leap year')
#
# checkleap()

month= input('enter month')
month = month.strip().lower()

def checkdaysformonth():
    if month=='jan' or month=='march' or month=='may' or month=='july' or  month=='august' or  month=='oct' or month=='dec':
        print('days for this month are',31)
    elif month=='apr' or month =='june' or month=='sep':
        print('days for this month are',30)
    elif month=='feb':
        print('leap year month', 28 or 29)
    else:
        print('invalid month')

checkdaysformonth()
