# Q1.Store your name in a string variable and print it using f-string.
name ="Sakshi"
address ="Kopergoan"
print(f"My name is {name} i am from {address}")

#Q2.Print your city name using string concatenation.
name = "Sakshi"
city = "Pune"
print( "my name is \t" + name + " \nMy city is " + city)

 #Q3. Print: "Hello" and "World" on two separate lines using escape character.
str1="Hello"
str2="World"
print("Hello\nWorld")

#Q4.Print a sentence that contains a single quote using escape character.
print('It\'s a beautiful day')

#Q5.Print a tab space between two words using escape character.
print("Python\tProgramming")

#Q6.Check and print the boolean value of 100.
num=100
print(bool(num))

#Q7.Check and print the boolean value of 0.
num=0
print(bool(num))

#Q8.Compare two numbers and print whether first is greater than second.
num1=10
num2=20
print(num1>num2)

#Q9.Add two numbers and print the result.
a=12
b=10
result= a+b
print(result)

#Q10.Multiply two numbers and print the result.
a=12
b=10
result= a*b
print(result)

#Q11.Find remainder of 25 divided by 4.
a=25
b=4
result= a%b
print(result)

#Q12.Use += operator to increase a variable by 10.
a=100
a += 10
print(a)

#Q13.Use -= operator to decrease a variable by 5.
a=100
a -= 5
print(a)

#Q14.Compare two numbers using == operator and print result.
num1=20
num2=30
print(num1==num2)

#Q15.Use logical and to check if a number is greater than 10 and less than 20.
num1=15
print(num1 >10 and num1 <20)

#Q16.Take two numbers from user and print sum, difference, product, and division.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Sum:", n1 + n2)
print("Difference:", n1 - n2)
print("Product:", n1 * n2)
print("Division:", n1 / n2)

#Q17.Print a formatted string that includes name and age using f-string.
name="Sakshi"
age=20
print(f"my self {name} and i am {age} years old")

#Q18.Check whether a number entered by user is greater than 50 and print True/False.
num=int(input("Enter any number:"))
num= num>50
print(num)

#Q19.Use logical or to check if a number is less than 10 or greater than 100.
num=int(input("Enter any Number:"))
print(num <10 or num >100)

#Q20.Use logical not to reverse a comparison result.
num=int(input("Enterr any Number:"))
print(not num >100)

#Q21.Use identity operator is to compare two variables referencing same list.
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)

#Q22.Use identity operator is not to compare two different lists.
list1 = [1, 2, 3]
list2 = list2
print(list1 is not list2)

#Q23.Perform bitwise AND on two numbers 5 and 3.
num1=5
num2=3
print(num1 & num2)

#Q24.Perform bitwise OR on two numbers 7 and 4.
num1=7
num2=4
print(num1 | num2)

#Q25.Perform bitwise XOR on two numbers 6 and 2.
num1=7
num2=4
print(num1 ^ num2)

#Q26.Take three numbers and evaluate: a + b * c - a // b ** 2
a=10
b=20
c=30
result=a + b * c - a // b ** 2
print(result)

#Q27.Take a number from user and check:
#It is greater than 10
#it is even
 # Print result using logical and.
num=int(input("Enter any number:")) 
print(num >10)
print(num % 2 == 0)
print( num >10 and num % 2 == 0)

  
#Q28.Create two lists, assign one list to another variable, then check identity using is and print result
l1 = [10, 20]
l2 = l1
print(l1 is l2)

#Q29.Take two integers, convert them to binary using bitwise operations, then perform AND, OR, and XOR and print results.
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
print("Binary AND:", x & y)
print("Binary OR:", x | y)
print("Binary XOR:", x ^ y)


#Q30. Write a program that:
# Takes two numbers
# Uses arithmetic, comparison, logical, and assignment operators in one program
# Prints at least 6 different outputs.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Greater than:", a > b)
print("Logical AND:", a > 0 and b > 0)

a += 5
print("After +=5:", a)

print("Multiplication:", a * b)
print("Equality:", a == b)
