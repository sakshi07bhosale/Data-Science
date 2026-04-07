#Q1.create a tuple with 3 fruits and print it.
Fruits=("Apple","Banana","Mango")
print(Fruits)

#Q2.create tuple with on item Python an print its type
name=("Python")
print(type(name)) 

#Q3.create a tuple of 5  numbers and print its length using len()
t=(1,2,3,4,5)
print(len(t))

#Q4.create a tuple and print its first element using indexing
t=(1,2,3,4,5)
print(t[0])

#Q5.create a tuple and print its last element using negative indexing
t=(1,2,3,4,5)
print(t[-1])

#Q6.create a tuple using the tuple()constructor with values 1 to 5 and print it
num = tuple(range(1,6))
print(num)

#Q7.Given t=(10,20,30,40,50) print element at index 1 and 3
t=(10,20,30,40,50)
print(t[1])
print(t[3])

#Q8.Given t=("a","b","c","d","e") print element from  1 to 4 using slicing
t=("a","b","c","d","e")
print(t[1:5])

#Q9. From a tuple t = (5,10,15,20,25,30) , print elements from index 2 to end.
t = (5,10,15,20,25,30)
print(t[2:])

#Q10. From a tuple t = (5,10,15,20,25,30) , print elements from start to index 3.
t = (5,10,15,20,25,30)
print(t[:4])

#Q11. Create a tuple with mixed data types (int, float, string, boolean) and print it.
t=(10,37.800,"Sakshi",True)
print(t)

#Q12. Check whether Python exists in a given tuple and print the result.
lang=("c","Java","Python","c++","SQL")
print("Python" in lang)

#Q13. Convert a tuple to a list, add a new element, and print the updated list.
t=(1,2,3,4)
li=list(t)
print(type(li))
li.append(5)
print(li)


#Q14. Convert a list back into a tuple and print it.
li = [1, 2, 3, 4,5]
t = tuple(li)
print(t)


#Q15. Create two tuples and concatenate them using += operator.
t1=(1,2,3)
t2=(4,5,6)
t1 += t2
print(t1)

#Q16. Convert a tuple to list, change the second element, and convert back to tuple.
t = (10, 20, 30)
l = list(t)
l[1] = 25
t = tuple(l)
print(t)

#Q17. Create a tuple and access elements using both positive and negative indexing.
t=(10,20,30,40,50,60,70,80,90,100)
print(t[0])
print(t[-1])

#Q18. Create a tuple of 7 elements and print its middle element.
t=(10,20,30,40,50,60,70,80,90,100)
print(t[len(t)//2])


#Q19. Create a tuple and try to change one value directly (observe and write the error).
#t = (1, 2, 3)
#t[0] = 10   # TypeError: 'tuple' object does not support item assignment


#Q20. Write a program that takes a tuple, converts it to list, replaces the last element, and converts back to tuple.
t = (10, 20, 30)
l = list(t)
l[-1] = 40
t = tuple(l)
print(t)


#Q21. Create a tuple of 10 numbers and extract the middle 5 elements using slicing.
t = (1,2,3,4,5,6,7,8,9,10)
print(t[2:7])


#Q22. Write a program to check if a value exists in a tuple before accessing its index.
t = (10, 20, 30)
if 20 in t:
    print(t.index(20))
    
    
#Q23. Create a tuple, convert it to list, remove one item, and convert it back to tuple.
t = (1, 2, 3)
l = list(t)
l.remove(2)
t = tuple(l)
print(t)


#Q24. Write a program that accepts a tuple, converts it to list, inserts a value at index 2, and converts back to tuple.
t = (1, 2, 4)
l = list(t)
l.insert(2, 3)
t = tuple(l)
print(t)


#Q25. Create a tuple and demonstrate slicing with positive and negative indexes in one program.
t = (1,2,3,4,5,6)
print(t[1:4])
print(t[-5:-2])


#Q26. Write a complete program that :-
#creates a tuple
#prints its length
# accesses elements
# slices it
# converts to list
# updates a value
# converts back to tuple
t = (10, 20, 30, 40)
print(len(t))
print(t[1])
print(t[1:3])
l = list(t)
l[2] = 35
t = tuple(l)
print(t)


#Q27. Write a program that takes two tuples, adds them, and prints the final result.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)


#Q28. Create a tuple, delete it using del , and then try to print it (observe the error).
#t = (1, 2, 3)
#del t
#print(t)   # NameError


#Q29. A school stores a student’s basic details in a tuple because the data should not be changed accidentally.
 #      The tuple contains: student = ("Rahul", 10, "A", 85.5)
   #    Write a program to:
# Print the student’s name and class using indexing.
student = ("Rahul", 10, "A", 85.5)
print(student[0])
print(student[1])

# Check whether "A" exists in the tuple.
print("A" in student)

# Convert the tuple into a list, change the marks (85.5 → 90.0), and convert it back into a tuple.
l = list(student)
l[3] = 90.0
student = tuple(l)

# Print the final updated tuple.
print(student)

#Q30. A customer’s selected product prices are stored in a tuple:
  #    prices = (250, 500, 750, 1000, 1250)
   #    Write a program to:
#1. Print the total number of items using len().
prices = (250, 500, 750, 1000, 1250)
print(len(prices))

#2. Print the first and last price using positive and negative indexing.
print(prices[0],prices[-1])

#3. Extract the middle three prices using slicing.
print(prices[1:4])

#4. Convert the tuple into a list, add a new price 1500, and convert it back into a tuple.
l = list(prices)
l.append(1500)
prices = tuple(l)

#5. Print the final tuple.
print(prices)