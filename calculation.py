from tkinter import *

window = Tk()
top_row = Frame(window)
top_row.grid(row = 0 , column = 0, columnspan = 2, sticky = N)
display = Entry(top_row, width = 45, bg = "light green")
display.grid()

num_pad = Frame(window)
num_pad.grid(row=1,column=0,sticky=W)

operator_pad = Frame(window)
operator_pad.grid(row=1,column=1,sticky=E)
num_pad_list = ['7','8','9','4','5','6','1','2','3','0','.','=']
operator_list = ['*','/','+','-','(',')','C']


def click(key):
    if key=='=':
        try:
            result = str(eval(display.get()))
        except:
            result ="-->error"
        display.insert(END, "="+result)
    elif key=='C':
        display.delete(0,END)
    else:
        if'=' in display.get():
            display.delete(0,END)
        display.insert(END, key)
button_groups={
    'num':{'list':num_pad_list, 'window':num_pad,'width':5,'cols':3},
    'op':{'list':operator_list,'window':operator_pad,'width':5,'cols':2},
    }

for label in button_groups.keys():
    r=0;c=0
    buttons = button_groups[label]
    for btn_text in buttons['list']:
        def cmd(x=btn_text):
            click(x)
        Button(buttons['window'],
               text=btn_text,
               width=buttons['width'],
               command = cmd).grid(row=r, column=c)
        c=c+1
        if c>=buttons['cols']:
            c=0
            r=r+1


window.mainloop()
