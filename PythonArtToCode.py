#Erase Output Folder
file = open("code.txt","w")
file.truncate(0)
file.close()


#Replace the syntax that can mess the code and write to the new file
with open('code.txt',"a") as the_file:
    the_file.write("print(\"")
for line in open("art.txt","r").readlines(): #Get the login
    line=line.replace("\n","")
    line=line.replace("\"","\\\"")
    line=line.replace("\'","\\\'")
    line=line.replace("\\","\\")
    with open('code.txt', 'a') as the_file:
        the_file.write(line+" \\n")
with open('code.txt',"a") as the_file:
    the_file.write("\")")

