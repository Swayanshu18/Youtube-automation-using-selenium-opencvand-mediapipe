
import cv2
import mediapipe as mp
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import os
import wget
import time
from time import sleep
import os
import wget
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.youtube.com/shorts/Z5L1a9EPlHA')
address = driver.find_element(By.ID, 'center').click()
click = driver.find_element(By.ID, 'shorts-player').click()


cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
fingerCoordinates=[(8,6),(12,10),(16,14),(20,18)]
thumbCoordinates=(4,2)
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    multilandmarks=results.multi_hand_landmarks
    #print(multilandmarks)
    if multilandmarks:
        handPoints=[]

        for handLms in multilandmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            for idx,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(idx,cx,cy)
                handPoints.append((cx,cy))
                #print(idx,lm)
        for point in handPoints:
            #print(point)
            cv2.circle(img,point,10,(0,0,255),cv2.FILLED)
        upCount=0
        for coordinate in fingerCoordinates:
            (8,6)
            if handPoints[coordinate[0]][1]<handPoints[coordinate[1]][1]:

                upCount+=1
        cv2.putText(img,str(upCount),(150,100),cv2.FONT_HERSHEY_PLAIN,12,(255,0,0),12)





        if upCount == 3:
            clickk = driver.find_element(By.XPATH,
                                         '//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()

    cv2.imshow("Finger Counter",img)

    cv2.waitKey(5)
