def print_v_pattern(name):
    n=len(name)
    for i in range(n):
        for j in range(n*2):
            if i==j or j==n*2-1-i:
                print(name[i],end=' ')
                
            else:
                print(' ',end=' ')
        print()
name="sneha"
print_v_pattern(name)

