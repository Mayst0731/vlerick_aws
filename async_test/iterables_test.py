lstOfInts = list()
lstOfInts.append(1)
lstOfInts.append(2)
lstOfInts.append(3)

# get iterator of list using __iter__()
it = lstOfInts.__iter__()
print("iterator of list: " + str(it))

# get member element of list using __getitem__()
print("iterator of list: " + str(lstOfInts.__getitem__(2)))

# iterator returns itself when passed to the iter function
print("it is iter(it) = " + str(it is iter(it)))

# get another iterator for list using the built in iter() method
it_another = iter(lstOfInts)
print("it_another = " + str(it_another))

print("iteration using iterator in a for loop")
# iterate using the iterator
for element in it_another:
    print(element)

print("iteration using iterable in a for loop")
# iterate using the iterable
for element in lstOfInts:
    print(element)