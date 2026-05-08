#Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i,end=" ")



#Print all even numbers between 1 and 20.
for i in range(1,21):
    if i % 2 ==0:
       print(i,end=" ")



#Print all odd numbers from 1 to 15.
for i in range(1,21):
    if i % 2 !=0:
       print(i,end=" ")



#Print the square of numbers from 1 to 5.
for i in range(1,6):
    print(i*i,end=" ")



#Print the sum of first 10 natural numbers.
sum=0
for i in range(1,11):
    sum+=i
print(sum)



#Print the multiplication table of 5.
for i in range(1,11):
    print(5*i,end=" ")


#Count how many numbers are divisible by 3 between 1 and 50.
for i in range(1,51):
        if i % 3 == 0:
           print(i,end=" ")

#Find the sum of numbers from 1 to 10.
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)
#Print each character of a string on a new line.
s = input("Enter string:")
for ch in s:
    print(ch)
#Count how many vowels are present in a given string.
s = input("Enter string: ")
count = 0
for ch in s:
    if ch in "aeiou" :
        count += 1
print("Vowels:", count)


#Print only uppercase letters from a string.
s = input("Enter string: ")
for ch in s:
    if ch.isupper():
        print(ch)

        #Reverse a string using a for loop.
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


#Count digits and letters separately in a string.
s = input("Enter string: ")
digits = letters = 0
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
print("Digits:", digits)
print("Letters:", letters)


#Find the largest number in a list.
lst = [10, 5, 25, 8]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("Largest:", largest)

#Find the smallest number in a list.
lst = [10, 5, 25, 8]
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print("Smallest:", smallest)

#Count how many even and odd numbers are in a list.
lst = [1, 2, 3, 4, 5]
even = odd = 0
for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)

#Print duplicate elements from a list.
lst = [1, 2, 3, 2, 4, 1]
duplicates = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)

#Count how many times a given number appears in a list
lst = [1, 2, 3, 2, 2, 4]
num = int(input("Enter number: "))
count = 0
for i in lst:
    if i == num:
        count += 1
print("Count:", count)

#Print numbers greater than the average of a list.
lst = [10, 20, 30, 40]
avg = sum(lst) / len(lst)
for i in lst:
    if i > avg:
        print(i)

