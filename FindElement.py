#list1=[1,2,3,4,5,6,7,8,9,10]

# using if and else
#num=int(input('enter number btw 1 to 10 '))
# #num=num.strip().lower()
#
# if list1.__contains__(num):
#     print('the numbner is ', num)
# else:
#     print('number not found')

# using for loop

# for n in list1:
#     if list1.__contains__(num):
#         print('number is ',num)
#         break
#
#     else:
#         print('number not found')
#         break

num=5
for x in range(11,0,-1):
    if x==num:
        print('value is', x)
        continue
    else:
        print(x)



