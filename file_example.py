fileptr = open("c:\\data\\a.txt", "r")

if fileptr:
    print("file is opened successfully")

# closes the opened file
fileptr.close()


with open("c:\\data\\a.txt",'r') as f:
    content = f.read();
    print(content)