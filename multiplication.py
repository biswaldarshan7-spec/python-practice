# multiplication table using for loop

n = int(input("Enter the number:"))

for i in range(1,11):
    # print(n,"x",i,"=",n*i)
    print(f"{n} X {i} = {n * i}")

# multiplication table using while loop

n = int(input("Enter the number:"))
i = 1
while(i<=10):
    print(f"{n} X {i} = {n*i}")
    i+=1

# multiplication table using function

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter the number:"))

table(n)