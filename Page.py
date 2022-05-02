import tkinter as tk
from tkinter import *
import sounddevice as sd
import librosa
import time
from functools import partial

class Info(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.exp = Label(self)
        self.exp.pack(padx=5, pady=5)
        self.script = Label(self)
        self.script.pack(padx=5)

    def set_info(self, script, cur, total):
        self.exp.config(text="{} / {}".format(cur, total), bg='#fff', fg='#f00')
        self.script.config(text="\"{}\"".format(script), font=("Consolas", 18))


class Select(tk.Frame):
    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text = "")
        self.emotions = ["Happiness", "Surprise", "Neutral", "Fear", "Disgust", "Anger", "Sadness"]
        self.r = IntVar()
        self.answer = self.emotions[self.r.get()]
        self.radios = []
        for idx, label in enumerate(self.emotions):
            self.radios.append(Radiobutton(self, text=label, variable=self.r, value=idx, command=self.select))
            self.radios[-1].pack(anchor=W, padx=5, pady=5)
            self.radios[-1]["font"] = ("Consolas", 15)


    def select(self):
        self.answer = self.emotions[self.r.get()]



class Page(tk.Frame):
    def __init__(self, master, cur, total, data):
        tk.Frame.__init__(self, master)
        self.filename, self.sr, self.label, self.script, self.y = data[0], data[1], data[2], data[3], data[4]
        self.button = Button(self, text="Next", command=self.answer, activebackground="orange", state = DISABLED)
        self.button.pack(side=BOTTOM)

        self.info = Info(self)
        self.info.set_info(self.script, cur, total)
        self.info.pack(side=TOP, padx=10, pady=10)

        self.select = Select(self)
        self.select.pack(side=LEFT, padx=25, pady=5)

        self.play = Player(self)
        self.play.set_audio(self.sr, self.y)
        self.play.pack(side=RIGHT, padx=25, pady=5)



    def answer(self):
        self.duration = time.time() - self.play.start_time
        self.ans = self.select.answer
        self.master.save_answer()
        self.master.switch_frame()


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


class StartPage(tk.Frame):
    def __init__(self, master):
        self.user, self.age, self.gender = tk.StringVar(), tk.StringVar(), tk.StringVar()
        tk.Frame.__init__(self, master)
        tk.Label(self, text="닉네임 : ").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="나이(만) : ").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.user).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=1, column=1, padx=10, pady=10)
        tk.Radiobutton(self, text="남자", variable=self.gender, value="M").grid(row=2, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text="여자", variable=self.gender, value="F").grid(row=2, column=1, padx=5, pady=5)
        self.gender.set('M')
        tk.Button(self, text="다음", command=self.register).grid(row=3, column=1, padx=10, pady=10)

    def register(self):
        self.master.user = self.user.get()
        self.master.age = int(self.age.get())
        self.master.gender = self.gender.get()
        self.master.switch_frame()

class EndPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="실험에 참가해주셔서 감사합니다.").grid(row=0, column=0, padx=10, pady=20)
        tk.Button(self, text="종료", command=self.quit).grid(row=2, column=0, padx=10, pady=20)

class InfoPage(tk.Frame):
    def __init__(self, master, info):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=info, wraplength = 360).grid(row=0, column=0, padx=10, pady=20)
        tk.Button(self, text="시작", command=self.master.switch_frame).grid(row=2, column=0, padx=10, pady=20)

class ExamplePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.emotions = ["Happiness", "Surprise", "Neutral" , "Fear", "Disgust", "Anger", "Sadness"]
        self.wavs = []
        for e in self.emotions:
            y, sr = librosa.load("./samples/{}.wav".format(e), sr=48000)
            self.wavs.append((y, sr))
        self.radios = []
        for idx, label in enumerate(self.emotions):
            Button(self, text=label, command=partial(sd.play, self.wavs[idx][0], self.wavs[idx][1])).grid(row=idx, padx=10, pady=10)

        tk.Button(self, text="다음", command=self.master.switch_frame).grid(row=9, column=0, padx=10, pady=20)

if __name__ == '__main__':
    from scipy import io as sio
    import scipy.io.wavfile
    wave_name = "./samples/036-005.wav"
    script = "나 먼저 갈게"
    sr, data = sio.wavfile.read(wave_name)

    top = Tk()
    top.geometry("400x400")
    page = Page(top, script, 1, 2, sr, data)
    page.pack()

    top.mainloop()
