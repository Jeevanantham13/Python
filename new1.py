f=open("file.txt","w+")
for i in range(1,100001):
    f.write("number= %d\r\n" % (i+0))
    
