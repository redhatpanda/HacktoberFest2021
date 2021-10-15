import tkinter
import os
from gtts import gTTS
import playsound
from pygame import mixer

window = tkinter.Tk()
window.title("TEXT TO SPEECH")
window.config(padx=50, pady=50)


def destroy():
    window.destroy()


def reset():
    main_title_box.delete(0, "end")


def converter():
    message = main_title_box.get()
    word = gTTS(text=message)
    word.save("text.mp3")
    mixer.init()
    mixer.music.load("directories in which it exists/text.mp3")
    mixer.music.play()
    os.remove("directories in which it exists/text.mp3")


main_title = tkinter.Label(text="TEXT TO SPEECH", font=("Arial", 18))
main_title.grid(row=0, column=1, padx=20, pady=20)

main_title_box = tkinter.Entry(width=80)
main_title_box.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

reset_button = tkinter.Button(
    text="RESET", fg="black", width=20, bg="green", command=reset
)
reset_button.grid(row=2, column=0, pady=20)

Audio_button = tkinter.Button(
    text="Audio", fg="black", width=20, bg="yellow", command=converter
)
Audio_button.grid(row=2, column=1, pady=20)

Exit_button = tkinter.Button(
    text="EXIT", fg="black", width=20, bg="red", command=destroy
)
Exit_button.grid(row=2, column=2, pady=20)


window.mainloop()