#Check whether a number is prime using a for loop.
num = int(input("Enter number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")

    else:
        print("Prime")
else:
    print("Not Prime")

#Print prime numbers between 1 and 50.
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


#Print a multiplication table of a given number
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#Find the factorial of a number using a for loop.
n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

#Check whether a string is a palindrome.
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Count words in a sentence using a for loop.
s = input("Enter sentence: ")
count = 1
for ch in s:
    if ch == " ":
        count += 1
print("Words:", count)


#Find the first repeated character in a string.
s = input("Enter string: ")
for ch in s:
    if s.count(ch) > 1:
        print("First repeated:", ch)

#Remove duplicate characters from a string.
s = input("Enter string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)

#Find the sum of digits of a number.
num = input("Enter number: ")
total = 0
for d in num:
    total += int(d)
print("Sum:", total)

#Print Fibonacci series up to n terms.
n = int(input("Enter terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Print a pattern using * and a for loop.
for i in range(1, 6):
    print("*" * i)

# Separate positive and negative numbers from a list.
lst = [10, -5, 7, -2, 3]
pos = []
neg = []

for i in lst:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print("Positive:", pos)
print("Negative:", neg)



# # 1. Write a program to print all odd numbers from 1 to 50, but skip numbers divisible by 5 using `continue`.
i = 1
while i <= 50:
    if i % 5 == 0:
        i += 1
        continue
    if i % 2 != 0:
        print(i,end=" ")
    i += 1
     
    

# # 2. Write a `for` loop that prints numbers from 1 to 100, but stops completely when a number divisible by both 7 and 9 is found.
for i in range(1,101):
    if i % 7 == 0 and i % 9 == 0:
        print(i)
        break



# # 3. Using a `while` loop, print numbers from 10 to 1, but skip number 6.
num = 10
while num >= 1:
    if num == 6:
        num -= 1
        continue
    print(num,end=" ")
    num -= 1


# # 4. Write a program to iterate through a list of names and stop printing once the name `"admin"` is found.
names = ["sakshi","akshata","vaishnavi","admin","samaruddhi","sneha"]
for name in names:
    if name == "admin":
        break
    print(name,end=" ")

         
# # 5. Write a program to print the first 5 even numbers using a `while` loop.
i = 1
num = 0
while num < 5:
    if i % 2 ==0:
        print(i)
        num += 1
    i += 1
   



# # 6. Write a loop that prints characters of a string, but does not print vowels.
s = input("Enter any string:")
vowels = "aeiouAEIOU"
for char in s:
    if char in vowels:
        continue
    print(char,end=" ")



# # 7. Write a program using `for` loop and `else` to check whether a number exists in a list.
numbers = [1,2,3,4,5,6,7,8,9,0]
x = int(input("Enter number (eg,0-9):-"))
for num in numbers:
    if num == x:
        print(f"{x} found in list")
        break
else:
        print(f"{x} not found in list")
        



# # 8. Write a program that prints numbers from 1 to 20, but prints `"Skipped"` instead of the number 13.
for i in range(1,21):
    if i == 13:
        print("Skipped")
        continue
    print(i)


# 9. Write a loop that prints numbers from 1 to 10, but uses `pass` for even numbers.
for i in range(1,11):
    if i % 2 == 0:
        pass
    else:
        print(i)


# # 10. Write a program that counts how many numbers between 1 and 100 are divisible by 3.
count = 0
for i in range(1,101):
    if i % 3 == 0:
        count += 1
print(f"Count of numbers divisible by 3:{count}")


# # 11. Write a program to find the first number between 1 and 1000 that is divisible by 11 and 13, then stop the loop.
for i in range(1,1001):
    if i % 11 == 0 and i % 13 == 0:
        print(f"First number divisible by 11 and 13:- {i}")
        break


# # 12. Write a program that prints all numbers from 1 to 100, but:
# # Skip multiples of 3
# # Stop if a number divisible by 17 appears
for i in range(1,100):
    if i % 3 == 0:
        continue
    if i % 17 == 0:
        break
    print(i,end=" ")
    

# # 13. Using a `while` loop, keep taking numbers from the user until they enter 0, then print how many numbers were entered.
count = 0
while True:
    n = int(input("enter number(0 to stop):"))
    if n == 0:
        break
    count += 1
print(f"Total number Entered:- {count}")




# # 14. Write a program to check whether a given number is prime, using a loop and `break`.

n = int(input("Enter number:-"))
is_prime = True
for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print("Prime") 
else:
    print("Not prime")


# 15. Write a program that prints a triangle pattern using nested `for` loops.
for i in range(1,6):
    for j in range(i):
        print("*",end= " ")
    print()   


# 16. Write a program to iterate through a list of integers and print **only the first negative number, then stop.
lst = [ 1,4,8,-3,9,-1]
for i in lst:
    if i < 0:
        print(i)
        break


# 17. Write a program using `for-else` to check if a number is present in a range from 1 to 50.

num = int(input("Enter number to check:"))
for i in range(1,50):
    if i == num:
        print(f"{num} is present in range 1-50")
        break
else:
        print(f"{num} is not present in range 1-50")
    

# 18. Write a program that skips all numbers divisible by 4, but prints all others from 1 to 40.
for i in range(1,40):
    if i % 4 == 0:
        continue
    print(i,end=" ")


# 19. Write a program that finds the “sum of numbers until the sum becomes greater than 100”, then stops.
total = 0
i = 1
while total <= 100:
    total += i
    i += 1
print(total)


# 20. Write a program that prints numbers from 1 to 100, but replaces:

#  multiples of 3 → "Fizz"
#  multiples of 5 → "Buzz"
#  multiples of both → "FizzBuzz"

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz",end=" ")
    elif i % 3 == 0:
        print("Fizz",end=" ")
    elif i % 5 == 0:
        print("Buzz",end=" ")
    else:
        print(i,end=" ")

# 21. Login Attempts System
#     A user gets 3 attempts to enter the correct password.
#     Stop the loop if the password is correct, otherwise block access.

password = "admin123"
attempts = 3
while attempts > 0:
    entered_pass = input("Enter password:")
    if entered_pass == password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect password ,Attempt left :{attempts}")
        

# 22. ATM Withdrawal
#     Keep asking for withdrawal amount until the amount is less than or equal to balance.

balance = 10000
while True:
    withdrawal = float(input("Enter withdrawal amount:"))
    if withdrawal <= balance:
        balance -= withdrawal
        print(f"Withdrawal successful.Remaining balance : {balance}")
    else:
        print("Inefficient balance.")
    break



# 23. Student Attendance
#     Iterate through a student list and stop checking attendance when "absent" is found.
students = [ "present","present","present","absent","ptrsent","absent"]
for s in students:
    if s == "absent":
        break
    print(s)
        



# 24. Online Exam System
#     Skip a question if the student chooses "skip" and continue to the next question.

que = ["Q1","skip","Q3","skip"]
for q in que:
    if q == "skip":
        continue
    print(q)


# 25. Inventory Check
#     Loop through product quantities and stop when **stock reaches zero**.

stock=[10,5,3,9,0,2,8,]
for s in stock:
    if s == 0:
        break
    print(s)



# 26. OTP Verification
#     Users have 5 chances to enter OTP. Stop immediately when OTP matches.

otp = "9999"
tries = 5
while tries > 0:
    x = input("Enter OTP:")
    if x == otp:
        print("Verified")
        break
    tries -= 1
        
else:
    print("OTP blocked")
        
    



# 27. Website Visitor Counter
#     Count visitors until count reaches 100, then stop the loop.

count = 0
while count < 100:
    count += 1
print("visitors rechead 100")


# 28. Salary Processing
#     Skip employees whose salary is 0, process others.

salaries = [ 30000,60000,0,90000,100000,0,785000]
for s in salaries:
    if s == 0:
        continue
    print(s)


# 29. Menu-Driven Program
#     Show menu repeatedly until user selects `"Exit"`.

while True:
    choice = int(input("Enter your choice (1-3): "))
    match choice:
        case 1:
            print("Add")

        case 2:
            print("View")

        case 3:
            print("Exits")
            break

        case _:
            print("Invalid choice! Please enter 1 to 3.")
          

# 30. Game Lives System
#     The player has 3 lives. Each wrong move reduces one life. End game when lives become 0.

lives = 3
while lives > 0:
    move = input("Enter move(right/wrong):")
    if move == "wrong":
        lives -= 1
        print("lives left:",lives)
print("Game over")






