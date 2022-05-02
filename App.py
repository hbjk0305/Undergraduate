import os
from Page import Page, StartPage, EndPage, InfoPage, ExamplePage
from Dataset import Dataset
import tkinter as tk
import csv

class ExpApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.dataset = Dataset("data.csv", srs=[8000, 16000, 32000])
        self.sample_dataset = Dataset("sample.csv", srs=[])
        self.total = len(self.dataset)
        self.answers = []
        self.frame_id = 0
        info0="""
본 실험은 음질의 차이에 따른 감정의 전달률을 알아보기 위한 실험입니다.
실험에서 사용하는 감정의 종류는 총 7가지로, 아래와 같습니다.

감정 : Happiness, Surprise, Neutral, Fear, Disgust, Anger, Sadness

아래의 "시작"버튼을 누르면 각 감정들에 해당하는 음성의 예시를 들어볼 수 있습니다."""
        info1 = """
본 실험에 앞서서 먼저 {}번의 예행연습을 진행하겠습니다.
        
Play 버튼을 눌렀을 때 들리는 음성을 듣고, 총 7가지 감정 중 가장 가깝게 느껴지는 감정을 선택해주세요.
음성은 최대 2번까지 재생할 수 있습니다.

아래의 "시작"버튼을 누르면 예행연습이 시작됩니다.
        """.format(len(self.sample_dataset))
        self.frames = [StartPage(self), InfoPage(self, info0), ExamplePage(self), InfoPage(self, info1)]
        sample_pages = [Page(self, "연습 {}".format(idx + 1), len(self.sample_dataset), data)
                 for idx, data in enumerate(self.sample_dataset)]
        self.frames.extend(sample_pages)
        info2 = """
        이제부터 본 실험을 시작하겠습니다.
        
        본 실험은 총 {}개의 음성으로 구성되어 있습니다.
        실험 시간은 약 10분입니다.
        모든 데이터는 실험 이외의 목적으로 사용되지 않습니다.
        
        아래의 "시작"버튼을 누르면 본 실험이 시작됩니다.
        """.format(self.total)
        self.frames.append(InfoPage(self, info2))
        pages = [Page(self, "{}".format(idx + 1), len(self.dataset), data)
                 for idx, data in enumerate(self.dataset)]
        self.frames.extend(pages)
        self.frame = self.frames[self.frame_id]
        self.frame.pack(padx = 50, pady = 50)
        self.centerWindow()

    def end(self):
        fields = ["User", "Gender", "Age", "filename", "sr", "answer", "duration", "label", "script"]
        os.makedirs("./result", exist_ok=True)
        with open('./result/{}.csv'.format(self.user), 'w', encoding='utf-8', newline='') as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(self.answers)

    def save_answer(self):
        self.answers.append((self.user, self.gender, self.age, self.frame.filename, self.frame.sr, self.frame.ans, self.frame.duration, self.frame.label, self.frame.script))

    def switch_frame(self):
        self.frame_id += 1
        if self.frame_id == len(self.frames):
            self.end()
            new_frame = EndPage(self)
        else:
            new_frame = self.frames[self.frame_id]
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

    def centerWindow(self):
        w, h = 400, 400
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (sw-w)/2, (sh-h)/2
        self.geometry("%dx%d+%d+%d"%(w, h, x, y))



if __name__ =="__main__":
    app = ExpApp()
    app.title("Test Session")

    app.mainloop()
