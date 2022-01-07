from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_) 
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
#def grafik(event):
  # graf,d,t=lahenda()
#if grafik==True:
     #a1=float(a.get)
     #b1=float(b.get)
     #c1=float(c.get)
     #x0=(-b1)/(2*a1)
     #y0=a1*x0*x0+b1*x0+c1
     #x=np.arange(x0-10,x0+10,0.5)
     #y=a1*x*x+b1*x+c1
     #fig=plt.figure()
     #plt.plot(x,y,"b:o",x0,y0,"r-d")
     #plt.title("Квадратное уравнение")
     #plt.ylabel("y")
     #plt.xlabel("x")
    # plt.grid(True)
    # plt.show()
     #text=f"Вершина параболлы({x0},{y0})"
#else:
     #text=f"График нет возможности построить"
     #solution.config(text=f"D={D}\n{t}\n{text}")
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

nupp=Button(aken,text="Решить",height=1,width=7,bg="green",fg="black", font="Arial 20") 
nupp.place(x=325,y=50)
nupp.bind('<Button-1>',okno)
nupp=Button(aken,text="график",height=1,width=7,bg="green",fg="black", font="Arial 20") 
nupp.bind('<Button-1>',okno)
nupp.place(x=450,y=50)
solution = Label(aken,width=25,text="Решение",font=("Arial Bold",20),fg="green",bg="yellow")
solution.place(x=30,y=120)

#i1=PhotoImage(file="kish.png")
#i2=PhotoImage(file="a1.png")
#i3=PhotoImage(file="b1.png")
#var=StringVar()
#var.set(1)
#r1=Radiobutton(aken,image=i1,variable=var,value="1",command=valik)
#r2=Radiobutton(aken,image=i2,variable=var,value="2",command=valik)
#r3=Radiobutton(aken,image=i3,variable=var,value="3",command=valik)


#lbl.pack()
#nupp.pack()#side=LEFT,TOP,RIGHT
#nupp1.pack()
#txt.pack()
#r1.pack()
#r2.pack()
#r3.pack()
aken.mainloop() 
