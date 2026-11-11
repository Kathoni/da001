def birthday_match(students):
 
#  Find a pair of students with the same birthday
#  Input: tuple of student (name, bday) tuples
#  Output: tuple of student names or None

 n = len(students) # O(1)
 record = StaticArray(n) # O(n)
 for k in range(n): # n
  (name1, bday1) = students[k] # O(1)
 # Return pair if bday1 in record
 for i in range(k): # k
  (name2, bday2) = record.get_at(i) # O(1)
 if bday1 == bday2: # O(1)
  return (name1, name2) # O(1)
 record.set_at(k, (name1, bday1)) # O(1)
 return None

 #DSA
 #List is a data structure it aids in storing and organising data
students = ["Alice", "John", "Mary", "David"]
print(students)

#Dictionary is also a data structuer
student = {
    "name": "Alice",
    "age": 21,
    "course": "IT"
}

print(student["name"])

#algorithm
numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)

# #how it works
# #The algorithm:
# 1. Starts by assuming 10 is the largest.
# 2. Checks 25 against 10.
# 3. Checks 7 against 25.
# 4. Checks 40 against 25.
# 5. Checks 15 against 40.
# 6. Returns 40.
# That's an algorithm!