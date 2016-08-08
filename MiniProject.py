from tkinter import *

window = Tk()
window.title("MiniProject made by DaEun_20135179")

#top frame
top_frame = Frame(window)
top_frame.grid(row=0, column=0, columnspan=3, sticky =N)
#name label
Label(top_frame, text="name: ").grid(row=0,column=0,sticky=W)
entry_name = Entry(top_frame, width=20, bg = "green")
entry_name.grid(row=0, column=1, sticky=W)
#grade label
Label(top_frame, text="grade: ").grid(row=0,column=2,sticky=W)
entry_grade = Entry(top_frame, width=15, bg ="light green")
entry_grade.grid(row=0, column=3, sticky=E)
#number label
Label(top_frame, text="number: ").grid(row=1, column=2,sticky=W)
entry_num = Entry(top_frame, width=15, bg = "light green")
entry_num.grid(row=1, column=3, sticky=E)
#file name label_1
Label(top_frame, text="file name: ").grid(row=2, column=2,sticky=W)
entry_output = Entry(top_frame, width=15, bg = "yellow")
entry_output.grid(row=2, column=3, sticky=E)
#file name label_2
Label(top_frame, text="file name: ").grid(row=3, column=2,sticky=W)
entry_input = Entry(top_frame, width=15, bg = "yellow")
entry_input.grid(row=3, column=3, sticky=E)

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

