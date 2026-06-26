age = int(input("Enter your age :"))
#if statement number 1
if(age%2==0):
    print("a is even")
else:
    print("a is odd")

#if statement number 2
if(age>18):
    print("you are above the age of concent")
    print("Good for you")

elif(age<0):
    print("You are entering an invalide age")

elif(age==0):
    print("You are entering 0")

else:
    print("you are bellow the age of concent")

print("End of program")

# Grading/ranking program

marks = int(input("Enter your marks:"))

# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F
if(marks>90 and marks<=100):
    print("your grade is :exelent")
elif(marks>80 and marks<=90):
    print("your grade is :A")
elif(marks>70 and marks<=80):
    print("your grade is :B")
elif(marks>60 and marks<=70):
    print("your grade is :C")
elif(marks>50 and marks<=60):
    print("your grade is :D")
elif(marks<=50):
    print("your grade is:F")
    
