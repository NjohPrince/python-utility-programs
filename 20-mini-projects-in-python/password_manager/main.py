from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

FONT_NAME = "Courier"
FONT = (FONT_NAME, 10, "bold")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="white")


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: " \
                                                              f"\nEmail: {email} \nPassword: {password} " \
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)
            website_entry.focus()


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)


canvas = Canvas(width=200, height=250, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 125, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=FONT, bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=FONT, bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT, bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=44)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=44)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(index=0, string="suprememajor@gmail.com")
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass_button = Button(text="Generate Password", width=18, command=generate_password)
gen_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
