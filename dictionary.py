d={} # empty dictionary

marks = {
    "Darshan": 355,
    "Shivam": 878,
    "manoj":545,
    0:"Darshan"
}

print(marks,type(marks))
print(marks["Shivam"])
print(marks.items()) # returns a list of key value pair
print(marks.keys())
print(marks.values())
marks.update({"Sai":234})
print(marks.items())

# sets and set methods

s = {1,4,54,45,35,53,4,4,4,2,"Darshan"}
# s = {} this is an empty dictionary
e = set() # empty set
print(s) # sets can't contain duplicate values and it is unordered
s.add(53534)
print(s,type(s))
print(len(s))
s.remove(1)
print(s)

# set union and intersection

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))
