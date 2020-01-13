from tkinter import *
import sqlite3

root=Tk()
root.title("Codewarriors")
root.iconbitmap("C:/Users/Snehal/Pictures/icon1.jpg")


conn=sqlite3.connect("dhp.db")
print("Database created successfully")

c=conn.cursor()

c=c.execute("""CREATE TABLE Housing_Price(Email_Address text,Your_Name text,In_which_locality_do_you_live text,Type_of_house text,Distance_from_Nearest_Hospital text,Number_of_Rooms text,Distance_from_Nearest_School text,Distance_from_Nearest_Police_Station text,Distance_from_Nearest_Fire_Station text,Availability_of_Transport_in_your_area text,Current_Price_of_the_House text);""")
print("Table created successfully")


def Submit():
    conn=sqlite3.connect("dhp.db")
    c=conn.cursor()
    a1=e1.get()
    a2=e2.get()
    a3=clicked2.get()
    a4=r6.get()
    a5=r1.get()
    a6=r.get()
    a7=r2.get()
    a8=r3.get()
    a9=r4.get()
    a10=r5.get()
    a11=r7.get()
    c.execute("INSERT INTO Housing_Price(Email_Address,Your_Name,In_which_locality_do_you_live,Type_of_house,Distance_from_Nearest_Hospital,Number_of_Rooms,Distance_from_Nearest_School,Distance_from_Nearest_Police_Station,Distance_from_Nearest_Fire_Station,Availability_of_Transport_in_your_area,Current_Price_of_the_House) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11))
    print(e1.get(),e2.get(),clicked2.get(),r6.get(),r1.get(),r.get(),r2.get(),r3.get(),r4.get(),r5.get(),r7.get())

    print("Data Inserted successfully")
    e1.delete(0,END)
    e2.delete(0,END)
    '''clicked2.delete(0,END)
    r6.delete(0,END)
    r1.delete(0,END)
    r.delete(0,END)
    r2.delete(0,END)
    r3.delete(0,END)
    r4.delete(0,END)
    r5.delete(0,END)
    r7.delete(0,END)'''
    conn.commit()
    conn.close()
    
frame=LabelFrame(root,text="Housing Price",fg="Blue",padx=5,pady=5)
frame.pack(side=LEFT,fill="both",expand=True)

'''label_1=Label(frame,text="This form is a general survey to get the\n data of housing prices in Surat city.\nYou are requested to enter the correct\n details.\n Some selected candidate will be awarded \nsome premium membership of Ganna+ \nand many more. \nWinners will be contacted through their \nEmail Id.",width=50,justify=LEFT)
label_1.pack(anchor=W,padx=10,pady=10)'''

label_2=Label(frame,text="Email Address*",width=50,justify=LEFT)
label_2.pack(anchor=W,padx=10,pady=10)

e1=Entry(frame,width=50)
e1.pack(anchor=W,padx=10,pady=10)

label_3=Label(frame,text="Your Name*",width=50,justify=LEFT)
label_3.pack(anchor=W,padx=10,pady=10)

e2=Entry(frame,width=50)
e2.pack(anchor=W,padx=10,pady=10)

label_4=Label(frame,text="In which locality do you live?*",width=50,justify=LEFT)
label_4.pack(anchor=W,padx=10,pady=10)

options=["Adajan","Athwagate","Bhatar","Chowk Bazar","City Light","Delhi Gate","Dindoli","Ghod Dod Road","Katargam","Majura Gate","Modern Town","Navagam","Pandesara","Parle Point","Piplod","Parvat Patiya","Rander","Sachin","Station Road","Udhna","Varachha","Ved Road","Other"]
clicked2=StringVar(frame)
clicked2.set("Choose")
drop=OptionMenu(frame,clicked2,*options)
drop.pack(anchor=W,padx=10,pady=10)

label_11=Label(frame,text="Type of house*",width=50,justify=LEFT)
label_11.pack(anchor=W,padx=10,pady=10)

Modes6=[("Flat or Residents","Flat or Residents"),("Row House","Row House"),("Bungalow","Bungalow")]

r6=StringVar()
r6.set(0)

for text6,mode6 in Modes6:
        Radiobutton(frame,text=text6,variable=r6,value=mode6).pack(anchor=W)

label_6=Label(frame,text="Distance from Nearest Hospital(in km)*",width=50,justify=LEFT)
label_6.pack(anchor=W,padx=10,pady=10)

Modes1=[("<1 km","<1 km"),("1-3 km","1-3 km"),("3-5 km","3-5 km"),(">5 km",">5 km")]

r1=StringVar()
r1.set(0)

for text1,mode1 in Modes1:
        Radiobutton(frame,text=text1,variable=r1,value=mode1).pack(anchor=W)


label_5=Label(frame,text="Number of Rooms*",width=50,justify=LEFT)
label_5.pack(anchor=W,padx=10,pady=10)

Modes=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("Other:","Other")]

