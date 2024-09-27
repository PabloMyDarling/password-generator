from tkinter import *
from random import choice

letters = list("abcdefghijklmnopqrstuvwxyz".upper())
lc_letters = list("abcdefghijklmnopqrstuvwxyz")
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
chars = list("!@#$%^&*()-_=+[].,<>/';:~|")

def get_password():
    global letters, lc_letters, nums, chars, password
    
    passform1 = choice(letters)+choice(letters)+choice(lc_letters)+choice(nums)+choice(nums)+choice(chars)+choice(letters)+choice(lc_letters)+choice(chars)+choice(chars)
    passform2 = choice(nums)+choice(chars)+choice(letters)+choice(lc_letters)+choice(chars)+choice(nums)+choice(lc_letters)+choice(letters)+choice(chars)+choice(chars)
    
    password = choice([passform1, passform2])

    return password

root = Tk()
root.title("Password Generator")
root.config(bg="purple")
root.geometry("350x125")

Label(root, text="Password Generator", bg="purple", fg="white", font=("Arial", 25, "bold")).pack(pady=2)

password_frame = Frame(root, bg="purple")
password_frame.pack(expand=True)

password = get_password()
passlabel = Label(password_frame, text=password, bg="purple", fg="white", font=("Arial", 18, "bold"))
passlabel.pack()
def copy():
    global password, passlabel
    passlabel.config(text="Please wait...")
    root.clipboard_clear()
    root.clipboard_append(password)
    passlabel.config(text=password)
Button(password_frame, text="Get Password", width=12, bg="blue", fg="white", command=lambda: passlabel.config(text=get_password())).pack(side=LEFT, pady=2, padx=3)
Button(password_frame, text="Copy Password", width=12, bg="blue", fg="white", command=copy).pack(side=LEFT, pady=2)

mainloop()
