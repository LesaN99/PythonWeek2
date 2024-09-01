#!/usr/bin/python3

# #empty list
my_list = []

# #append to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Insertig value 15
my_list.insert(1, 15)
print(my_list)

#Extending 
my_list.extend([50, 60, 70])
print(my_list)

#Remove 
my_list.pop()
print(my_list)

#Sorting 
my_list.sort()
print(my_list)

#Index
index_of_30 = my_list.index(30)
print(index_of_30)



