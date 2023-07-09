from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pw():
    password_input.delete(0,END)
    passchars = []
    for i in range (0,random.randint(10,16)):
        passchars.append(random.choice(letters))
    for i in range (0,random.randint(2,4)):
        passchars.append(random.choice(numbers))
    for i in range (0,random.randint(2,4)):
        passchars.append(random.choice(symbols))
    random.shuffle(passchars)
    to_write  = "".join(passchars)
    password_input.insert(0,to_write)
    pyperclip.copy(to_write)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as my_file:
        website = website_input.get()
        username = username_input.get()
        password = password_input.get()
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok == TRUE:
                my_file.writelines(website +','+username+','+password+'\n')
                website_input.delete(0,END)
                username_input.delete(0,END)
                password_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Mangager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)
canvas.grid(column=1,row= 0)


website_label = Label(text="Website")
website_label.grid(column=0,row= 1, sticky='w')

website_input = Entry(width=35)
website_input.grid(columnspan = 2, row=1, column=1, sticky='w')
website_input.focus()


username_label = Label(text="Username/Email")
username_label.grid(row=2, column=0, sticky='w')

username_input = Entry(width=35)
username_input.grid(columnspan = 2, row=2, column=1, sticky='w')
username_input.insert(0,"ben.bonulo@hotmail.com")



password_label = Label(text="Password")
password_label.grid(row=3, column=0, sticky='w')

password_input = Entry(width=35)
password_input.grid(row=3, column=1, sticky='w')

generate_pw = Button(text="Generate", width=10,command=generate_pw)
generate_pw.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row =4, column=1, columnspan=2)

window.mainloop()
