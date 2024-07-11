from tkinter import *
import os


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        print("Please don't leave any fields empty!")
    else:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        
        website_entry.delete(0, END)
        email_user_entry.delete(0, END)
        password_entry.delete(0, END)
        email_user_entry.insert(0, "takuya.genesys01@gmail.com")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Buttons
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=3)
website_entry.focus()
email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=3)
email_user_entry.insert(0, "takuya.genesys01@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()