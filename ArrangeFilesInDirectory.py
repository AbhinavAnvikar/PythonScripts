import os

path = input("Enter the path : ");
#path ='C:\Users\aban0617\Downloads'
os.chdir(path)
#print(os.getcwd());

for list in os.listdir(path):

    if(os.path.isfile(list)):
        file_extn = os.path.splitext(list)[1]
        NewPath = path +"\\"+file_extn
        destination = path +"\\"+file_extn+"\\"+os.path.splitext(list)[0]+file_extn
        src = path +"\\"+os.path.splitext(list)[0]+file_extn
        #print("Newpath - "+NewPath)
        #print("src - " + src)
        #print("destination - "+destination)
        try:
            os.mkdir(file_extn,777)
        except FileExistsError:
            pass
            #print("Directory Exists - "+file_extn)
        try:
            os.rename(src,destination)
        except FileExistsError:
            pass
            #print("File Already Exists at path - "+destination)