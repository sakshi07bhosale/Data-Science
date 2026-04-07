#=====================append()=====================
#1. Write a program to add 10 user-entered integers into a list using append(). 
lst = []
for i in range(10):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)



#2. Append only even integers from 1 to 20 into a list.
lst = []
for i in range(1, 21):
    if i % 2 == 0:
        lst.append(i)
print(lst)

#3. Append the square of each integer from an existing list into a new list. 
lst = [1, 2, 3, 4]
squares = []
for i in lst:
    squares.append(i * i)
print(squares)

#4. Take integer input until the user enters `0` and append each value to a list.
lst = []
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    lst.append(num)
print(lst)

#5. Append elements of a tuple `(5, 10, 15)` one by one into a list.
lst = []
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    lst.append(num)
print(lst)

#======================clear()==========================

#1. Write a program to clear all elements from an integer list. 
lst = [1, 2, 3]
lst.clear()
print(lst)

#2. Clear a list only if it contains more than 5 integers. 
lst = [1, 2, 3, 4, 5, 6]
if len(lst) > 5:
    lst.clear()
print(lst)

#3. Display all elements of a list and then clear it. 
lst = [10, 20, 30]
print(lst)
lst.clear()
print(lst)

#4. Clear a list and then add 3 new integer values to it. 
lst = [1, 2, 3]
lst.clear()
lst.extend([4, 5, 6])
print(lst)

#5. Clear a list inside a function and print the list outside the function.
def clear_list(l):
    l.clear()

lst = [1, 2, 3]
clear_list(lst)
print(lst)


#==============================copy()=============================

#1. Copy all elements of one integer list into another list using copy(). 
a = [1, 2, 3]
b = a.copy()
print(b)

#2. Copy a list and add new integers to the copied list without affecting the original. 
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)

#3. Copy a list and remove an element from the copied list.
a = [10, 20, 30]
b = a.copy()
b.remove(20)
print(b)


#===============================count()========================

#1. Count how many times the integer 5 appears in a list. 
lst = [5, 1, 5, 3, 5]
print(lst.count(5))

#2. Count the occurrences of a user-entered integer in a list. 
lst = [1, 2, 3, 2, 2]
num = int(input("Enter number: "))
print(lst.count(num))

#3. Count how many times an even number appears in a list.
lst = [1, 2, 4, 5, 6]
count = 0
for i in lst:
    if i % 2 == 0:
        count += 1
print(count)


#===========================extend()===================

#1. Extend a list with another integer list entered by the user. 
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

#2. Extend a list using a tuple of integers. 
lst = [1, 2]
lst.extend((3, 4))
print(lst)

#3. Extend an empty list with integers from range 1 to 5.
lst = []
lst.extend(range(1, 6))
print(lst)


#==============================index()=================

#1. Find the index of a given integer in a list. 
lst = [10, 20, 30]
print(lst.index(20))

#2. Find the index of the first occurrence of integer 10 in a list. 
lst = [5, 10, 20, 10]
print(lst.index(10))

#3. Take an integer from the user and display its index in the list.
lst = [1, 2, 3, 4]
num = int(input("Enter number: "))
print(lst.index(num))

#====================insert()==================

#1. Insert an integer at the beginning of a list. 
lst = [2, 3]
lst.insert(0, 1)
print(lst)


#2. Insert an integer at a specific index entered by the user. 
llst = [1, 2, 3]
index = int(input("Enter index: "))
value = int(input("Enter value: "))
lst.insert(index, value)
print(lst)


#3. Insert the integer 100 at index 3.
lst = [1, 2, 3, 4, 5]
lst.insert(3, 100)
print(lst)



#====================pop()===============

#1. Remove the last integer from a list using pop(). 
lst = [1, 2, 3]
lst.pop()
print(lst)

#2. Remove the integer at index 2 using pop(). 
lst = [10, 20, 30, 40]
lst.pop(2)
print(lst)

#3. Pop all integers from a list one by one.
lst = [1, 2, 3]
while lst:
    print(lst.pop())


#=====================remove()===============

#1. Remove a specific integer value from a list. 
lst = [1, 2, 3]
lst.remove(2)
print(lst)


#2. Remove the first occurrence of integer 10 from a list. 
lst = [10, 20, 10, 30]
lst.remove(10)
print(lst)

#3. Remove all occurrences of a given integer from a list. 
lst = [5, 5, 3, 5]
num = int(input("Enter number: "))
while num in lst:
    lst.remove(num)
print(lst)


#====================reverse()====================
 
#1. Reverse an integer list using reverse(). 
lst = [1, 2, 3]
lst.reverse()
print(lst)

#2. Reverse a list of integers without creating a new list.
lst = [10, 20, 30]
lst.reverse()
print(lst)

#3. Reverse a list inside a function.
def reverse_list(l):
    l.reverse()

