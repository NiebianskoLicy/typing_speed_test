from tkinter import *
import json

window = Tk()
window.title("Typing Speed Test")
window.geometry("720x450")

font = ("Arial", 14)
timer = 60

# TODO 2: fix word count
# TODO 3: finish after reaching to 0 seconds

with open("words.json", "r") as f:
     text = json.load(f)["text"]


def start_timer(timer):
    user_text.config(state=NORMAL)
    countdown_text.after(1000,start_timer, timer-1)
    timer -= 1
    countdown_text.config(text=f"Countdown:\n{timer}")

    word_per_sec = word_count()/(timer/60)
    wps_text = Label(window, text=f"WPS:\n {word_per_sec}", font=("Arial", 14))
    wps_text.after(1000, word_count, )
    wps_text.place(x=605, y=200)


def word_count():
    word_per_sec = 0
    count_text = user_text.get("1.0", END)
    word = ""
    print(word_per_sec)
    for letter in count_text:
        word += letter
        if letter == " ":
            word = ""
            if word in text:
                word_per_sec += 1
                return word_per_sec
    return word_per_sec


#typping speed test
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
