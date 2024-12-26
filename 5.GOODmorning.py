import time
timestamp=(time.strftime("%H:%M:%S"))
timestamp1=int((time.strftime("%H:%M:%S")))
time1=int(input("ENTER THE TIME YOU ENTERED IN THE OFFICE:"))
if(time1>timestamp1):
    print("SIR YOU ARE LATE")
elif(time1<timestamp1):
    print("GOOD MORNING SIR")
else:
    print("YOU ARE FIRED")



