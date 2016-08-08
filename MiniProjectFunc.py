from MiniProject import *
import pickle

book=[ ]

# check state frame
def check_state(msg):
    output_state.delete(0.0, END)
    output_state.insert(END, msg)


# check result frame
current_state = 'number order'
def check(x):
    global book
    global current_state
    output_data.delete(0.0, END)

    if x == 'number order':
        book.sort(key = lambda i:i[0])
        check_state('Sorted by number')
    elif x == 'name order':
        book.sort(key = lambda i:i[1])
        check_state('Sorted by name')
    elif x == 'descending':
        book.sort(key = lambda i:i[2])
        check_state('Sorted by score in descending sort order')
    elif x == 'ascending':
        book.sort(key = lambda i:i[2], reverse=True)
        check_state('Sorted by score in ascending sort order')

    for data in book:
        output_data.insert(END, data)
        output_data.insert(END, '\n')

    current_state = x

def click_func(x):
    global book

    if x == 'add':
        try:
            book.append([int(entry_num.get()), entry_name.get(), float(entry_grade.get())])
            check(current_state)
            check_state('Data is added')
        except ValueError:
            refresh_state('Invalid')
    elif x == 'delete':
        t = 0
        try:
            for i in book:
                if i[0] == int(entry_num.get()):
                    del book[t]
                    check(current_state)
                    check_state('Data is deleted')
                    break
                t += 1
        except ValueError:
            check_state('Invalid')
    elif x == 'save':
        try:
            fout = open(entry_output.get(), 'wb')
            pickle.dump(book, fout)
            fout.close()
            check(current_state)
            check_state('Data is saved')
        except FileNotFoundError:
            check_state('Invalid')
    elif x == 'open':
        try:
            fin = open(entry_input.get(), 'rb')
            book = pickle.load(fin)
            check(current_state)
            check_state('Data is loaded')
        except FileNotFoundError:
            check_state('Invalid')



pad_list=['add','delete','save','open']
c=0
for func in pad_list:
    def click(x=func):
        click_func(x)
    Button(top_frame, text=func, width=5, command=click).grid(row=c, column=5, sticky=E)
    c+=1

# Sorting buttons
def click_sort(x):
    check(x)

num_pad_list = ['number order','name order','descending','ascending']

r=0
for btn in num_pad_list:
    Button(middle_frame, text=btn, width=12, command =click).grid(row=4, column=r)
    r+=1
    


window.mainloop()


