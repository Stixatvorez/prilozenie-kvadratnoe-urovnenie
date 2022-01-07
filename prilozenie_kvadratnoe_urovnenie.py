from tkinter import *
from tkinter import messagebox
def okno(event):
    if a.get() == "" or b.get() == '' or c.get() == '':
        messagebox.showinfo('БУЙ БУЙ!',' МАХАЦА БУИШЬ?! ЗАПОЛНИ ВСЕ ПОЛЯ!')#всплывающее окно    
    else:
        av = float(a.get())
        bv = float(b.get())
        cv = float(c.get())
        D = (bv)**2 - 4 * av * cv
        if D < 0:
            solution.config(text="корней нет")
        elif D == 0:
            x = -1 * bv/(2 * av)
            solution.config(text="D="+str(D)+", "+'X='+str(round(x,2)))
        else:
            x1 = (-1 * bv - D ** 0.5)/(2 * av)
            x2 = (-1 * bv + D ** 0.5)/(2 * av)
            solution.config(text="D="+str(D)+", "+'X1='+str(round(x1,2))+", "+'X2='+str(round(x2,2)))
aken=Tk()
aken.title("Калькулятор квадратного уравнения from markusha salumets")
aken.geometry('400x600')

a = StringVar()
a.set('')
b = StringVar()
b.set('')
c = StringVar()
c.set('')

nadpis = Label(aken,text="Решение квадратного уравнения",font=("Arial Bold",20),fg="green",bg="Lightblue")
nadpis.pack(side=TOP)
a=Entry(aken,width=2,bg="Lightblue",font=("Arial Bold",30),textvariable = a)
b=Entry(aken,width=2,bg="Lightblue",font=("Arial Bold",30),textvariable = b)
c=Entry(aken,width=2,bg="Lightblue",font=("Arial Bold",30),textvariable = c)
a.place(x=0,y=50)
b.place(x=125,y=50)
c.place(x=215,y=50)

x2l = Label(aken,text="x**2+",font=("Arial Bold",20),fg="green")
xl = Label(aken,text="x+",font=("Arial Bold",20),fg="green")
Ol = Label(aken,text="=0",font=("Arial Bold",20),fg="green")
x2l.place(x=50,y=50)
xl.place(x=175,y=50)
Ol.place(x=275,y=50)

nupp=Button(aken,text="Решить",height=1,width=7,bg="green",fg="black", font="Arial 20") #.pack(side=TOP) command=vajutamine()
nupp.place(x=325,y=50)
nupp.bind('<Button-1>',okno)
solution = Label(aken,width=25,text="Решение",font=("Arial Bold",20),fg="green",bg="yellow")
solution.place(x=30,y=120)


aken.mainloop() 
