# -*- coding: utf-8 -*-
from tkinter import *
import math
from PIL import Image, ImageTk

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        params = ['ctverec', 'obdelnik', 'trojuhelnik']

        self.button = Button(frame, text="ende", fg="red", command=master.destroy)
        self.button.pack(side=LEFT)

        self.button2 = Button(frame, text='potvrd', fg="blue", command=self.choice)
        self.button2.pack(side=LEFT)

        self.hi_there = Button(frame, text="check", command=self.check)
        self.hi_there.pack(side=LEFT)

        self.tvar = StringVar(frame)
        self.tvar.set('0') # standardní hodnota

        self.tvarvolba = OptionMenu(frame, self.tvar, *params)
        self.tvarvolba.pack(side=LEFT)

        self.button3 = Button(frame, text="calc", command=self.choice2)
        self.button3.pack()

    def check(self):
        print('check ok')

    def choice(self):
        if self.tvar.get() == "ctverec":
            print('ctv')
            self.ctverec()

        elif self.tvar.get() == 'obdelnik':
            print('obd')
            self.obdelnik()

        elif self.tvar.get() == 'trojuhelnik':
            print('tro')
            self.trojuhelnik()

        else:
            print('troj')

    def ctverec(self):
        self.canvas = Canvas(root)
        self.canvas.create_rectangle(130, 110, 290, 270)
        self.canvas.pack()
    
        im = Image.open("src/ctverec.jpg")
        im.show()

        self.text = Text()
        self.text.pack()
        self.text.insert(END, "ctverec :")
        self.text.insert(END, '\n')
        self.text.insert(END, "obvod = 4a")
        self.text.insert(END, '\n')
        self.text.insert(END, "obsah = a^2")
        
        self.strana = StringVar()
        self.strana.set(0)

        self.vstup = Entry(textvariable=self.strana)
        self.vstup.pack()

    def cti_ctverec(self):
        print(self.strana.get())
        self.text.insert(END, '\n')
        self.text.insert(END, 'obvod ctverce o strane {} je {}'.format(self.strana.get(), 4*int(self.strana.get())),'red')
        self.text.insert(END, '\n')
        self.text.insert(END, 'obsah ctverce o strane {} je {}'.format(self.strana.get(), int(self.strana.get())*int(self.strana.get())), 'red')
        self.text.tag_config('red', foreground="red")

    def obdelnik(self):
        self.canvas = Canvas(root)
        self.canvas.create_rectangle(130, 110, 290, 270)
        self.canvas.pack()
        
        im = Image.open("src/obdelnik.jpg")
        im.show()

        self.text = Text()
        self.text.pack()
        self.text.insert(END, "obdelnik :")
        self.text.insert(END, '\n')
        self.text.insert(END, "obvod = 2*(a+b)")
        self.text.insert(END, '\n')
        self.text.insert(END, "obsah = a*b")
        
        self.strana = StringVar()
        self.strana.set(0)

        self.strana2 = StringVar()
        self.strana2.set(0)

        self.vstup = Entry(textvariable=self.strana)
        self.vstup.pack()

        self.vstup2 = Entry(textvariable=self.strana2)
        self.vstup2.pack()

    def cti_obdelnik(self):
        print(self.strana.get())
        print(self.strana2.get())
        a = int(self.strana.get())
        b = int(self.strana2.get())

        self.text.insert(END, '\n')
        self.text.insert(END, 'obvod obdelniku o strane {} a {} je {}'.format(a,b,2*(a+b)),'red')
        self.text.insert(END, '\n')
        self.text.insert(END, 'obsah obdelniku o strane {} a {} je {}'.format(a,b,a*b), 'red')
        self.text.tag_config('red', foreground="red")

    def trojuhelnik(self):
        self.canvas = Canvas(root)
        points = [0,0 , 100,0 , 50,100 ]
        self.canvas.create_polygon(points)
        self.canvas.pack()
        
        im = Image.open("src/trojuhelnik.jpg")
        im.show()

        self.text = Text()
        self.text.pack()
        self.text.insert(END, "trojuhelnik :")
        self.text.insert(END, '\n')
        self.text.insert(END, "obvod = a+b+c")
        self.text.insert(END, '\n')
        self.text.insert(END, "obsah = sqrt(s*(s-a)(s-b)(s-c)) kde s = 1/2 obvodu")
        
        self.strana = StringVar()
        self.strana.set(0)

        self.strana2 = StringVar()
        self.strana2.set(0)

        self.strana3 = StringVar()
        self.strana3.set(0)

        self.vstup = Entry(textvariable=self.strana)
        self.vstup.pack()

        self.vstup2 = Entry(textvariable=self.strana2)
        self.vstup2.pack()

        self.vstup3 = Entry(textvariable=self.strana3)
        self.vstup3.pack()

    def cti_trojuhelnik(self):
        print(self.strana.get())
        print(self.strana2.get())
        print(self.strana3.get())
        a = int(self.strana.get())
        b = int(self.strana2.get())
        c = int(self.strana3.get())

        s = (1/2)*(a+b+c)

        self.text.insert(END, '\n')
        self.text.insert(END, 'obvod trojuhelniku o stranach {}, {} a {} je {}'.format(a,b,c,a+b+c),'red')
        self.text.insert(END, '\n')
        self.text.insert(END, 'obsah trojuhelniku o stranach {}, {} a {} je {}'.format(a,b,c,math.sqrt(s*(s-a)*(s-b)*(s-c))), 'red')
        self.text.tag_config('red', foreground="red")

    def choice2(self):
        if self.tvar.get() == 'obdelnik':
            self.cti_obdelnik()

        elif self.tvar.get() == 'ctverec':
            self.cti_ctverec()

        elif self.tvar.get() == 'trojuhelnik':
            self.cti_trojuhelnik()

        else:
            print('err man')

if __name__=="__main__":

    root = Tk()
    app = App(root)
    root.mainloop()