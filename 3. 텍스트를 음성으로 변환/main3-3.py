from gtts import gTTS 
from playsound import playsound
import os

# 경로를 .py파일을 실행경로로 이동, 현재경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의텍스트.txt' 
with open(file_path, 'rt', encoding = 'UTF8') as f : 
    
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')

tts.save("myText.mp3")

playsound("myText.mp3")


# 나의텍스트.txt 경로를 바인딩
# 파일은 f이름으로 오픈, 
# 한글로 작성된 파일을 열기 때문에 'rt', encoding='UTF8'형식으로 열어 글자가 깨지지 않게 한다.

# 파일의 전체 내용으르 읽어 read_file 변수에 바인딩
    # with는 파일을 열고 종료되면 자동으로 파일을 닫는다.
    # 파일을 열 때 with를 사용하면 코드가 간결해짐