file=open("web.txt","r")
print(file.read())
file.close()

file=open("web.txt","w")
file.write("Welcome to ur python portal")
file.close()

file=open("web.txt","a")
file.write("\n Heres a new python portal")
file.close()



f1=open("ref.txt","a+")
f2=open("kg.txt","r")
f1.write(f2.read())
f1.seek(0)
f2.seek(0)
print(f1.read())
print(f2.read())