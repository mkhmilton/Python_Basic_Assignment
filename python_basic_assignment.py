#Task 1: Variable Manipulation
print("\nTask 1 Solution:-")
name = "Khalid Hasan Milton"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old")





#Task 2: Data Types and Type Conversion
print("\nTask 2 Solution:-")
num1 =10
num2 = 10.5
num1_float = float(num1)
num2_int = int(num2)
print("num1:" + str(num1))
print("num1_float:" + str(num1_float))
print("num2:" + str(num2))
print("num2_int:" + str(num2_int))





#Task 3: String Manipulation
print("\nTask 3 Solution:-")
sentence = "Python programming is fun"
print("Length of " + sentence + " is : " + str(len(sentence)))
print("8Th character of " + str(sentence[8]))
substring = sentence[0:7]
print(substring + "I enjoy it!")






#Task 4: Lists and List Manipulation
print("\nTask 4 Solution:-")
fruits = ["Apple", "Banana", "Cherry", "date"]
fruits.append("grape")
fruits.remove("Banana")
print("Length of the list:", len(fruits))
sliced_fruits = fruits [2:4]
extra_fruits = ["kiwi", "lemon"]
combined_fruits = sliced_fruits + extra_fruits
print("Combined list:", combined_fruits)





#Task 5: Conditional Statements
print("\nTask 5 Solution:-")
num = 18
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")





#Task 6: Loops
print("\nTask 6 Solution:-")
print("Numbers from 1 to 10:")
for num in range(1, 11):
    print(num)
sum = 0
for num in range(1, 101):
    sum = sum + num
print("Sum of numbers from 1 to 100:", sum)






#Task 7: Functions
print("\nTask 7 Solution:-")
def calculate_square(num):
    return num ** 2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
num_1 = 7
num_2 = 29

square_of_7 = calculate_square(num_1)
is_29_prime = is_prime(num_2)

print("Square of", num_1, "is:", square_of_7)
if is_29_prime:
    print(num_2, "is a prime number.")
else:
    print(num_2, "is not a prime number.")







#Task 8: Dictionaries
print("\nTask 8 Solution:-")
student = {
    "name": "Khalid Hasan Milton",
    "age": 25,
    "grade": "A+",
}
student["course"] = "Computer Science & Engineering(Evening Masters)"
print("Keys in the dictionary:")
for key in student.keys():
    print(key)
print("\nKey-value pairs:")
for key, value in student.items():
    print(key, ":", value)
