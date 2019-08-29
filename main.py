from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to my app")
window.geometry("350x200")

# lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# txt = Entry(window, width=10, state='disabled')
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()
# btn = Button(window, text="Click me", bg="orange", fg="red")
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click me", command=clicked)
btn.grid(column=2, row=0)

combo = Combobox(window)
combo["values"] = (1, 2, 3, 4, 5, "Text")
combo.current(3)
combo.grid(column=0, row=1)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=1, row=1)

# rad1 = Radiobutton(window, text="First", value=1, command=clicked)
rad_state = IntValue()
rad1 = Radiobutton(window, text="First", value=1, variable=rad_state)
rad2 = Radiobutton(window, text="Second", value=2, variable=rad_state)
rad3 = Radiobutton(window, text="Third", value=3, variable=rad_state)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)
window.mainloop()
