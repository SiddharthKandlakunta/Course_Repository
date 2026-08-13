#list is mutable
ex_list = [10,30,4.6,'hello']
for item in ex_list:
    print(f'{item} is of {type(item)} type')

#operations on list
#concatination
list1 = [1,3,5,7,9]#odd
list2 = [2,4,6,8,10]#even
print(list1+list2)

#repetition
print(list1*5)

#membership
print( 3 in list1 )
print( 2 in list1 )

#slicing [start:stop:step-size]  start to stop-1
list3 = ['hello','hola','welcomen','ohio']
#[0,1,2,3] [-4,-3,-2,-1]
print(list3[0:4]) #hola, welcomen
print(list3[1:])#prints from second to end of list
print(list3[:3])#prints first three
print(list3[:])#whole list
print(list3[-1])#last item
print(list3[-2:])#last two items
print(list3[:-2])#first two items
print(list3[::-1])#prints whole list reversed
print(list3[-2: :1])#first two items reversed
print(list3[:-3:-1])#last two items reversed
print(list3[-3::-1])#everything except last two items, reversed


#functions in list

list4 = [10,10,20,40,60]
print(len(list4))

string5 = 'hello world'
list5 = list(string5)
print(list5)
list4.append(70)
print(list4)
list4.append([80,90])
print(list4)
list4.extend(list5)
print(list4)
list4.insert(2,25)
print(list4)
print(list4.count(10))
print(list4.index(10))
print(list4.index('h'))
#print(list.index(100))
list4.remove(10)
print(list4)
#list4.remove(100)

print(list4.pop(8))#passing index as argument
print(list4.pop())
print(list4)

list4.reverse()
print(list4)
#sort and sorted

l1 = [34,50,12,14,60]
print(l1)
l1.sort(reverse=True)
print(l1)

l1 = [34,50,12,14,60]
l2 = sorted(l1,reverse = True)#does not change original list
print(l1)
print(l2)

print(min(l1))
print(max(l1))
print(sum(l1))




