# #it is a data structure which is similar to hash table
# #it is an unordered collection of items until 3.6, from 3.7 onwards it is ordered
# #dictionary has key value pairs and is mutable in nature
# #keys should be unique and must be an immutable object like a number, string, and tuples

# dict1 = {}
# print(type(dict1))
# dict2 = {1:'Hyderabad', 2:'Delhi', 3:['Mumbai', 'North'], 1 : 'secunderabad'}
# print(dict2)
# #to access values in dictionary we use keys and for that we use keys
# print(dict2[3])
# #these are mutable
# dict2[3] = 'Mumbai'
# print(dict2[3])
# print(dict2.get(3))
# #to delete we use del and pop
# # del dict2[3]#this is a operation and will return none
# # print(dict2)
# deleted_variable = dict2.pop(3)
# print(deleted_variable)
# #print(dict2.pop(3))#pop will return the deleted item
# print(dict2)
# print(dict2.popitem())#this will remove the last item added to dictionary
# print(dict2)

# dict2.clear()#It will clear the dictionary
# print(dict2)

# dict3 = {'First Name':'John', 'Last Name': 'Doe', 'Age': 35, 'Address': 'California'}
# print(len(dict3))
# print(dict3.keys())
# print(dict3.values())
# print(dict3.items())

# for i in dict3:
#     print(i)

# dict2 = dict3.copy()
# print(dict2)


# student_marks = {
#     'John': 95,
#     'Jane': 85,
#     'Rick': 78,
#     'Ron': 56,
#     'Mary': 34,
#     'Richard': 98
# }

# student_grades={}
# for student in student_marks:
#     marks = student_marks[student]
#     if marks > 90 :
#         student_grades[student] = 'O'
#     elif marks > 80:
#         student_grades[student] = 'A'
#     elif marks > 70:
#         student_grades[student] = 'B'
#     elif marks > 60:
#         student_grades[student] = 'C'
#     elif marks > 50:
#         student_grades[student] = 'D'
#     else:
#         student_grades[student] = 'F'
# print(student_grades)

#nested dictionaries

student_data = {
    1: {'Name':'John', 'Age':19, 'Course':'Python', 'Time': ['morining','evening']},
    2: {'Name':'Jane', 'Age':20, 'Course':'Python with DSA'},
    'Student Roll': [1,2]
}
print(student_data[1]['Time'][1])
print(student_data[1])
print(student_data['Student Roll'][0])
print(student_data[1]['Name'])
student_data[1]['Blood Group'] = 'B+'
print(student_data[1])
#del student_data[1]['Blood Group']

print(f'deleted {student_data[1].pop('Blood Group')} from student data')
print(student_data[1])
