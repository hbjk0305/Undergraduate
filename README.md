# Undergraduate

현재 재생 오류가 있음.

## 실험 설명
본 실험에서는 음질의 차이에 따른 감정의 전달능력을 알아보고자 합니다.
실험은 크게 예행연습과 본 실험으로 구성되어 있습니다.
먼저 Loading 시간 후에 아래와 같은 창이 뜬다. (Loading 시간이 생각보다 길다)

### step0. 준비물
유선 이어폰을 필수로 착용해주세요!!!!!
python 3.6 이상을 사용해주세요.

### step1. 실험설명
<img width="512" alt="스크린샷 2022-05-02 오후 5 02 18" src="https://user-images.githubusercontent.com/20623289/166203308-682ee776-1787-4558-9ae5-77d586b3be95.png">
- 닉네임은 결과파일의 이름으로 사용되기 때문에 원하는 이름을 사용하면 된다.
- 나이는 만 나이로 숫자만 적어주세요.
- 성별 체크 후 "다음"을 눌러주세요.

<img width="512" alt="스크린샷 2022-05-02 오후 5 03 52" src="https://user-images.githubusercontent.com/20623289/166203454-64605960-34a1-4f17-a087-85c6169ff8e0.png">
- 위 그림과 같이 실험에 대한 설명이 적혀 있습니다.
- 숙지하신 후 "시작"을 눌러주세요.

<img width="512" alt="스크린샷 2022-05-02 오후 5 05 18" src="https://user-images.githubusercontent.com/20623289/166203596-6cba0228-8dea-495b-9e51-e10df9109ccb.png">
- 위 그림에서 각 감정에 해당하는 음성을 들어볼 수 있습니다.
- 들어보면서 볼륨을 조절해주세요.
- 다 들으신 후에 "다음"을 눌러주세요.

### step2. 예행연습
<img width="512" alt="스크린샷 2022-05-02 오후 5 06 46" src="https://user-images.githubusercontent.com/20623289/166203772-ce2ce5e3-19f7-4eb3-8b09-c3ba582285c1.png">
- 음성은 최대 두번까지 재생할 수 있습니다.
- 본 실험에 앞서서 예행연습을 수행할 예정입니다.

<img width="512" alt="스크린샷 2022-05-02 오후 5 08 36" src="https://user-images.githubusercontent.com/20623289/166204004-8c68e09c-8bd8-41af-a0dc-bc05dc64aa92.png">
- 위 그림은 예행연습 창입니다. 
- 맨 위에 `(현재 실험 번호) / (전체 실험의 개수)`가 표시됩니다.
- 그 아래에 음성의 대사가 주어집니다.
- 오른쪽 상자 안의 "Play"버튼을 누르면 음성이 재생됩니다. 음성은 최대 두번까지 재생할 수 있습니다.
- 왼쪽 박스에서 가장 가깝게 느껴지는 감정을 선택한 후, 아래의 "Next"버튼을 눌러주세요.
- 총 세 번의 예행연습 후 본실험이 시작됩니다.

### step3. 본실험
본 실험 창은 예행연습 창과 동일하게 구성되어 있으며, 총 56개의 음성을 듣고 느껴지는 감정을 평가하게 됩니다.

### step4. 실험 종료
실험 종료 후 result 폴더 안의 (닉네임).csv를 보내주세요.


## 프로그램 실행 방법


```
git clone https://github.com/hbjk0305/Undergraduate.git
cd Undergraduate
```
먼저 samples.zip의 압축을 풀어주세요. 폴더명은 samples로 유지해주세요.
```
pip install sounddevice librosa
python3 App.py
```


