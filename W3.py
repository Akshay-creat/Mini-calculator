# a = "pyhton"
# print(a)

# x = float(1)
# y = int(2.8)
# z = complex(1)

# print(type(x))
# print(type(y))
# print(type(z))

# list =list(("apple","banana","cherry"))
# print(list)

# list = ["apple","banana","cherry"]

# print(list[1])

# list = ["apple","banana","cherry"]
# print(list[0:])

# list = ["apple","banana","cherry"]
# list[1]="black current"
# print(list)

# list = ["apple","banana","cherry"]
# list.insert(2,"watermelon")
# print(list)

# list = ["apple","banana","cherry"]
# list.append("orange")
# print(list)

# list = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# list.extend(tropical)
# print(list)

# list = ["apple","banana","cherry"]
# list.remove("banana")
# print(list)

# list = ["apple","banana","cherry"]
# list.pop(1)
# print(list)

# list = ["apple","banana","cherry"]
# list.pop(1)
# print(list)

# list = ["apple","banana","cherry"]
# list.clear()
# print(list)

# list = ["apple","banana","cherry"]
# for x in list:
#     print(x)

# list = ["apple", "banana", "cherry"]
# for i in range(len(list)):
#     print(list[i])

# list = ["apple", "banana", "cherry"]
# i = 0
# while i<len(list):
#     print(list[i])
#     i += 1

# list = ["apple", "banana", "cherry"]
# [print(x)for x in list]

#list comprehension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
#         print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if 'a' in x]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x != 'apple']
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ["hello" for x in fruits ]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = fruits.copy()
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = list(fruits)
# print(newlist)

#Joining lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

#Accessing tuples
# fruits = ("a", "b", "c")
# print(fruits[1])

# fruits = ("a", "b", "c")
# print(fruits[0:3])

# fruits = ("a", "b", "c")
# if "a" in fruits:
#     print("a present in fruits")

# x = ('apple','banana',"cherry")
# y = list(x)
# y[1]= "kiwi"
# x = tuple(y)
# print(x)

# x = ('apple','banana','cherry')
# y = ('orange',)

# x += y

# print(x)

# thistuple =  ('apple','banana','cherry')
# y = list(thistuple)
# y.remove('apple')
# thistuple = tuple(y)
# print(thistuple)

# thistuple =  ('apple','banana','cherry')
# del thistuple
# print(thistuple)

#Unpacking
# fruits =  ('apple','banana','cherry')

# (green,yellow,red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green,yellow,*red) = fruits

# print(green)
# print(yellow)
# print(red)

# thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
# for x in thistuple:
#     print(x)

# thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
# for i in range(len(thistuple)):
#     print(thistuple[i])

# thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i += 1

#join tuples
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# thistuple = fruits* 2
# print(thistuple)

#Sets
# thisisset = {"apple", "banana", "cherry",}
# for x in thisisset:
#     print(x)

# thisisset = {"apple", "banana", "cherry",}
# print('banana'in thisisset)

# thisset = {"apple", "banana", "cherry",}
# thisset.remove("banana")
# print(thisset)

# thisset =  {"apple", "banana", "cherry",}
# thisset.discard("banana")
# print(thisset)
#discard will not return an error if banana does not exist

# thisset =  {"apple", "banana", "cherry",}
# for x in thisset:
#     print(x)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# myset = set1 | set2
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 | set4

# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1) 

# thisdict = dict(name = "akshay", age = 24, country = "norway")
# print(thisdict)

