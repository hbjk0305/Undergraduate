import tkinter as tk
from tkinter import *
import sounddevice as sd
from scipy import io as sio
import scipy.io.wavfile
import time

class Info(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.exp = Label(self)
        self.exp.pack(padx=5, pady=5)
        self.script = Label(self)
        self.script.pack(padx=5)

    def set_info(self, script, cur, total):
        self.exp.config(text="{} / {}".format(cur, total))
        self.script.config(text="\"{}\"".format(script), font=("Consolas", 18))


class Select(tk.Frame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text = "")
        self.emotions = ["Happiness", "Surprise", "Neutral", "Fear", "Disgust", "Anger", "Sadness"]
        self.r = IntVar()
        self.radios = []
        for idx, label in enumerate(self.emotions):
            self.radios.append(Radiobutton(self, text=label, variable=self.r, value=idx, command=self.select))
            self.radios[-1].pack(anchor=W, padx=5, pady=5)
            self.radios[-1]["font"] = ("Consolas", 15)


    def select(self):
        self.answer = self.emotions[self.r.get()]



class Page(tk.Frame):
    def __init__(self, master, script, cur, total, sr, data):
        tk.Frame.__init__(self, master)


        self.info = Info(self)
        self.info.set_info(script, cur, total)
        self.info.pack(side=TOP, padx=10, pady=10)

        self.select = Select(self)
        self.select.pack(side=LEFT, padx=25, pady=5)

        self.play = Player(self)
        self.play.set_audio(sr, data)
        self.play.pack(side=RIGHT, padx=25, pady=5)

        self.button = Button(self, text="Next", command=self.answer, activebackground="orange", state = DISABLED)
        self.button.pack(side=BOTTOM)

    def answer(self):
        self.duration = time.time() - self.play.start_time
        self.ans = self.select.answer


class Player(tk.Frame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text="")
        self.played = 2
        self.button = Button(self, text= "Play", command = self.play, activebackground="orange")
        self.button.pack(padx = 10, pady = 10)
        self.a = Label(self)
        self.a.pack(padx = 5, pady = 5)
        self.a.config(text="재생 기회가 {}회 남았습니다.".format(self.played))

    def play(self):
        self.master.button["state"] = tk.NORMAL
        if self.played ==2:
            self.start_time = time.time()
        sd.play(self.data, self.sr)
        self.played -= 1
        self.a.config(text="재생 기회가 {}회 남았습니다.".format(self.played))
        if self.played == 0:
            self.button["state"]=tk.DISABLED

    def set_audio(self, sr, data):
        self.sr, self.data = sr, data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wave_name = "./samples/036-005.wav"
    script = "나 먼저 갈게"
    sr, data = sio.wavfile.read(wave_name)

    top = Tk()
    top.geometry("400x400")
    page = Page(top, script, 1, 2, sr, data)
    page.pack()

    top.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
