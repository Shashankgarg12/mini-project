from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import filecmp
global P1,P2
def F1_location():
    global P1
    P1=filedialog.askopenfilename()

def F2_location():
    global P2
    P2=filedialog.askopenfilename()

def Compare_F1_F2():
    if filecmp.cmp(P1,P2): messagebox.showinfo("Result","Both files are same")
    else : messagebox.showinfo("Result","Files are Different")

def Merge_F1_F2():
    print('h')
    global P1,P2
    data = data2 = ""
    with open(P1) as fp:
        data = fp.read()
    with open(P2) as fp:
        data2 = fp.read()
    data += "\n"
    data += data2
    with open ('file3.txt', 'w') as fp:
        fp.write(data)

Code_With_Shashank=Tk()

Code_With_Shashank.title("Compare & Merge")

up=Frame(Code_With_Shashank)
down=Frame(Code_With_Shashank)

up.pack(fill=BOTH,expand=1,pady=10)
down.pack(fill=BOTH,expand=1,pady=10)

F1=Button(up,text="File 1",command=F1_location)
F2=Button(up,text="File 2",command=F2_location)
Merge=Button(down,text="   Merge  ",command=Merge_F1_F2)
Compare=Button(down,text="Compare",command=Compare_F1_F2)

F1.pack(fill=BOTH,expand=1,side=LEFT,padx=10)
F2.pack(fill=BOTH,expand=1,side=RIGHT,padx=10)
Merge.pack(fill=BOTH,expand=1,side=LEFT,padx=10)
Compare.pack(fill=BOTH,expand=1,side=RIGHT,padx=10)

Code_With_Shashank.mainloop()