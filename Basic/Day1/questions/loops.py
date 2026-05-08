# 1. Write a program to check whether a number is positive or negative.
num = int(input("Enter any number:-"))
if num >= 0:
    print(f"{num}  is positive number")
else:
    print(f"{num}  is negative number") 


#  2. Write a program to check if a number is greater than 100.
num = int(input("Enter any number:-"))
if num > 100:
    print(f"{num}  is greater than 100")
else:
    print(f"{num}  is not  greater than 100") 


# 3. Write a program to check whether a given number is even or odd.
num = int(input("Enter any number:-"))
if num % 2 == 0:
    print(f"{num}  is even number")
else:
    print(f"{num}  is odd number") 


# 4. Write a one-line if statement to check if a number is less than 50.
num = int(input("Enter any number:-"))
if num <= 50: print("less than 50")


# 5. Write a program to check whether a person is eligible to vote (age ≥ 18).
age = int(input("Enter your Age:-"))
if age >= 18:
    print("Person is eligible for the voting")
else:
    print("Person is  not eligible for the voting")
    

# 6. Write a program to check whether a number is positive, negative, or zero.
num = int(input("Enter any number:-"))
if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is a negative number")
else:
    print("zero")


# 7. Write a program to check the largest of two numbers.
num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))
if num1 > num2:
    print(f"num1 {num1} is greater")
else:
    print(f" num2 {num2} is greater")
    


# 8. Write a program to check the largest of three numbers using if-elif.
num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))
num3 = int(input("Enter third number:-"))
if num1 > num2 and num2 >num3:
    print(f" num1 {num1} is greater")
elif num2 > num3 and num2 >num1:
    print(f" num2 {num2} is greater")
else:
    print(f"num3 {num3} is greater")


# 9. Write a program to check whether a year is a leap year.
year = int(input("Enter year: "))
if year % 4 == 0 :
    print("Leap Year")
else:
    print("Not a Leap Year")


# 10. Write a program to check if a student passed or failed (marks ≥ 40).
marks = int(input("Enter your marks:-"))
if marks >= 40:
    print("pass")
else:
    print("fail")



# 11. Write a program to assign grades:
#        ≥90 → A
#        ≥75 → B
#        ≥60 → C
#        Else → Fail

marks = int(input("Enter your marks:-"))
if marks >=90:
    print("A")
elif marks >=75:
    print("B")
elif  marks >=60:
    print("C")
else:
    print("Fail")

# 12. Write a program to check whether a number lies between 10 and 50 using and.
num = int(input("Enter number: "))
if num >= 10 and num <= 50:
    print("Between 10 and 50")
else:
    print("Not in range")


# 13. Write a program to check whether at least one condition is true using or.
num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))
if num1 > num2 or num1 < num2:
    print("Condition true")
else:
    print("Condition false")

# 14. Write a program to check login:
#         username = "admin"
#         password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")


# 15. Write a program to check if a number is divisible by 3 and 5.
num = int(input("Enter number: "))
if num % 3 == 0 and num %5 == 0:
    print(f"number {num} is divisible by 3 and 5")
else:
    print(f"number {num} is not divisible by 3 and 5")


# 16. Write a nested if program to check:
#         gender = female
#         age ≥ 18 → Can vote

gender = input("Gender:")
age = int(input("Age:"))
if gender == "female" or "Female" :
    if age >= 18:
        print("Can vote")
    else:
        print("Can't vote")
        

# 17. Write a program to check whether a character is a vowel or consonant.
ch = input("Enter any Character:-")
if ch in "aeiouAEIOU" :
    print("Vowel")
else:
    print("Consonant")


# 18. Write a one-line if-else to check pass/fail.
marks = int(input("Enter your marks:-"))
print("Pass") if marks >= 35 else print("Fail")


# 19. Write a program using not operator to reverse a condition.
a = 10
if not a > 20:
    print("Condition reversed")


# 20. Write a program that uses pass inside an if block and print “Thank you” in else.
num = int(input("Enter number: "))
if num > 0:
    pass
else:
    print("Thank you")



# 21. Write a program using match to print the day name for numbers 1–7.
day = int(input("Enter day number: "))
match day:
    case 1:
     print("Monday")
    case 2: 
     print("Tuesday")
    case 3:
     print("Wednesday")
    case 4:
     print("Thursday")
    case 5:
     print("Friday")
    case 6:
     print("Saturday")
    case 7:
     print("Sunday")



# 22. Write a program using match to build a simple calculator (+, -, *, /).
a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter operator: ")

match op:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*': 
        print(a * b)
    case '/':
        print(a / b)



# 23. Write a program to categorize age:
#         <13 → Child
#         13–19 → Teen
#         20–59 → Adult
#         60+ → Senior

age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


# 24. Write a program using match to check month name from month number.
month = int(input("Enter number of month:"))
match month:
    case 1:
     print("January")
    case 2:
     print("February")
    case 3:
     print("March")
    case 4:
     print("April")
    case 5:
     print("May")
    case 6:
     print("June")
    case 7:
     print("July")
    case 8:
     print("August")
    case 9:
     print("September")
    case 10: 
     print("October")
    case 11: 
     print("November")
    case 12:
     print("December")



# 25. Write a program using a match with a default case and print “Month number is not present”.
month = int(input("Enter number of month:"))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6: print("June")
    case 7: print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Month number is not present")


# 26. Write a program to check traffic signal colors and print actions.
signal = input("Enter signal color (eg. red,yellow,green):")

if signal == "red" or "Red" or "RED":
    print("Stop")
elif signal == "yellow" or "Yellow" or "YELLOW":
    print("Wait")
elif signal == "green" or "Green" or "GREEN":
    print("Go")


# 27. Write a program using match to classify student group based on name list.
name = input("Enter name (eg. Amit,Rahul,Sita,gita): ")

match name:
    case "Amit" | "Rahul"| "amit" | "rahul":
        print("Group A")
    case "Sita" | "Gita" | "Sita" | "Gita":
        print("Group B")
    case _:
        print("No group")



# 28. Write a program to check eligibility for a job:
#         Age ≥ 21
#         Degree = Yes
#         Experience ≥ 1 year

age = int(input("Enter age: "))
degree = input("Degree (yes/no): ")
exp = int(input("Experience: "))

if age >= 21 and degree == "yes" or "Yes" or "YES" or "y" or "Y" and exp >= 1:
    print("Eligible for job")
else:
    print("Not eligible")



# 29. Write a program using match with multiple values in one case.
num = int(input("Enter number: "))

match num:
    case 1 | 3 | 5:
        print("Odd number")
    case 2 | 4 | 6:
        print("Even number")
    case _:
        print("Other number")

# ===
name = "SAKSHI"
for i in name:
    print(i)

    # =======

    rollno = [1,2,3,4,5,6]
for i in rollno:
    print(i)

    # ======
    name = "SAKSHI💕"
for i in range(0,101):
    print(name,end=" ")


    # ====
    for i in range(0,100,2):
         print(i,end=" ")



