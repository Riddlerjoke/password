import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 12
    password_max = 24
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("1080x720")
window.iconbitmap("logo.ico")
window.config(background="#3CCFFF")

frame = Frame(window, bg="#3CCFFF")

width = 512
height = 512

image = PhotoImage(file="padlock.png").zoom(20).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#3CCFFF", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg=("#3CCFFF"))

label_title = Label(right_frame, text="mot de passe", font=("helvetica", 35), bg="#3CCFFF", fg="white")
label_title.pack()

password_entry = Entry(right_frame, font=("helvetica", 35), bg="#3CCFFF", fg="white")
password_entry.pack()

generate_password = Button(right_frame, text="Générer", font=("helvetica", 35), bg="#3CCFFF", fg="white", command=generate_password)
generate_password.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=E)


frame.pack(expand=YES)


window.mainloop()