from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice((letters)) for x in range(randint(8, 10))]
    password_symbols = [choice((symbols)) for x in range(randint(2, 4))]
    password_numbers = [choice((numbers)) for x in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email_user) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the datails entered: \nEmail: {email_user}\n"
                                                      f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.writelines(f"{website} | {email_user} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img_lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_lock)
canvas.grid(column=1, row=0)

invisible_label = Label()
invisible_label.grid(column=0, row=0)
invisible_label2 = Label()
invisible_label2.grid(column=2, row=0)

website_label = Label(text="Website:", font=("verdana", 10, "bold"))
website_label.grid(column=0, row=1, sticky="E")

email_user_label = Label(text="Email/Username:", font=("verdana", 10, "bold"))
email_user_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:", font=("verdana", 10, "bold"))
password_label.grid(column=0, row=3, sticky="E")

website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

email_user_entry = Entry(width=55)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_user_entry.insert(END, "gui.ghrp@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="W")

pass_gen_button = Button(text="Generate Password", width=13, command=generate_password)
pass_gen_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
