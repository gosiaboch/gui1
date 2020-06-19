import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()

greeting = tk.Label(window, text="Witamy w generatorze hasła! Proszę wpisać czy chcesz hasło silne czy słabe:")
greeting.pack()

choice = tk.Entry(window)
choice.pack()

def silneHaslo():
    malaLitera = random.choices("qwertyuiopasdfghjklzxcvbnm")
    duzaLitera = random.choices("QWERTYUIOPASDFGHJKLZXCVBNM")
    symbol = random.choices("!@#$%^&*<>?,.")
    liczba = random.choices("1234567890")
    x = malaLitera + duzaLitera + symbol + liczba + liczba + malaLitera + duzaLitera + liczba + malaLitera + symbol
    random.shuffle(x)
    result = "".join(x)
    return result

def slabeHaslo():
    slowa = ["kawa", "arbuz", "podkowa", "mango", "piesek"]
    liczba = random.choices("1234567890")
    y = random.choices(slowa) + liczba
    result2 = "".join(y)
    return result2

def check_choice():
    if choice.get() == "silne":
        text = silneHaslo()
    elif choice.get() == "słabe":
        text = slabeHaslo()

    messagebox.showinfo("Twoje wygenerowane hasło to", text)

submit = tk.Button(window, text="Submit", command=check_choice)
submit.pack()

window.mainloop()

import string
import random

random.choice(string.ascii_letters)