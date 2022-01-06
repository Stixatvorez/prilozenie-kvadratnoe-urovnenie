from tkinter import *
from tkinter import messagebox

def vajutamine(event):
    if a.get() == "" or b.get() == '' or c.get() == '':
        messagebox.showinfo('Ошибка!',' ТЫ ШО ОПУХ! ЗАПОЛНИ ВСЕ ПОЛЯ!')    
    else:
        av = int(a.get())
        bv = int(b.get())
        cv = int(c.get())
        D = (bv)**2 - 4 * av * cv
        if D < 0:
            solution.config(text="Уравнение не имеет корней")
        elif D == 0:
            x = -1 * bv/(2 * av)
            solution.config(text="D="+str(D)+", "+'X='+str(round(x,2)))
        else:
            x1 = (-1 * bv - D ** 0.5)/(2 * av)
            x2 = (-1 * bv + D ** 0.5)/(2 * av)
            solution.config(text="D="+str(D)+", "+'X1='+str(round(x1,2))+", "+'X2='+str(round(x2,2)))

aken=Tk()
aken.title("Квадратные уравнения")

aken.geometry('600x175')

a = StringVar()
a.set('')
b = StringVar()
b.set('')
c = StringVar()
c.set('')

nadpis = Label(aken,text="Решение квадратного уравнения",font=("Arial Bold",20),fg="green")
nadpis.pack(side=TOP)

ka=Entry(aken,width=2,font=("Arial Bold",30),textvariable = a)
kb=Entry(aken,width=2,font=("Arial Bold",30),textvariable = b)
kc=Entry(aken,width=2,font=("Arial Bold",30),textvariable = c)
ka.place(x=0,y=50)
kb.place(x=125,y=50)
kc.place(x=215,y=50)

x2l = Label(aken,text="x**2+",font=("Arial Bold",20),fg="green")
xl = Label(aken,text="x+",font=("Arial Bold",20),fg="green")
Ol = Label(aken,text="=0",font=("Arial Bold",20),fg="green")
x2l.place(x=50,y=50)
xl.place(x=175,y=50)
Ol.place(x=275,y=50)

nupp=Button(aken,text="Решить",height=1,width=7,bg="green",fg="blue", font="Arial 20") #.pack(side=TOP) command=vajutamine()
nupp.place(x=325,y=50)
nupp.bind('<Button-1>',vajutamine)

solution = Label(aken,width=25,text="Решение",font=("Arial Bold",20),fg="green",bg="yellow")
solution.place(x=30,y=120)


aken.mainloop() 
