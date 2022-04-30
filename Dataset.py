import glob
import librosa
import random

random.seed(42)

class Dataset:
    def __init__(self, data_csv, srs):
        print("Loading", data_csv)
        self.data = []
        import csv
        f = open(data_csv, 'r', encoding='utf-8')
        for i, line in enumerate(csv.reader(f)):
            if i==0:
                continue
            y, sr = librosa.load("./samples/"+line[0], sr=48000)
            self.data.append([line[0], 48000, line[2], line[3], y])
            for sr in srs:
                y_ = librosa.resample(y, orig_sr=48000, target_sr=sr)
                self.data.append([line[0], sr, line[2], line[3], y_])
                # filename, sr, label, script, data
        f.close()
        random.shuffle(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

if __name__=="__main__":
    for i in Dataset("data.csv", srs=[16000]):
        print(i)
