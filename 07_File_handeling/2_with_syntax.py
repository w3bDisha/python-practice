with open("demo.txt","r") as f:  #read mode
    data = f.read()
    print(data)

    #when we are using with syntax to file automatically close hojati h 
    #hume f.close() ki jrurt ni

with open("demo.txt","w") as f: #write mode
    f.write("New data saved")