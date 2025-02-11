#accessing dictionaries
# thisdict = {"brand": "ford",
#             "model":"mustang",
#             "year":1994}
# print(thisdict["model"])

# thisdict = {"brand": "ford","model":"mustang",
#             "year":1994}
# x = thisdict.get("model")
# print(x)

# thisdict = {"brand": "ford","model":"mustang",
#              "year":1994}
# thisdict.keys()
# thisdict['color'] = 'black'
# print(thisdict)

# thisdict = {"brand": "ford","model":"mustang",
#               "year":1994}
# x = thisdict.values()
# print(x)

# thisdict = {"brand": "ford","model":"mustang",
#                "year":1994}
# x = thisdict.items()
# print(x)

# thisdict = {"brand": "ford","model":"mustang",
#                 "year":1994}
# if 'model' in thisdict:
#     print("yes")

# thisdict = {"brand": "ford","model":"mustang",
#                  "year":1994}

# thisdict.update({'year' : 2020})
# print(thisdict)

# thisdict = {"brand": "ford","model":"mustang",
#                  "year":1994}
# thisdict.pop('model')
# print(thisdict)

# thisdict = {"brand": "ford","model":"mustang",
#                  "year":1994}
# thisdict.popitem()
# print(thisdict)


#Looping through lists
# thisdict = {"brand": "ford","model":"mustang",
#             "year":1994}
# for x in thisdict:
#     print(x)

# thisdict = {"brand": "ford","model":"mustang",
#             "year":1994}
# for x in thisdict:
#     print(thisdict[x])

# thisdict = {"brand": "ford","model":"mustang",
#          "year":1994}
# for x,y in thisdict.items():
#     print(x,y)

# thisdict = {"brand": "ford","model":"mustang",
#          "year":1994}
# x = thisdict.copy()
# print(x)

#Nested dictionaries
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily["child2"]["name"])

#if else 
# a = 20
# b = 200
# if b > a:
#     print("b is greater than a")

# a = 33
# b = 33
# if a > b:
#     print("a is greater than b")
# elif(a == b):
#     print("a is equal to b")   

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 200
# b = 33
# if a > b: print("a is greater than b")

# a = 2
# b = 300
# print('a')if a > b else print('b')

# a = 330
# b = 330
# print('a') if a >b else print('=')if a == b else print('b')

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print('both conditions are true')

# a = 200
# b = 33
# c = 500
# if a>b or c>b:
#     print('atleast one condition is true')

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

# x = 41 
# if x > 30:
#     print('above ten')
# if x > 40:
#     print('also above 40')
# else:
#     print('not above 50')

# a = 33
# b = 200
# if b > a:
#     pass

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# fruits = ['apple','banana','cherry']
# for x in fruits:
#     if x == 'banana':
#         break
#     print(x)

# fruits = ['apple','banana','cherry']
# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2,30,3):
#     print(x)

# for x in range(6):
#     print(x)
# else:
#     print('finally finished')

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:

#Python classes and objects
# class Myclass:
#     x = 5

# print(Myclass)
# p1 = Myclass()
# print(p1.x)

# built in init functions
#  _in_it()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)