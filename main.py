file=open("web.txt","r")
print(file.read())
file.close()

file=open("web.txt","w")
file.write("Welcome to ur python portal")
file.close()

file=open("web.txt","a")
file.write("\n Heres a new python portal")
file.close()
