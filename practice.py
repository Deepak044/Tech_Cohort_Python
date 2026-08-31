# print("Hello World")

# alphabets = "ABCDE"
# for i in alphabets:
#     print(i)

# String Methods

# a = "dEEpak"
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.replace("dEEpak", "John"))

str1 = "Welcome to the console"
# str1 = "Deepak"
print(len(str1))
print((str1.center(50)))
print(len(str1.center(50)))

print(str1.count("e"))
print(str1.endswith("!"))
print(str1.find("to", 4, 10))    # find will check the given value and return the index, if value is absent it will return -1.

print(str1.isalnum())            # Alpha numeric: Return True if string consist of A-Z, a-z,0-9, and if other punctuations are present it returns false.
print(str1.isalpha())            # isalpha() : Return True if string consist of A-Z, a-z, and if other punctuations or numbers are present it returns false.

print(str1.islower())            # islower() - Returns True if all characters are in lowercase, else False.
print(str1.istitle())            # istitle() - Returns Ture if first letter of each word of the string is capitalized else return False.





