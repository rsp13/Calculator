from tkinter import *
from tkinter import ttk
from  tkinter import  messagebox
calc=Tk()
list1=[]
def calnum(n):
    '''if n=='.':
        num.insert(len(num.get())+n)'''
    if n in ['+','-','*','/']:
        list1.append(num.get())
        list1.append(n)
        num.delete(0,'end')
        num.focus()
    elif n=='=':
        if list1[1]=='+':
            ans=float(list1[0])+float(num.get())
        elif list1[1]=='-':
            ans=float(list1[0])-float(num.get())
        elif list1[1]=='*':
            ans=float(list1[0])*float(num.get())
        elif list1[1]=='/':
            ans=float(list1[0])/float(num.get())
        num.delete(0,'end')
        num.insert(0,ans)
        num.focus()
    elif n=='.':
        num.insert(len(num.get())+len(num.get()),n)
    else:
        l=len(n)
        num.insert(l+len(num.get()),n)
        num.focus()
def clear():
    list1.clear()
    num.delete(0,'end')
    num.focus()

calc.geometry('200x300')
calc.title('Clculator')
calc.config(background='wheat')
num=Entry(calc,width=25,bd=10,bg='cornflowerblue')
num.grid(columnspan=4, ipadx=10)
btn1=Button(calc,text='1',command=lambda:calnum('1'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn1.grid(row=2,column=0)
btn2=Button(calc,text='2',command=lambda :calnum('2'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn2.grid(row=3,column=0)
btn3=Button(calc,text='3',command=lambda :calnum('3'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn3.grid(row=4,column=0)
btn4=Button(calc,text='4',command=lambda:calnum('4'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn4.grid(row=2,column=1)
btn5=Button(calc,text='5',command=lambda :calnum('5'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn5.grid(row=3,column=1)
btn6=Button(calc,text='6',command=lambda :calnum('6'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn6.grid(row=4,column=1)
btn7=Button(calc,text='7',command=lambda :calnum('7'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn7.grid(row=2,column=2)
btn8=Button(calc,text='8',command=lambda :calnum('8'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn8.grid(row=3,column=2)
btn9=Button(calc,text='9',command=lambda :calnum('9'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btn9.grid(row=4,column=2)
btnplus=Button(calc,text='+',command=lambda :calnum('+'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btnplus.grid(row=2,column=3)
btnmin=Button(calc,text='-',command=lambda :calnum('-'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btnmin.grid(row=3,column=3)
btnmul=Button(calc,text='*',command=lambda :calnum('*'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btnmul.grid(row=4,column=3)
btndiv=Button(calc,text='/',command=lambda :calnum('/'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btndiv.grid(row=5,column=3)
btncelar=Button(calc,text='CE',command=lambda :clear(),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btncelar.grid(row=5,column=0)
btnm0=Button(calc,text='0',command=lambda :calnum('0'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btnm0.grid(row=5,column=1)
btndot=Button(calc,text='.',command=lambda :calnum('.'),height=1,width=4,bg='darkgrey',relief='groove',justify='center')
btndot.grid(row=5,column=2)
btnequal=Button(calc,text='=',command=lambda :calnum('='),height=2,width=20,bg='darkgrey',relief='groove',justify='center')
btnequal.grid(columnspan=5,ipadx=10)
calc.mainloop()