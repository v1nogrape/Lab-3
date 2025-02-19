import tkinter as tk
import random
import string
import pygame

def generate_block():
    letters = random.choices(string.ascii_uppercase, k=3)
    digits = random.choices(string.digits, k=2)
    block = letters + digits
    random.shuffle(block)
    return ''.join(block)

def generate_password():
    blocks = [generate_block() for _ in range(3)]
    return '-'.join(blocks)

def update_password():
    password = generate_password()
    Text_gen.delete(0, tk.END)
    Text_gen.insert(0, password)


pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

window = tk.Tk()
window.geometry('265x380')
window.resizable(width=False, height=False)

bg_img = tk.PhotoImage(file='pupupu.png')
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.85, anchor='center')

lbl_gen = tk.Label(frame, text='Gen', font=('Arial', 15), fg='black')
lbl_gen.grid(column=0, row=0, padx=5, pady=5)
Text_gen = tk.Entry(frame, width=25)
Text_gen.insert(0, 'XXXXX-XXXXX-XXXXX')
Text_gen.grid(column=0, row=1, padx=5, pady=5)

btn_gen = tk.Button(frame, text='*тык*', command=update_password)
btn_gen.grid(column=0, row=3, padx=10, pady=10)

window.mainloop()