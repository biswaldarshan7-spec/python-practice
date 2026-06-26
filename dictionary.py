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
