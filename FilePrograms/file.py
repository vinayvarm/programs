
# General code
#
# f=open('sample','r')
# print(f.mode)
# f.close()

# Reading contents w/o for loop using context manager

# with open('sample','r') as f:
#     f_contents= f.read()
#     print(f_contents)

# print one line w/o using for loop

# with open('sample','r') as g:
#     g=g.readline()
#     print(g)

# print all contents using for loop
with open('sample', 'r') as f1:
    for line in f1:
        print(line,end='')


