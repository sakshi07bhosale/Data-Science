#1. capitalize():Converts first character to uppercase, rest to lowercase.
text = "python PROGRAMMING"
print(text.capitalize())

#2. casefold():Converts string to lowercase (stronger than lower()).
text = "StraSSe"
print(text.casefold())

#3. center(width):Centers the string with spaces.
text = "Python"
print(text.center(10))

#4. count(substring):Counts occurrences of substring.
text = "banana"
print(text.count("a"))

#5. encode():Encodes string into bytes.
text = "Python"
print(text.encode())

#6. endswith(substring):Checks if string ends with substring.
print("hello.py".endswith(".py"))

#7. expandtabs(tabsize):Replaces \t with spaces.
text = "Hello\tWorld"
print(text.expandtabs(4))

#8. find(substring):Returns index of first occurrence or -1.
print("Python".find("o"))

#9. format():Formats values using {}.
print("My name is {}".format("Sakshi"))

#10. format_map(mapping):Uses dictionary for formatting.
data = {"name": "Sakshi"}
print("Hello {name}".format_map(data))

#11. index(substring):Same as find() but gives error if not found.
print("Python".index("y"))

#12. isalnum():Checks alphanumeric characters.
print("Python123".isalnum())

#13. isalpha():Checks only alphabets.
print("Python".isalpha())

#14. isascii():Checks ASCII characters.
print("Hello".isascii())

#15. isdecimal():Checks decimal digits only.
print("123".isdecimal())

#16. isdigit():Checks digits (including Unicode).
print("123".isdigit())

#17. isidentifier():Checks valid Python variable name.
print("my_var".isidentifier())

#18. islower():Checks lowercase letters.
print("python".islower())

#19. isnumeric():Checks numeric values.
print("½".isnumeric())

#20. isprintable():Checks printable characters.
print("Hello\n".isprintable())

#21. isspace():Checks whitespace only.
print("   ".isspace())

#22. istitle():Checks title case.
print("Hello World".istitle())

#23. isupper():Checks uppercase letters.
print("PYTHON".isupper())

#24. join(iterable):Joins list elements.
words = ["Python", "is", "easy"]
print(" ".join(words))

#25. ljust(width):Left-aligns string.
print("Python".ljust(10))

#26. lower():Converts to lowercase.
print("PYTHON".lower())

#27. lstrip():Removes left spaces.
print("  Python".lstrip())

#28. maketrans():Creates translation table.
table = str.maketrans("aeiou", "12345")
print("python".translate(table))

#29. partition(separator):Splits into 3 parts
print("python-programming".partition("-"))

#30. replace(old, new):Replaces substring.
print("I like Java".replace("Java", "Python"))

#31. rfind(substring):Finds from right.
print("banana".rfind("a"))

#32. rindex(substring):Same as rfind() but error if not found.

#33. rjust(width):Right-aligns string.
print("Python".rjust(10))


#34. rpartition(separator):Splits from right.
print("a-b-c".rpartition("-"))

#35. rsplit(separator):Splits from right.
print("a,b,c".rsplit(","))

#36. rstrip():Removes right spaces.
print("Python   ".rstrip())

#37. split(separator):Splits string into list.
print("Python is easy".split())

#38. splitlines():plits lines.
print("Hello\nWorld".splitlines())

#39. startswith(substring):Checks starting string.
print("Python".startswith("Py"))

#40. strip():Removes both side spaces.
print("  Python  ".strip())

#41. swapcase():Swaps case.
print("PyThOn".swapcase())

#42. title():Converts to title case.
print("python programming".title())

#43. translate(table):Uses translation table (see maketrans).

#44. upper():Converts to uppercase.
print("python".upper())

#45. zfill(width):Pads zeros on left.
print("45".zfill(5))


