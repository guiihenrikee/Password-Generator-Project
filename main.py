from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

def find_password():
    web_entry = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if web_entry in data:
            email = (data[web_entry]['email'])
            password = (data[web_entry]['password'])
            messagebox.showinfo(title=f"{web_entry}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {web_entry} exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email_user = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email_user,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email_user) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  #READING OLD DATA
        except FileNotFoundError:
            print("File not found error.\nCreating new file and writing new data.")
            data = new_data
        except json.JSONDecodeError:
            print("JSON decode error.\nWriting new data.")
            data = new_data
        else:
            print("Adding new data to file.")
            data.update(new_data)        #UPDATING OLD DATA WITH NEW DATA
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4) #SAVING UPDATED DATA
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_user_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img_lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_lock)
canvas.grid(column=1, row=0)

#Labels
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

#Entrys
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=1, sticky="W")
website_entry.focus()
email_user_entry = Entry(width=55)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="W")
password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, sticky="W")

#Buttons
pass_gen_button = Button(text="Generate Password", width=13, command=generate_password)
pass_gen_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
