import os # 경로를 이동하기 위해 os 라이브러리를 불러옴.
from gtts import gTTS 
from playsound import playsound #playsound 모듈로 부터 playsound를 불러와 사용

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동, playsound에서 한글을 인식하지 못하기 때문
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

text = "안녕하세요. 파이썬과 40개의 작품들입니다."

tts = gTTS(text = text, lang='ko')
tts.save("hi.mp3")

playsound('hi.mp3') # hi.mp3 파일 재생