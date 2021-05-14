from tkinter import *

root=Tk()
root.title("restaurant pos")
root.geometry("800x800+300+300")
root.resizable(False, False)

def b1event():
    if(b1['text'] == 'table1'):
        b1['text'] = 'a주문/n b주문'
        b1['fg']='red'
        b1['bg'] = 'yellow'

    else:
       b1['text'] = 'table1'
       b1['fg'] = 'yellow'
       b1['bg'] = 'red'

b1=Button(root, text="table1", command = b1event,  width=20, height=7, overrelief="solid")
b1.pack()
b1.place(x=30, y=30)  

# chkValue = tk.BooleanVar() 
# chkValue.set(True)
 
# chkExample = tk.Checkbutton(root, text='Check Box', var=chkValue) 
# chkExample.grid(column=0, row=0)

def b2event():
    if(b2['text'] == 'table2'):
        b2['text'] = 'complete'
        b2['fg']='red'
        b2['bg'] = 'yellow'
    else:
       b2['text'] = 'table2'
       b2['fg'] = 'yellow'
       b2['bg'] = 'red'

    
b2=Button(root, text="table2", command = b2event,fg = 'yellow', bg = 'red',width=20, height=7, overrelief="solid")
b2.pack()
b2.place(x=300, y=30)

def b3event():
    if(b3['text'] == 'table3'):
        b3['text'] = 'complete'
        b3['fg']='red'
        b3['bg'] = 'yellow'

    else :
       b3['text'] = 'table3'
       b3['fg'] = 'yellow'
       b3['bg'] = 'red'

  
b3=Button(root, text="table3",command = b3event,fg = 'yellow', bg = 'red',width=20, height=7, overrelief="solid")
b3.pack()
b3.place(x=30, y=200)

def b4event():
    if(b4['text'] == 'table4'):
        b4['text'] = 'complete'
        b4['fg']='red'
        b4['bg'] = 'yellow'

    else:
       b4['text'] = 'table4'
       b4['fg'] = 'yellow'
       b4['bg'] = 'red'

  
b4=Button(root, text="table4",command = b4event,fg = 'yellow', bg = 'red', width=20, height=7, overrelief="solid")
b4.pack()
b4.place(x=300, y=200)


b2=Button(root, text="table2", command = b2event,fg = 'yellow', bg = 'red',width=20, height=7, overrelief="solid")
b2.pack()
b2.place(x=300, y=30)

def b5event():
    if(b5['text'] == 'table5'):
        b5['text'] = 'complete'
        b5['fg']='red'
        b5['bg'] = 'yellow'

    else :
       b5['text'] = 'table5'
       b5['fg'] = 'yellow'
       b5['bg'] = 'red'

b5=Button(root, text="table5",command = b5event,fg = 'yellow', bg = 'red',width=20, height=7, overrelief="solid")
b5.pack()
b5.place(x=30, y=370)

def b6event():
    if(b6['text'] == 'table6'):
        b6['text'] = 'complete'
        b6['fg']='red'
        b6['bg'] = 'yellow'

    else:
       b6['text'] = 'table6'
       b6['fg'] = 'yellow'
       b6['bg'] = 'red'

  
b6=Button(root, text="table6",command = b6event,fg = 'yellow', bg = 'red', width=20, height=7, overrelief="solid")
b6.pack()
b6.place(x=300, y=370)


root.mainloop()
