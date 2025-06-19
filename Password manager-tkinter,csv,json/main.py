from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '.', '@', '^', '-', '_', '=', '+',
           ',', '?', ';', ':', '{', '}', '[', ']', "'", '"']


def generate_password():
    password_entry.delete(0, END)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random_password = password_letters + password_numbers + password_symbols

    random.shuffle(random_password)
    final_password = ''.join(random_password)

    password_entry.insert(0, string=final_password)

    pyperclip.copy(final_password)


#  ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    # data = f'{website_name} | {username} | {password}\n'

    new_data = {
        website_name: {
            'username': username,
            'password': password
        }
    }

    if len(website_name) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message='Some fields are empty. Please fill them.')

    else:
        is_okay = messagebox.askokcancel(title=website_name, message=f'Details entered:\n\nUsername: {username}\n\n'
                                                                     f'Password: {password}\n\nIs it okay to save?')
        if is_okay:
            try:
                with open('data_file.json', 'r') as file:  # In json we have 'r' and 'w' only.
                    # Reading old data
                    data = json.load(file)  # data is a py dictionary
                    # Updating old data
                    data.update(new_data)  # update is func of dictionary to add dictionary to it
                    #  file.write(data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open('data_file.json', 'w') as file:
                    # Saving updated data
                    # noinspection PyUnboundLocalVariable
                    json.dump(data, file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title='Successful!', message='Details added to file successfully.')


# ----------------------------- SEARCH PASSWORD ----------------------------------#
def search_password():
    try:
        data = json.load(open('data_file.json'))
    except FileNotFoundError:
        messagebox.showerror(title='No Data file Found.', message='File is empty.No passwords found.')
    else:
        website_name = website_entry.get().title()
        if len(website_name) == 0:
            messagebox.showerror(title='Error', message='Website name is required to search.')
        else:
            if website_name in data:
                website_credentials = data[website_name.title()]
                pyperclip.copy(website_credentials['password'])
                messagebox.showinfo(title=f'{website_name} Credentials',
                                    message=f"Username: {website_credentials['username']}\n"
                                            f"Password: {website_credentials['password']}\n\n"
                                            f"Password copied to Clipboard")
            else:
                messagebox.showinfo(title='Website Credentials Not Found',
                                    message=f'No details for {website_name} exists.\nPlease try again')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager GUI App')
window.config(pady=60, padx=60, bg='black')

canvas = Canvas(width=200, height=200, highlightthickness=0, bg='pink')
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#  Labels
website_label = Label(text="Website :", font=("Arial", 10, 'bold'), bg='black', fg='white')
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username :", font=("Arial", 10, 'bold'), bg='black', fg='white')
email_label.grid(row=2, column=0)

password_label = Label(text='Password :', font=("Arial", 10, 'bold'), bg='black', fg='white')
password_label.grid(row=3, column=0)

null_label = Label(bg='black', fg='white')
null_label.grid(row=4, column=0)

#  Entry
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1, column=1)

username_entry = Entry(width=54)
username_entry.insert(END, string='yaswanthaparagada@gmail.com')
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

#  Buttons
generate_button = Button(text="Generate Password", command=generate_password, bg='pink', fg='red')
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=43, command=save_password, bg='pink', fg='red')
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text='Search', width=15, bg='pink', fg='red', command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()
