# list comprehension --> Creating new list from previous list
import math
import random

n = [6, 8, 3]
no = [i+1 for i in n]    # New item for item in list
no1 = [i*2 for i in range(1, 5)]
# for i in n:
#     add = i+1
#     no.append(add)
#
print(no)
print(no1)

no3 = [i**2 for i in n]
no4 = [i for i in n if i % 2 == 0]
print(no3)
print(no4)

# Dictionary Comprehension

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ['A', 'B', 'C']
students_scores = {i: random.randint(1, 100) for i in names}

print(students_scores)

passed_stud = {(students, score)for (students, score) in students_scores.items() if score >= 60}

print(passed_stud)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}


print(result)
