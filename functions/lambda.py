#lambda function is a anonymous function
# it can have any number of arguments but only a single expression

## lambda arguments : expression

x = lambda a: a + 5
print(x(5))

y = lambda a,b : a * b
print(y(5,6))

z = lambda a, b, c : a + b + c
print(z(1,2,3))

#lambda is best used inside an other function

def n_times(n):
    return lambda a : a*n

double = n_times(2)
print(f'the double of 586 is {double(586)}')

triple = n_times(3)
print(f'the triple of 586 is {triple(586)}')
#lambda is created when we need a function for short period of time

###lambda is mainly used with map(), filter() and sorted() functions.

#map(function, iterable)
marks = [45, 56, 98, 85, 76 , 92, 63]

def grade(marks):
    if marks >= 90:
        return 'O'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B'
    elif 60 <= marks < 70:
        return 'C'
    else:
        return 'F'

grades = list(map(grade, marks))


#grades = list(map(grade, marks))

numbers = [1,15,4,6,25]
doubled = list(map(lambda x : x * 2 , numbers))
print(doubled)

print(f'marks are {marks}')
print(f'grades are {grades}')   
#print(f'grades are {next(grades)}') 

#print(f'grades are {list(grades)}')

#filter filters variables from a datatype.

def fail_score(score):
    return score < 60

result = list(filter(fail_score, marks))
print(f'the failing scores are {result}')

result_lambda = list(filter(lambda a: a<60, marks))
print(f'the failing scores are {result_lambda}')

#sorted (iterable, key, reverse = False) key(used for sort comparision like key = len and reverse are optional

sorted_numbers = sorted(numbers,reverse = True)
print(sorted_numbers)

letters = ['a', 'z', 'd', 'c']
sorted_letters = sorted(letters, reverse = True)
print(sorted_letters)

words = ['hi', 'hello', 'hola', 'welcomen']
sorted_words = sorted(words, key = len,reverse= True)
print(sorted_words)
print(sorted(words,key = lambda x : len(x)))

students = [
    {"name": "John", "grade": 89},
    {"name": "Jane", "grade": 85},
    {"name": "Bob", "grade": 60}
]

students_1 = [('bob', 90), ('john', 85), ('jane', 93)]

# Sort by the "grade" key in each dictionary
sorted_students = sorted(students, key=lambda x: x["grade"])
sorted_students_1 = sorted(students_1, key = lambda x : x[1])
print(sorted_students)
print(sorted_students_1)
