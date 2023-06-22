from tkinter import *
root=Tk()
root.geometry("500x300")
def getvals():
    print("accepted")
#Heading
Label(root,text="python registration Form",font="ar 15 bold").grid(row=0,column=3)

#creating field names
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
payment_Mode=Label(root,text="Payment Mode")

#packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment_Mode.grid(row=5,column=2)

#creating variables to store values
namevalue= StringVar
phonevalue= StringVar
gendervalue= StringVar
emergencyvalue= StringVar
payment_Modevalue= StringVar
checkvalue=IntVar

#creating entry fields
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
payment_Modeentry=Entry(root,textvariable=payment_Modevalue)

#packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
payment_Modeentry.grid(row=5,column=3)

#creating Checkbox
checkbtn= Checkbutton(text="remember me ?", variable= checkvalue )
checkbtn.grid(row=6,column=3)

#submit button
Button(text="Submit", command=getvals()).grid(row=7,column=3)


root.mainloop()