r=StringVar()
r.set(0)

for text,mode in Modes:
        Radiobutton(frame,text=text,variable=r,value=mode,command=lambda:clicked(r.get())).pack(anchor=W,)

def clicked(v):
        if(v=="Other"):
                e3=Entry(frame,width=50)
                e3.pack(anchor=W,padx=10,pady=10)
        
frame_1=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
frame_1.pack(side=LEFT,fill="both",expand=True,padx=10,pady=10)

label_7=Label(frame_1,text="Distance from Nearest School(in km)*",width=50,justify=LEFT)
label_7.pack(anchor=W,padx=10,pady=10)

Modes2=[("<1 km","<1 km"),("1-3 km","1-3 km"),("3-5 km","3-5 km"),(">5 km",">5 km")]

r2=StringVar()
r2.set(0)

for text2,mode2 in Modes2:
        Radiobutton(frame_1,text=text2,variable=r2,value=mode2).pack(anchor=W)

label_8=Label(frame_1,text="Distance from Nearest Police Station(in km)*",width=50,justify=LEFT)
label_8.pack(anchor=W,padx=10,pady=10)

Modes3=[("<1 km","<1 km"),("1-3 km","1-3 km"),("3-5 km","3-5 km"),(">5 km",">5 km")]

r3=StringVar()
r3.set(0)

for text3,mode3 in Modes3:
        Radiobutton(frame_1,text=text3,variable=r3,value=mode3).pack(anchor=W)

label_9=Label(frame_1,text="Distance from Nearest Fire Station(in km)*",width=50,justify=LEFT)
label_9.pack(anchor=W,padx=10,pady=10)

Modes4=[("<1 km","<1 km"),("1-3 km","1-3 km"),("3-5 km","3-5 km"),(">5 km",">5 km")]

r4=StringVar()
r4.set(0)

for text4,mode4 in Modes4:
        Radiobutton(frame_1,text=text4,variable=r4,value=mode4).pack(anchor=W)
        
label_10=Label(frame_1,text="Availability of Transport in your area*",width=50,justify=LEFT)
label_10.pack(anchor=W,padx=10,pady=10)

Modes5=[("Easily Available","Easily Available"),("Time Consuming","Time Consuming"),("Depends","Depends")]

r5=StringVar()
r5.set(0)

for text5,mode5 in Modes5:
        Radiobutton(frame_1,text=text5,variable=r5,value=mode5).pack(anchor=W)
                
label_12=Label(frame_1,text="Current Price of the House*",width=50,justify=LEFT)
label_12.pack(anchor=W,padx=10,pady=10)

Modes7=[("<7 lacs","<7 lacs"),("7-15 lacs","7-15 lacs"),("15-30 lacs","15-30 lacs"),("30-50 lacs","30-50 lacs"),(">50 lacs",">50 lacs")]

r7=StringVar()
r7.set(0)

for text7,mode7 in Modes7:
        Radiobutton(frame_1,text=text7,variable=r7,value=mode7).pack(anchor=W)
s=r7.get()
myButton=Button(frame_1,text="Submit",command=Submit)
myButton.pack()

conn.commit()

conn.close()

root.mainloop()
