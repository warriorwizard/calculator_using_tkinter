from tkinter import *
root=Tk()

root.title('Calculator')

disp=Entry(root,width=40,borderwidth=5,bg='#b5a874')
disp.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def click(num):
    global b
    b=disp.get()
    a=len(disp.get())
    h=disp.insert(a,num)
    b=disp.get()
def clear():
    disp.delete(0,END)
def add():
    b=disp.get()
    global a
    a=int(b)
    global operator
    operator='+'
    disp.delete(0,END)
def mul():
    b=disp.get()
    global a
    a=int(b)
    global operator
    operator='*'
    disp.delete(0,END)
def div():
    b=disp.get()
    global a
    a=int(b)
    global operator
    operator='//'
    disp.delete(0,END)


def equal():
    b=disp.get()
    global c 
    c=int(b)
    global operated
    if operator=='+':
        operated=a+c
    elif operator=='*':
        operated=a*c
    elif operator=='//':
        operated=a/c

    disp.delete(0,END)
    disp.insert(0,operated)

btn9=Button(root,padx=40,pady=20,text='9',command=lambda:click(9) ).grid(row=1,column=0)
btn8=Button(root,padx=40,pady=20,text='8',command=lambda:click(8) ).grid(row=1,column=1)
btn7=Button(root,padx=40,pady=20,text='7',command=lambda:click(7) ).grid(row=1,column=2)
btn6=Button(root,padx=40,pady=20,text='6',command=lambda:click(6) ).grid(row=2,column=0)
btn5=Button(root,padx=40,pady=20,text='5',command=lambda:click(5) ).grid(row=2,column=1)
btn4=Button(root,padx=40,pady=20,text='4',command=lambda:click(4) ).grid(row=2,column=2)
btn3=Button(root,padx=40,pady=20,text='3',command=lambda:click(3) ).grid(row=3,column=0)
btn2=Button(root,padx=40,pady=20,text='2',command=lambda:click(2) ).grid(row=3,column=1)
btn1=Button(root,padx=40,pady=20,text='1',command=lambda:click(1) ).grid(row=3,column=2)
btn0=Button(root,padx=40,pady=20,text='0',command=lambda:click(0) ).grid(row=4,column=0)
btn_div=Button(root,padx=40,pady=20,text='/',command=div ,bg='#d9c8a3').grid(row=4,column=1)
btn_clr=Button(root,padx=39,pady=20,text='C',command=clear,bg='#8f0b0b' ).grid(row=4,column=2)
btn_add=Button(root,padx=39,pady=20,text='+',command=add, bg='#d9aca3').grid(row=5,column=0)
btn_mul=Button(root,padx=39,pady=20,text='X',command=mul,bg='#a3d9c9' ).grid(row=5,column=1)
btn_eql=Button(root,padx=39,pady=20,text='=',command=equal,bg='#4a4747' ).grid(row=5,column=2)


root.mainloop()