#Q1. Write a Python program to create a list of 5 student names and print it.
name=["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
print(name)

#Q2.Write a program to find the length of a list using len().
name=["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
print(len(name))

#Q3.Create a list with mixed data types and print all elements one by one.
list=["Sakshi",2,True,7.5]
for item in list:
    print(list)

#Q4.Write a program to access the first and last element of a list.
name=["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
print(name[0])    #first
print(name[-1])   #last

#Q5.Create a list and print the element using negative indexing.
name=["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
print(name[-2]) 


#Q6.Write a program to check whether "Chetan" exists in a list.
names=["Ganesh","Chetan","Sarthak"]
if "Chetan" in names:
    print("Chetan exists")
else:
    print("Not found")
    
#Q7.Write a program to change the second element of a list.
name=["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
name[1]="Dhanashree"
print(name)

#Q8.Create an empty list and append three values to it.
name=[]
name.append("Sakshi")
name.append("Akshata")
name.append("Dhanashree")
print(name)

#Q9.Write a program to remove the last element from a list.
name=["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
name.pop()
print(name)

#Q10.Create a list and clear all its elements using a method.
name = ["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha"]
name.clear()
print(name)

#Q11.Write a program to slice a list from index 2 to 5.
name = ["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha","Dhanashree","Gaytri"]
print(name[2:5])

#Q12.Write a program to replace the first two elements of a list using range assignment.
name = ["Sakshi","Akshata","Vaishnavi","sneha","Aakanksha","Dhanashree","Gaytri"]
name[0:2]=["Ganesh","Sarthak"]
print(name)

#Q13.Create two lists and join them using the + operator.
list1=[1,2,3]
list2=[4,5,6]
list=list1+list2
print(list)

#Q14.Write a program to insert an element at index 3 in a list.
lst = [1, 2, 3, 5]
lst.insert(3, 4)
print(lst)

#Q15.Write a program to extend a list using:
# another list
list1=["sakshi","Akshata"]
list2=["Dhanu","Mauu"]
list1.extend(list2)
print(list1)

#a tuple
lst = [1, 2]
t = (3, 4)
lst.extend(t)
print(lst)


#Q16.Write a program to remove a specific value from a list using remove().
list=[1,2,3,4,5]
list.remove(2)
print(list)

#Q17.Write a program to sort a list of integers in ascending order.
list=[4,5,3,2,1]
list.sort()
print(list)

#Q18.Write a program to sort a list of integers in descending order.
list=[4,5,3,2,1]
list.sort(reverse=True)
print(list)

#Q19.Write a program to reverse a list using an inbuilt method.
list=[4,5,3,2,1]
list.reverse()
print(list)

#Q20.Write a program to copy a list using the copy() method and show that changes in the original list do not affect the copied list.
lst1 = [1, 2, 3]
lst2 = lst1.copy()
lst1.append(4)
print(lst1)
print(lst2)


#Q21.Write a program to extend a list using a dictionary and print the result.
st = [1, 2]
d = {3: "a", 4: "b"}
lst.extend(d)
print(lst)


#Q22.Write a program to demonstrate that list2 = list1 creates a reference, not a copy.
list1 = [1, 2, 3]
list2 = list1

list1.append(4)
print(list1)
print(list2)

#Q23.Write a program to sort a list containing both uppercase and lowercase letters alphabetically.
lst = ["b", "A", "d", "C"]
lst.sort()
print(lst)


#Q24.Write a program to sort a list containing uppercase and lowercase letters together using key=str.lower.
lst = ["b", "A", "d", "C"]
lst.sort(key=str.lower)
print(lst)

#Q25.Write a program to remove the element at index 4 using pop().
lst = [10, 20, 30, 40, 50, 60]
lst.pop(4)
print(lst)

#Q26.Write a program to delete the third element of a list using the del keyword.
lst = [1, 2, 3, 4]
del lst[2]
print(lst)


#Q27.Write a program to count how many times a specific value occurs in a list.
lst = [1, 2, 2, 3, 2]
print(lst.count(2))

#Q28.Write a program to find the index of a specific element in a list.
list=[10,20,30,40,50]
list=list.index(20)
print(list)

#Q29.Write a program to add elements of a set to a list using extend().
lst = [1, 2]
s = {3, 4}
lst.extend(s)
print(lst)


#Q30.Write a program that performs the following operations on a list
#append
#insert
#remove
#sort
# reverse
lst = [3, 1, 2]

lst.append(4)
lst.insert(1, 10)
lst.remove(1)
lst.sort()
lst.reverse()
print(lst)
