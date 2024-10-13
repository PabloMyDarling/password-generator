from tkinter import *
import string
from random import choice

root = Tk()
root.title("Password Generator")
root.geometry("420x300")

Label(root, text="Password Generator", font=("TkDefaultFont", 20, "bold")).pack(pady=2)

#settings
chars = StringVar(root, "12")
letters = BooleanVar(root, True)
lowercase_letters = BooleanVar(root, True)
symbols = BooleanVar(root, True)
numbers = BooleanVar(root, True)

password = StringVar(root)

def get_password(e: Event | None = None):
    Password = ""
    can_add = []
    if letters.get(): can_add.append("letters")
    if lowercase_letters.get(): can_add.append("lowercase letters")
    if symbols.get(): can_add.append("symbols")
    if numbers.get(): can_add.append("numbers")
    for _ in range(1, int(chars.get())):
        try: to_add = choice(can_add)
        except IndexError:
            password.set("Tick at least one of the options!")
            return
        if to_add == "letters": Password = f"{Password}{choice(list(string.ascii_uppercase))}"
        elif to_add == "lowercase letters": Password = f"{Password}{choice(list(string.ascii_lowercase))}"
        elif to_add == "numbers": Password = f"{Password}{choice(range(0, 9))}"
        elif to_add == "symbols": Password = f"{Password}{choice(list(string.punctuation))}"
    
    password.set(Password)

def copy_password(e: Event | None = None):
    root.clipboard_clear()
    root.clipboard_append(password.get())

cool = Entry(root, state=DISABLED, textvariable=password, fg="#000", justify=CENTER, borderwidth=0, font=("TkDefaultFont", 14))
cool.pack(fill=X, padx=1)

get_password()

buttons = Frame(root)
buttons.pack(pady=2)
n = Button(buttons, text="New", command=get_password, width=7, cursor="hand2", bg="#fff"); n.pack(side=LEFT, padx=3)
c = Button(buttons, text="Copy", command=copy_password, width=7, cursor="hand2", bg="#fff"); c.pack(side=LEFT)
n.bind("<Enter>", lambda e: n.config(bg="#f2f2f2"))
n.bind("<Leave>", lambda e: n.config(bg="#fff"))
c.bind("<Enter>", lambda e: c.config(bg="#f2f2f2"))
c.bind("<Leave>", lambda e: c.config(bg="#fff"))

password_settings = LabelFrame(root, text="Password Settings", width=140, height=160)
password_settings.pack(expand=True)
password_settings.propagate(False)


v = Frame(password_settings); v.pack(fill=X, padx=1)
Label(v, text="Characters").pack(side=LEFT)
characters_entry = Entry(v, justify=CENTER, width=4, textvariable=chars)
characters_entry.pack(side=RIGHT)
def check(e: Event | None = ...):
    try:
        if int(chars.get()) > 32: chars.set("")
    except ValueError: chars.set("")
characters_entry.bind("<KeyRelease>", check)

w = Frame(password_settings); w.pack(fill=X, padx=1)
Label(w, text="Letters").pack(side=LEFT)
Checkbutton(w, text="", variable=letters).pack(side=RIGHT)

x = Frame(password_settings); x.pack(fill=X, padx=1)
Label(x, text="Letters (lowercase)", font=("TkDefaultFont", 8)).pack(side=LEFT)
Checkbutton(x, text="", variable=lowercase_letters).pack(side=RIGHT)

y = Frame(password_settings); y.pack(fill=X, padx=1)
Label(y, text="Symbols").pack(side=LEFT)
Checkbutton(y, text="", variable=symbols).pack(side=RIGHT)

z = Frame(password_settings); z.pack(fill=X, padx=1)
Label(z, text="Numbers").pack(side=LEFT)
Checkbutton(z, text="", variable=numbers).pack(side=RIGHT)

mainloop()
