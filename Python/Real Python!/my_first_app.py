import tkinter as tk

def set_message():
    txt = text_enter.get()
    title_label.configure(text=txt)

window = tk.Tk()
window.title('Display_what_you_type!')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='Display_what_you_type!')
title_label.pack()

text_enter = tk.Entry(master=window)
text_enter.pack()

ok = tk.Button(master=window, text='Okay', command=set_message)
ok.pack()

window.mainloop()
