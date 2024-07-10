# write a program to create a dictionary of hindi words with values as their english translation. Provides user  with a  option to lool it up!

# words = {
#     "madad " : "Help",
#     "kursi" : "Chair",
#     "billi": " cat"
# }

# word = input("Enter the word which you wnat translation :")

# print(words[word])


# 2 --->>  write a program to input eight number from the user and display all the unique number(once).

# s = set()
# n = input("Enter number 1 :")
# s.add(int(n))
# n = input("Enter number 2 :")
# s.add(int(n))
# n = input("Enter number 3 :")
# s.add(int(n))
# n = input("Enter number 4 :")
# s.add(int(n))
# n = input("Enter number 5 :")
# s.add(int(n))
# n = input("Enter number 6 :")
# s.add(int(n))
# n = input("Enter number 7:")
# s.add(int(n))
# n = input("Enter number 8 :")
# s.add(int(n))

# print(s)


#3-------->>>>   can we have a set with 18(int) and '18' (str) as a value in it?
# s = set()
# s.add(18)
# s.add("18")
# print(s)



#4 . --------->>>>>  what will be the length of following set s :

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')  # length of s after these operation?


# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')

# print(s)


# 5 . --------->>>>>   s= {}

# what is the type of s ?

s = {}
print(type(s))   #  dicitonary


# 6 . ------->>>>>create an empty dictionary. Allow 4 friends to enter their favorite language as value and use as their names. Assume that the names are unique.

# d = {}

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# print(d)

#7..---------->>>>>  if the names of 2 friends are same: what will happen to the program in problem 6?


# d = {}

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# print(d)



#  8...---------->>>>> if the languages of 2 friends are same: what will happen to the program in problem 6?



# d = {}

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# name = input("Enter the name:")
# lang = input("enter language:")
# d.update({name:lang})

# print(d)




# 9 ., ------------>>>>>  can you change the values inside a list which is contained in set s?
# s = {8,7,12,"harry",[1,2]}

# No, you cannot change the values inside a list that is contained in a set because sets in Python can only contain immutable (hashable) elements. Lists are mutable and therefore cannot be elements of a set. If you try to create such a set, it will raise a TypeError.

