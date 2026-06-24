friends = ["Apple","Orange",5,345.43,False,"Aakash","Rohan"]

print(friends[0])
friends[0]="Grapes"

print(friends[0])# lists are mutable unlike strings
#lists can be indexed like strings

print(type(friends[0])) # lists can hold different data types
print(type(friends[2]))
print(type(friends[3]))
print(type(friends[4]))

print(friends[0:4])

# list methods

print(friends)
friends.append("Darshan") #  it changes the original list insted of making a new one
print(friends)

l1 = [1,4,54,53,22,46,86,44]
l1.sort() # sort the list in assending order
print(l1)
l1.reverse() # reverse the values stored in the list
print(l1)
l1.insert(3,57777) # insert the value(57777) at l1[3] place
print(l1)
l1.pop(3)
print(l1)
print(l1.pop(3)) # also return the pop out value while other functions doesn't return anything (None)