#creating empty list
my_list = []

#Appending the following elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 at the second position in the list
my_list.insert(1, 15)

#Extend my_list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)

#Removing the last element from my_list.
my_list.pop()

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list
print(my_list.index(30))


