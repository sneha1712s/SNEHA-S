names="balaji srinivasan"
print(names)
print(names[:])
print(names[2:])
print(names[-1:])
print(names[-5:-1])
print(names[::-1])
print(names[::-3])
sep='-'.join(names[::2])
print(sep)
for i in range(0,len(names)):
    if(i%3==0 and i!=0):
        print('-',end='')
    else:
        print(names[i],end='')


