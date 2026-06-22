name = "darshan" # a string is immutable
a = 'darshan'  # Single quoted string    
b = "darshan"    # Double quoted string  
c = '''darshan'''  # Triple quoted string

length_of_string = len(name) # count the length from 1
print(length_of_string)

# string slicing
name_short= name[0:3] # 0 included but 3 excluded
print(name_short)

character1= name[1] # starts from 0 and 1 excluded
print(character1)

# negetive slicing
name = "Darshan"

negetive_sliced = name[-4:-1]
print(negetive_sliced)

# skip value
skip = name[2:8:2] # the last digit is the skip value
print(skip)

word = "amazing"
skipped = word[1:6:2] # mzn
print(skipped)

# string functions

name = "darShan bro"

print(len(name))
print(name.endswith("han"))
print(name.startswith("Dar"))# this function is case sensetive
print(name.capitalize())# only capitalise the first letter
print(name.upper())
print(name.lower())
print(name.find("S"))# case sensetive,fint the index of the first occurance,if not present returns -1
print(name.replace("ar","dt"))