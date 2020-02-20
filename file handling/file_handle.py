
with open('file.txt','r') as fileptr:
#fileptr=open('file.txt','r')


 opened=fileptr.read()
 print (opened)
 #print (fileptr.readline(1))
'''for i in opened:
    print (i)'''

## here 'file' stores a temporary memory if 'file.txt' can be opened
'''if fileptr==True:    #means it is openable
    print("file is opened successfully")'''
print(dir(fileptr))
