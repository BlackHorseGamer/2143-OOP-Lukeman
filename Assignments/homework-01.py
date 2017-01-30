"""
Name: Robert Lukeman
Email: lukemanrobert@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: January 31st, 2017
"""

"""
Question A. What would Python print?
"""

"""
a = [1,5,4,2,3]
print(a[0], a[-1])
#Prints: 1 3
"""

"""
This prints the number in position 0 first, but then the -1 has to go to the far right
since theres nothing to the left of position 0.
"""

"""
a[4] = a[2] + a[-2]
print(a)
#Prints: [1, 5, 4, 2, 6]
"""

"""
What this does is similar to before. It focuses on what number is in position a[4], 
then gets the number in position a[2], which is four, then from a[0], a[-2] makes the 
program get the number in position a[3], adds them up, and replaces the number in 
position a[4] with the result.
"""

"""
print(len(a))
#Prints: 5
"""

"""
len stands for length, so this command displays how many elements are in the array.
"""

"""
print(4 in a)
#Prints: True
"""

"""
If the number is in one of the positions in the array, "True" is printed.
I tweaked it by temporarily replacing the 4 with a 7, which made the program print
"False."
"""

"""
a[1] = [a[1], a[0]]
print(a)
#Prints: [1, [5, 1], 4, 2, 6]
"""

"""
So what this does is replace the item in position a[1] with a new bracketed set of numbers
based on other positions.
"""

#Question B: Write a function that removes all instances of an element from a list.

"""
x = [3, 1, 2, 1, 5, 1, 1, 7]

def remove_all(el, lst):
  for i in lst:
    if el == i:
      lst.remove(i)
#This only removes so many instances of i, so only one remains.
  if el in lst:
    lst.remove(el)
#but THIS removes the last instance.

print(x)

remove_all(1, x)
print(x)
"""

#Question C: Write a function that takes two values, x and y, and a list, and adds as many
#y's to the end of the list as there are x's. Do not use the built-in function.


"""
z = [1, 2, 4, 2, 1]

print(z)

def add_this_many(x, y, lst):
  for i in lst:
#This checks every position in lst
    if i == x:
      lst.append(y)
#So given this code, every time x is fould in a position, y is appended in the end.
    
    
add_this_many(1, 5, z)

print(z)
"""
"""
#Question D: What would Python print?

a = [3, 1, 4, 2, 5, 3]

print(a[:4])
#Prints: [3, 1, 4, 2]
#This prints the numbers in the first four positions of the list

print(a)
#Prints: [3, 1, 4, 2, 5, 3]
#This prints the entirety of the list.

print(a[1::2])
#Prints: [1, 2, 3]
#This starts by printing the number at position a(1), then treks through the list printing
#the value every 2nd  position until the end of the list.

print(a[:])
#Prints: [3, 1, 4, 2, 5, 3]
#No numbers are specified, so again, the whole list is printed.

print(a[4:2])
#Prints: []
#The numbers are out of order, so it cant print any positions.

print(a[1:-2])
#Prints: [1, 4, 2]
#This prints the number in position a(1), then the numbers between it and a(-2)

print(a[::-1])
#Prints: [3, 5, 2, 4, 1, 3]
#Prints the list in its entirety since it assumes the numbers between the start and a(-1)
"""

#Question E: Reversing list order.

"""
x = [3, 2, 4, 5, 1]
print(x)

def reverse(lst):
  print(lst[::-1])

reverse(x)
"""

"""
#Question F: Rotating elements to the right by k.

x = [1, 2, 3, 4, 5]
print(x)

def rotate(lst, k):
  print (lst[k-1:] + lst[:k-1])
  
rotate(x, 3)
"""


"""
#Question H: Dictionaries. What would Python print?

superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}

superbowls['peyton manning'] = 1
#I dont know when the assignment was written, but this information is outdated.
#That 1 should really be 2, but I'll leave it as is just to be polite.

superbowls['joe flacco'] = 1

print('colin kaepernick' in superbowls)
#prints: False
#Colin Kaepernick was not found in the dictionary, so it returns false. Poor guy.

print(len(superbowls))
#Prints: 4
#Prints how many positions there are in superbowls

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False
#Peyton Manning doesn't have as many super bowl championships as Joe Montana.
#As such this is false.

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'peyton manning': 1, 'tom brady': 3, 'joe montana': 4, ('eli manning', 'giants'): 2, 'joe flacco': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 3: 'cat', 'joe flacco': 1, 'tom brady': 3, 'peyton manning': 1, 'joe montana': 4}

superbowls[('eli manning', 'giants')] = superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'peyton manning': 1, 3: 'cat', 'joe montana': 4, 'tom brady': 3, 'joe flacco': 1, ('eli manning', 'giants'): 5}
#Its addition. 4 plus 1 is 5. 
#This is adding the super bowls of Joe Montana and Peyton Manning together
#then putting the result in Eli Manning's position.

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {'joe montana': 4, 'peyton manning': 1, 'tom brady': 3, 3: 'cat', 'joe flacco': 1, ('eli manning', 'giants'): 5, ('steelers', '49ers'): 11}
"""


#Question I: Replace all occurences of x as the value with y.

"""
d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
print(d)

d[1] = {2:1, 3:4}
d[2] = {4:4, 5:1}
    

  
print(d)

"""


#Question J: Delete all occurences

"""
d = {1:2, 2:3, 3:2, 4:3}
print(d)

def rm(c, x):
  if x == c[1]:
    del c[1]
  if x == c[2]:
    del c[2]
  if x == c[3]:
    del c[3]
  if x == c[4]:
    del c[4]

rm(d,2)

print(d)
"""
#Looping doesn't work for this one
