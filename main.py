from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry('750x550')
win.config(bg='black')


# Button Function


def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'),
                                                      ('All file', '*.txt')))
    img = Image.open(open_file).convert('RGB')
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image = img


def hide():
    global hide_msg
    password = code.get()
    if password == '1234':
        msg = text1.get(1.0, END)
        hide_msg = lsb.hide(str(open_file), msg)
        messagebox.showinfo('Success', 'Your message is successfully hidden, please save your image.')
    elif password == '':
        messagebox.showinfo('Error', 'Please enter Secret Key')
    else:
        messagebox.showinfo('Error', 'Wrong Secret Key')
        code.set('')


def save_img():
    hide_msg.save('Secret_file.png')
    messagebox.showinfo('Save', 'Image has been successfully saved.')


def show():
    password = code.get()
    if password == '1234':
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0, END)
        text1.insert(END, show_msg)
    elif password == '':
        messagebox.showinfo('Error', 'Please enter Secret Key')
    else:
        messagebox.showinfo('Error', 'Wrong Secret Key')
        code.set('')


# Logo
pic = Image.open('logo.png')
logo = ImageTk.PhotoImage(pic)
Label(win, image=logo, bd=0).place(x=10, y=10)

# Heading
Label(win, text='Steganographer', font='"Times New Roman" 40 bold', bg='black', fg='green').place(x=205, y=15)

# Frame 1
f1 = Frame(win, width=250, height=220, bd=5, bg='beige')
f1.place(x=60, y=120)
lf1 = Label(f1, bg='beige')
lf1.place(x=0, y=0)

# Frame 2
f2 = Frame(win, width=320, height=220, bd=5, bg='white')
f2.place(x=380, y=120)
text1 = Text(f2, font='ariel 15 bold', wrap=WORD)
text1.place(x=0, y=0, width=310, height=210)

# Label for Secret Key
Label(win, text='Enter Secret Key', font='20', bg='black', fg='yellow').place(x=260, y=370)

# Entry Widget for Secret Key
code = StringVar()
e = Entry(win, textvariable=code, bd=2, font='impact 12 bold', show='*')
e.place(x=258, y=400)

# Buttons
open_button = Button(win, text='Open Image', bg='blue', fg='white', font='ariel 12 bold', cursor='hand2',
                     command=open_img)
open_button.place(x=100, y=450)

save_button = Button(win, text='Save Image', bg='green', fg='white', font='ariel 12 bold', cursor='hand2',
                     command=save_img)
save_button.place(x=240, y=450)

hide_button = Button(win, text='Hide Data', bg='red', fg='white', font='ariel 12 bold', cursor='hand2', command=hide)
hide_button.place(x=430, y=450)

show_button = Button(win, text='Show Data', bg='orange', fg='white', font='ariel 12 bold', cursor='hand2', command=show)
show_button.place(x=560, y=450)

mainloop()
