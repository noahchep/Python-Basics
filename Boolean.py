#true false
import math

print(10>20)
print(10==10.0)
print(10>=10.11)


score = int(input("Enter the score:"))

if score >= 90:
    print ("A")
elif 80 <= score <= 89:
    print("A-")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("B-")
elif 50 <= score <= 49:
    print("C")
elif 40 <= score <= 49:
    print("C-")
elif 30 <= score <= 39:
    print("C-")
elif 20 <= score <= 29:
    print("D")
else:
    print("E")








