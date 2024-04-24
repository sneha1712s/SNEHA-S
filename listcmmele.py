shetty=[]
n=int(input('Enter the shetty list size'))
for i in range(0,n):
    ele=int(input('Enter the elements'))
    shetty.append(ele)
    
nagaraj=[]    
n=int(input('Enter the nagraj list size'))
for i in range(0,n):
    ele=int(input('Enter the elements'))
    nagaraj.append(ele)
    
for i in shetty:
    for j in nagaraj:
        if i==j:
            print(i)