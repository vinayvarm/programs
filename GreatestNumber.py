n1=int(input('enter number'))
n2=int(input('enter number'))
n3=int(input('enter number'))

if n1>=n2 and n1>=n3:
    print("n1 is greatest", n1)
elif n2>=n3 and n2>=n1:
    print("n2 is greatest",n2)
elif n1==n2 and n2==n3:
    print('value are same')
else:
    print("n3 is greatest",n3)

