# 1. Write a python script to check whether a given number is positive or non-positive
num = int(input("Enter number \t"))
if num > 0:
    print("Number is positive ")
else:
    print("Number is non- positive ")
print()

# 2. Write a python script to check whether a given number is divisible by 5 or not
num = int(input("Enter number "))
if num % 5 == 0:
    print(num, " Number is divisiblle of 5")
else:
    print(num, " Number is not divisible of 5")
print()

# 3. Write a python script to check whether a given number is even or odd
num = int(input("Enter number "))
if num % 2 == 0:
    print(num, " Number is even ")
else:
    print(num, " Number is odd ")
print()

# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2"))
if num1 == num2:
    print(num1, "and ", num2, " are equal")
elif num1 > num2:
    print(num1, " is greater")
else:
    print(num2, " is greater")
print()
# 5. Write a python script to print two given words in dictionary order
word1=input("Enter word1 ")
word2=input("Enter word2 ")
if ord(word1[0])<ord(word2[0]):
    print(word1,word2,sep="\n")
else:
    print(word2,word1,sep="\n")    
print()    
# 6. Write a python script to check whether a given number is a three digit number or not.
num1 = int(input("Enter number "))
if 100 <= num1 <= 999:
    print("Number is three digits ")
else:
    print("Number is not three digits ")
print()

# 7. Write a python script to check whether a given number is positive, negative or zero.
num = int(input("Enter number "))
if num > 0:
    print("Positive number ")
elif (num < 0):
    print("Number is negative ")
else:
    print(" Number is zero ")
print()

# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
print(" quadratic equation ax2 + bx + c ")
b = int(input("Enter the coefficient of x of equation "))
a = int(input("Enter the coefficient of x2 of equation "))
c = int(input("Enter the constant coefficient of equation "))
D = (b*b-4*a*c)
if D > 0:
    print(" the quadratic equation has two real and different roots ")
elif (D < 0):
    print(" the quadratic equation has two complex roots ")
else:
    print("roots will be equal and real ")
print()

# 9. Write a python script to check whether a given year is a leap year or not.
year = int(input(" Enter year "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, " year is leap year ")
        else:
            print(year, " year is not leap year ")
    else:
        print(year, " year is a leap year ")
else:
    print(year, " The year is not a leap year (it has 365 days).")
print()

# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
num1 = int(input(" Enter number 1 "))
num2 = int(input(" Enter number 2"))
num3 = int(input(" Enter number 3"))
if num1 > num2 and num2 > num3:
    print(num1, " is greater ")
elif (num1 < num2 and num2 > num3):
    print(num2, " is greater ")
else:
    print(num3, " is greater ")
print()

# 11. Write a python script to take the month value in numeric format and display the number of days in it.
month = int(input("Enter month number "))
if month == 4 or month == 6 or month == 9 or month == 11:
    print(month, " month is having 30 days ")
elif (month == 2):
    print(month, " month is having 28 or 29 days ")
else:
    print(month, " month is having 31 days ")
print()

# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
real = int(input(" Enter real part of complex number "))
img = int(input(" Enter imginary part of complex number  "))
com=complex(real,img)
print(com)
if real > img:
    print(real, " is greater ")
else:
    print(img, " is greater")
