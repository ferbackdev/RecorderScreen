import cv2
import keyboard
import numpy as np
import pyautogui

fps = 30
screen_size = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("record.avi", codec, fps, screen_size)

while True:
    frame = pyautogui.screenshot()
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    video.write(frame)
    if keyboard.is_pressed("q") or keyboard.is_pressed("Q") or keyboard.is_pressed("esc"):
        break
    
video.release()
cv2.destroyAllWindows()
    