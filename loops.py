i=0
while(i<=50):
    print(i)
    i=i+1

for i in range (1,6):
    print(i)

# loop in list

list = [1,3,5,34,643,24,1,14435,24,86]

for i in list:
    print(i)

#loop in string

s = "darshan"

for i in s:
    print(i)

# break and continue

for i in range(50):
    if(i==12):
        break # exit the loop right now
    print(i)
for i in range(50):
    if(i==12):
        continue # skip only this iteration
    print(i)

# for with else statement

l= [1,7,8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!

# pass statement

for i in range(24):
    pass  
# without pass, the program will throw an error

i=0
while(i<23):
    print(i)
    i+=1