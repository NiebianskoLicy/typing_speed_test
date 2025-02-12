from tkinter import *
import json

window = Tk()
window.title("Typing Speed Test")
window.geometry("720x450")

font = ("Arial", 14)
timer = 60

# getting text for program
with open("words.json", "r") as f:
     text = json.load(f)["text"]

# function which start countdown and show WPS
def start_timer():
    global timer, wps_text
    #disable button for multi clicking it
    start_button.config(state=DISABLED)
    word_per_sec = round((word_count() / (timer/60)), 2)

    wps_text.config(text=f"WPS:\n {word_per_sec}", font=("Arial", 14))
    wps_text.after(1000, word_count)
    wps_text.place(x=605, y=200)

    user_text.config(state=NORMAL)
    # start timer
    st_tim = countdown_text.after(1000,start_timer,)
    timer -= 1

    countdown_text.config(text=f"Countdown:\n{timer}")

    # on 0 sec program ends
    if timer == 0:
        user_text.config(state=DISABLED)

        wps_text.config(text=f"Time's up!\n\nWPS: {word_per_sec}\nWPM: {round(word_count(), 2)}")
        wps_text.place(
            x=590,
            y=190, )
        countdown_text.after_cancel(st_tim)
        # after reaching 0 time, user can restart again
        timer = 60
        start_button.config(text="Restart", command=start_timer, state=NORMAL)

# a function which count words written
def word_count():
    count_word = 0
    count_text = user_text.get("1.0", END)
    word = ""
    for letter in count_text:
        word += letter
        if letter == " ":
            word = ""
            if word in text:
                count_word += 1
                return count_word
    return count_word

# outer variable allow to not overwrite labels
wps_text = Label(window)


#typping speed test
typ_sp_text = Text(window, height=8, width=50, font=font, wrap=WORD)
typ_sp_text.insert(END, text)
typ_sp_text.place(x=10, y=10)
typ_sp_text.config(state=DISABLED)

# window for user text
user_text = Text(window, height=8, width=50, font=font)
user_text.place(x=10, y=220)
user_text.config(state=DISABLED)

# start button
start_button = Button(window, text="Start", command=start_timer)
start_button.config(font=("Arial", 14),width=5)
start_button.place(x=580, y=361)

# coundown label
countdown_text = Label(
    window,
    text="Countdown:\n60",
    font=("Arial", 14),
)
countdown_text.config()
countdown_text.place(x=580, y=50)

window.mainloop()
