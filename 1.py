mydict={'age':18,'grade':'B'}
mydict["age"]=""

if mydict["age"]:
    print("Something")
elif not mydict["age"]:
    print("Nothing")
else:
    print("None of the above")