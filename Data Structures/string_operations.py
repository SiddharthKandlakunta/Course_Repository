#string is a sequence of characters
#strings are immutable and ordered(indexed)

x = 'hello world'
print(x)
# x[1] = 'o' 
# print(x)
y = '!'
print(x+y)
age = 21
print(f'{x+y} my age is {age}')

#string operations 
#slicing
a = 'python example'
#0,1,2,3,4,5,6,7,8,9,10,11,12,13
#-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
print(a[5:10])
print(a[:10])
print(a[5:])
print(a[:])
print(a[-8:-3])
print(a[5::2])
print(a[::-1])
# for letter in a:
#     parint(hello letter)



#string built in functions
print(len(a)) #used to find the length of the string
print(a.title()) #used to make the first lettr of every word in a string capital
print(a.lower()) #returns all lower case
print(a.upper()) #returns all upper case
b = 'hello hello mic testing, hello'
print(len(b))
print(b.count('hello'))#checks the number of times the substring is repeated
print(b.count('hello',5))#str.count(substr,start,stop)
print(b.count('hello',5,11))
print(b.find('hello'))#used to find index of the substring start position
print(b.find('hello',5))
print(b.find('hee'))#returns -1
#print(b.index('hee'))#returns a value error, works in the same way as find
print(b.endswith('hello'))
print(b.endswith('o'))
print(b.endswith('e'))
print(b.startswith('h'))
print(a.isalnum())#returns true if and only if all the chars are either numbers or characters
print(b.isalnum())
c = 'world\rbye'
print(c)
print(c.isspace())#returns true if string is non empty and has only white spaces
d = ' \n \t \r'
print(d.isspace())
print(a.isspace())
print(a.islower())
e = 'hello world 12324!!!'
print(a.islower())
print(a.isupper())
print(a.istitle())
f = 'Hello World'
print(f.lstrip())
print(f.rstrip())
print(f.strip())
print(f.replace('o','*'))
print(f.replace('World', 'class'))
print('_'.join(f))#here _ is a separator
g = 'This is a python class'
print(g.partition('a')) #always returns 3 string outputs
print(g.partition('are'))
print(g.split())#retuens a list, by default splits with space as a separator
print(g.split('i'))
