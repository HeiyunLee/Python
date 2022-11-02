import pyautogui
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 경로를 현재 .py파일을 실행하는 경로로 이동.
# pyautogui에서 한글을 인식하지 못해 경로를 이동하였다.

picPosition = pyautogui.locateOnScreen('pic1.png')
print(picPosition) 
# pic1.png 파일과 동일한 그림을 찾아 좌표를 출력

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png')
    print(picPosition) 
    # 앞의 사진에서 좌표를 찾지 못하였다면 pic2.png 파일과 동일한 그림을 찾아 좌표를 출력

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png')
    print(picPosition)
    # 앞의 사진에서 좌표를 찾지 못하였다면 pic3.png 파일과 동일한 그림을 찾아 좌표를 출력
