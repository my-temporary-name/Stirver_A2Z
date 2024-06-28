# Provided 'n' you have to find out the n-th Fibonacci Number. 

n = int(input("Enter: ")) + 1
f =[]
f.append(0)
f.append(1)

for i in range(2,n):
    f.append(f[i-1] + f[i-2])

print(f[-1])