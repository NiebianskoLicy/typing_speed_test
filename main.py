import tkinter
from tkinter import *
import random
import json
import time

window = Tk()
window.title("Typing Speed Test")
window.geometry("700x450")

font = ("Arial", 14)
timer = 60

# TODO 1: fix countdown
# TODO 2: create word count
# TODO 3: finish after reaching to 0 seconds

with open("words.json", "r") as f:
     text = json.load(f)["text"]

def start_timer(timer):
    user_text.config(state=NORMAL)
    window.after(1000, start_timer, timer)
    timer -= 1
    countdown_text.config(text=f"{timer}")

typ_sp_text = Text(window, height=8, width=50, font=font, wrap=WORD)
typ_sp_text.insert(END, text)
typ_sp_text.place(x=10, y=10)
typ_sp_text.config(state=DISABLED)

user_text = Text(window, height=8, width=50, font=font)
user_text.place(x=10, y=220)
user_text.config(state=DISABLED)

start_button = Button(window, text="Start", command=lambda : start_timer(timer))
start_button.config(font=("Arial", 14),width=5)
start_button.place(x=580, y=361)

countdown_text = Label(
    window,
    text="Countdown:\n60",
    font=("Arial", 14),
)
countdown_text.config()
countdown_text.place(x=580, y=50)

window.mainloop()
