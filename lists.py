fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[-1])

students = ["Alice", "John", "Mary", "David"]
students.append("Eve")
students.remove("John")
students[0] = "Alicia"
print(students)
print(len(students))

for i in fruits:
 print(i)
for j in students:
 print(j)

marks = [85, 90, 78, 92, 88]
total = 0

for i in marks:
 if i > 80:
  print(i)
 total = total + i
 
print(total)


# marks = [70, 80, 65, 90, 75]

# total = 0

# for mark in marks:
#     total = total + mark

# print(total)
# count = 1

# while count <= 5:
#     print(count)

# count = 1   

# while count <= 10:
#     print(count)
#     count = count + 1

count = 10

while count >= 1:
    print(count)
    count = count - 1

number = 1

total = 0

while number <= 5:
    total = total + number
    number = number + 1

print(total)

marks = [70, 85, 60, 90, 75]

total = 0
i = 0
while i < len(marks):
    total = total + marks[i]
    i = i + 1
print(total)
