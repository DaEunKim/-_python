from tkinter import *
import pickle

window = Tk()
window.title("MiniProject made by DaEun_20135179")

classbook=[ ]

#top frame
top_frame = Frame(window)
top_frame.grid(row=0, column=0, columnspan=3, sticky =N)
#name label
Label(top_frame, text="name: ").grid(row=0,column=0,sticky=W)
entry_name = Entry(top_frame, width=20, bg = "light green")
entry_name.grid(row=0, column=1, sticky=W)
#grade label
Label(top_frame, text="grade: ").grid(row=0,column=2,sticky=W)
entry_grade = Entry(top_frame, width=7, bg ="light green")
entry_grade.grid(row=0, column=3, sticky=E)
#number label
Label(top_frame, text="number: ").grid(row=1, column=2,sticky=W)
entry_num = Entry(top_frame, width=5, bg = "light green")
entry_num.grid(row=1, column=3, sticky=E)
#file name label_1
Label(top_frame, text="file name: ").grid(row=2, column=2,sticky=W)
entry_output = Entry(top_frame, width=15, bg = "yellow")
entry_output.grid(row=2, column=3, sticky=E)
#file name label_2
Label(top_frame, text="file name: ").grid(row=3, column=2,sticky=W)
entry_input = Entry(top_frame, width=15, bg = "yellow")
entry_input.grid(row=3, column=3, sticky=E)

# Refresh state frame
def refresh_state(msg):
    output_state.delete(0.0, END)
    output_state.insert(END, msg)


#middle frame
middle_frame = Frame(window)
middle_frame.grid(row=5, column=0, sticky=S)


#result frame
result_frame = Frame(window)
result_frame.grid(row=6, column=0, sticky = S)
output_data = Text(result_frame, width = 75, height = 10, wrap = WORD, background = "pink")
output_data.grid(row = 5, column = 0, sticky = W)

#bottom
output_state = Text(result_frame, width = 75, height=1, wrap = WORD, background = "red")
output_state.grid(row = 6, column =0, sticky = W)


# Refresh result frame
current_state = 'number order'
def refresh(x):
    global classbook
    global current_state
    output_data.delete(0.0, END)

    if x == 'number order':
        classbook.sort(key = lambda i:i[0])
        refresh_state('Sorted by number')
    elif x == 'name order':
        classbook.sort(key = lambda i:i[1])
        refresh_state('Sorted by name')
    elif x == 'descending order':
        classbook.sort(key = lambda i:i[2])
        refresh_state('Sorted by score in descending sort order')
    elif x == 'ascending order':
        classbook.sort(key = lambda i:i[2], reverse=True)
        refresh_state('Sorted by score in ascending sort order')

    for data in classbook:
        output_data.insert(END, data)
        output_data.insert(END, '\n')

    current_state = x


def click_func(x):
    global classbook

    if x == 'add':
        try:
            classbook.append([int(entry_num.get()), entry_name.get(), float(entry_grade.get())])
            refresh(current_state)
            refresh_state('Data is added')
        except ValueError:
            refresh_state('Invalid input')
    elif x == 'delete':
        t = 0
        try:
            for i in classbook:
                if i[0] == int(entry_num.get()):
                    del classbook[t]
                    refresh(current_state)
                    refresh_state('Data is deleted')
                    break
                t += 1
        except ValueError:
            refresh_state('Invalid input')
    elif x == 'save':
        try:
            fout = open(entry_output.get(), 'wb')
            pickle.dump(classbook, fout)
            fout.close()
            refresh(current_state)
            refresh_state('Data is saved')
        except FileNotFoundError:
            refresh_state('Invalid file name')
    elif x == 'open':
        try:
            fin = open(entry_input.get(), 'rb')
            classbook = pickle.load(fin)
            refresh(current_state)
            refresh_state('Data is loaded')
        except FileNotFoundError:
            refresh_state('Cannot find file')

pad_list=['add','delete','save','open']
c=0
for bb in pad_list:
    def click(x=bb):
        click_func(x)
    Button(top_frame, text=bb, width=5, command=click).grid(row=c, column=5, sticky=E)
    c+=1

# Sorting buttons
def click_sort(x):
    refresh(x)

num_pad_list = ['number order','name order','descending order','ascending order']

r=0
for btn in num_pad_list:
    Button(middle_frame, text=btn, width=12, command =click).grid(row=4, column=r)
    r+=1
    


window.mainloop()

