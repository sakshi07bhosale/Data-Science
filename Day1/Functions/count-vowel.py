def count_vowel(text):
    count = 0
    for ch in text:
        if ch in "AEIOUaeiou":
            count += 1
    return count
print(count_vowel("sakshi"))