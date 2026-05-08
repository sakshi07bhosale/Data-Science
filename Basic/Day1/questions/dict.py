#1.Create a dictionary with keys name, rollNo, and address and print it.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu)

#2.Write a program to access and print the value of key name from a dictionary.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu["name"])

#3.Create a dictionary and print its length using len().
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(len(stu))

#4.Write a program to check the type of a dictionary using type().
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(type(stu))

#5.Create a dictionary with two keys and print all its values
stu={
   "name":"Sakshi",
   "address":"Nashik"
}
print(stu.values())

#6.Create a dictionary and access values using both [] and get() methods.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu["name"])
print(stu.get("rollno"))

#7.Write a program to add a new key-value pair to an existing dictionary.
stu={
   "name":"Sakshi",
   "address":"Nashik"
}
stu["rollno"]=10
print(stu)

#8.Create a dictionary and update one value using the update() method.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu.update({"stuId":11})
print(stu)

#9.Write a program to remove a key using the pop() method.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu.pop("rollno")
print(stu)

#10.Create a dictionary and remove the last inserted item using popitem().
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu.popitem()
print(stu)

#11.Write a program to print all keys using the keys() method.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu.keys())

#12.Write a program to print all values using the values() method.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu.values())

#13.Create a dictionary and print all key-value pairs using items().
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu.items())

#14.Convert a tuple of key-value pairs into a dictionary using dict().
stu =(("name","Sakshi"),("rollno",10),("address","Nashik"))
tupleTodict = dict(stu)
print(tupleTodict)

#15.Write a program to check if a key exists in a dictionary.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
if "name" in stu:
    print(True)
else:
    print(False)

#16.Create a dictionary with duplicate keys and print the output.
stu={
   "name":"Sakshi",
   "rollno":10,
   "rollno":11,
   "rollno":12,
   "rollno":13,
   "rollno":14,
   "address":"Nashik"
}
print(stu)

#17.Write a program to delete a specific key using the del keyword.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
del stu["rollno"]
print(stu)

#18.Write a program to delete the entire dictionary using del.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
del stu

#19.Create a dictionary and empty it using the clear() method.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu.clear()
print(stu)

#20.Copy a dictionary using the copy() method and show both dictionaries.
stu1={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu2=stu1.copy()
print("Student 2 data:-",stu2)

#21.Copy a dictionary using the dict() constructor and modify the original dictionary.
stu1={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu2= dict(stu1)
stu1["a"]=100
print("original:", stu1)
print("copy:",stu2)

#22.Write a program to demonstrate why dict1 = dict2 is not a proper copy.
stu1={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu2= stu1
stu1["a"]=100
print("stu1:", stu1)
print("stu2:",stu2)

#23.Create a dictionary and add multiple items using assignments.
stu={}
stu["name"]="Sakshi"
stu["rollno"]=10
stu["address"]="Nashik"
print(stu)

#24. Write a program to remove multiple keys one by one using pop().
stu1={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu.pop("name")
stu.pop("rollno")
print(stu)

#25.Use fromkeys() to create a dictionary with default values.
keys = ["a", "b", "c"]
name = "sakshi"
d = dict.fromkeys(keys, name)
print(d)


#26. Write a program to access a missing key using get() without error.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print(stu.get("stuId"))

#27. Create a dictionary and print key-value pairs in tuple form.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
dictTotuple = stu.items()
print(dictTotuple)


#28. Write a program to update multiple values using update().
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
stu.update({"name":"Akshata","rollno":11,"address":"Pune"})
print(stu)

#29. Create a dictionary and check membership of a key using in.
stu={
   "name":"Sakshi",
   "rollno":10,
   "address":"Nashik"
}
print("name" in stu)
print("address" in stu)

#30. Write a program that creates a dictionary from tuples and accesses values using keys.
stu =(("name","Akshata"),("rollno",10),("address","Nashik"))
tupleTodict = dict(stu)
print(tupleTodict["name"])
print(tupleTodict["address"])