lst = [1, 2, 3]
reverse_list(lst)
print(lst)


#==================sort()====================

#1. Sort a list of integers in ascending order. 
lst = [5, 2, 9, 1]
lst.sort()
print(lst)


#2. Sort a list of integers in descending order. 
lst = [5, 2, 9, 1]
lst.sort(reverse=True)
print(lst)

#3. Sort a list and display the smallest integer.
lst = [8, 3, 5, 1]
lst.sort()
print("Smallest:", lst[0])






# =============================================================


#1. Create a set with 5 integer values and print it.
name={1,2,3,4,5}
print(name)

#2. Create a set using the set() constructor from a list.
name=["Sakshi",7,"Bhosale"]
s=set(name)
print(s)

#3. Create a set with duplicate values and print the result.
name={1,1,2,3,0,3,4}
print(name)

#4. Create a set containing True and 1. Print the set.
name={"1",1,True,"0",0,False}
print(name)


#5. Write a program to find the length of a set using len().
name={"1",1,True,"0",0,False}
print(len(name))

#6. Create a set with mixed data types and print it.
name={"Sakshi",20,True,20.3}
print(name)

#7. Write a program to access set elements using a for loop.
name={1,2,3,4,5}
for x in name:
    print(x)

#8. Create an empty set and add three elements using add().
name=set()
name.add("Sakshi")
name.add("Akshata")
name.add("Akanksha")
print(name)


#9. Write a program to remove an element from a set using discard().
name={'Akanksha', 'Sakshi', 'Akshata'}
name.discard("Akanksha")
print(name)


#10. Write a program to remove an element from a set using remove().
name={'Akanksha', 'Sakshi', 'Akshata'}
name.remove("Akanksha")
print(name)

#11. Write a program that removes a non-existing element using discard().
name={'Akanksha', 'Sakshi', 'Akshata'}
name.discard("Vaishnavi")
print(name)

#12. Write a progname={'Akanksha', 'Sakshi', 'Akshata'}
#name={'Akanksha', 'Sakshi', 'Akshata'}
#name.remove("Vaishnavi") #key error
#print(name)

#13. Write a program to remove a random element from a set using pop().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
name.pop()
print(name)

#14. Write a program to clear all elements from a set using clear().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
name.clear()
print(name)


#15. Write a program to delete a set completely using del.
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
del name

#16. Write a program to combine two sets using union().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno={1,2,3,4,5,6}
unionset=name.union(rollno)
print( "set of union:-",unionset)

#17. Write a program to combine two sets using the | operator.
id={6,7,8,9,}
rollno={1,2,3,4,5}
#unionset=id|rollno
print( "set of union:-",id|rollno)

#18. Write a program to update one set using another set with update().
id={6,7,8,9,}
rollno={1,2,3,4,5}
id.update(rollno)
print(id)

#19. Write a program to join a set with a list using union().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno=[1,2,3,4,5]
print(name.union(rollno))

#20. Write a program to join three sets using union().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno={1,2,3,4,5}
city={"nashik","Pune","Mumbai"}
print(name.union(rollno,city))

#21. Write a program to find common elements between two sets using intersection().
rollno={1,2,5,7,9,6}
id={4,5,3,9,}
#rollno.intersection(id)
print(rollno.intersection(id))

#22. Write a program to find common elements between two sets using the & operator.
rollno={1,2,5,7,9,6}
id={4,5,3,9,}
print(rollno & id)


#23. Write a program to find intersection between a set and a list using intersection().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno=[1,2,3,4,5]
intersectionset=name.intersection(rollno)
print(intersectionset)

#24. Write a program to update a set using intersection_update().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno=[1,2,3,4,5]
name.intersection_update(rollno)
print(name)

#25. Write a program to find elements present in first set but not in second using difference().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno=[1,2,3,4,5]
name.difference(rollno)
print(name)

#26. Write a program to find difference between two sets using the - operator.
rollno={1,2,5,7,9,6}
id={4,5,3,9,}
rollno-id
print(rollno)

#27. Write a program to update a set using difference_update().
rollno={1,2,5,7,9,6}
id={4,5,3,9,}
rollno.difference_update(id)
print(rollno)


#28. Write a program to find symmetric difference using symmetric_difference().
name={'Akanksha', 'Sakshi', 'Akshata','Vaishnavi','Dhanashree','Pooja'}
rollno=[1,2,3,4,5]
print(name.symmetric_difference(rollno))

#29. Write a program to find symmetric difference using the ^ operator.
rollno={1,2,5,7,9,6}
id={4,5,3,9,}
print(rollno^id)

#30. Write a program to perform union, intersection, difference, and symmetric difference on two sets and print all results.
a={1,2,3}
b={3,4,5}
print("Union:",a.union(b))
print("Intersection:",a.intersection(b))
print("Difference:",a.difference(b))
print("Symmetric_difference:",a.symmetric_difference(b))
