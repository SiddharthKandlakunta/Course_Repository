#there are two type of files text and binary
#text examples are: .txt, .csv, .py etc. binary: audio, video i.e., not human readable
#main operations on file: open, read, write, close
#opening a file in a program

#file_object = open('text1.txt','x') #open('file name','mode')

# f1 = open('text1.txt','r')
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.close()

# with open('text2.txt','a+') as f1:
#     print(f1.tell())
#     f1.write('append mode')
#     f1.seek(0)
#     print(f1.read())

# f1 = open('img.jpg','rb+')
# f2 = open('img_copy.jpg','wb+')
# for i in f1:
#     f2.write(i)

# print(f1.read())

f1 = open('C:\\Users\\Srinivasulu K\\Desktop\\hello.txt','r')
print(f1.read())
    



# #here file_object is an object which points towards the file since open func returns an obj
# f1 = open('text1.txt','r')#here the file obj, f1 points to begining of text1.txt
# # with open('text.txt','r') as f1:
# #     data = f1.read()
# #     print(data)
# print(f1.tell())
# data = f1.read()
# print(f1.tell())
# print(data)
# f1.seek(0)
# print(f1.tell())
# f1.close()
# #the default mode for read function is 'r'

# #for write mode, the already exsisting file will become empty
# #if opening a new file which doesnt exist 'w' mode will make a new file

# f2 = open('text2.txt','w')#f2 will point to the begining of the file
# f2.write('this is a new file')
# f2.close()
# #print(f2.read())

# #r+ is for reading first and then writing and follows all the rules of 'r' mode
# #it also enables writing to the 'r' mode
# with open('text2.txt', 'r+') as f3:
#     data = f3.read()
#     print(data)
#     print(f3.tell())
#     f3.write('in r+ mode')
#     #data = f3.read()
#     f3.seek(0)
#     # print(data)
#     print(f3.tell())




# #w+ is for writing first and read next, it follows all the rules of 'w' mode
# #it also enables reading to the 'w' mode


# #'a' is append mode, follows rules of write mode but object points to the end of the file



