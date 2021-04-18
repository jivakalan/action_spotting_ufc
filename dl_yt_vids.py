# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:04:44 2020

@author: jkalan
"""


from pytube import YouTube
from datetime import datetime
import os,time

def downloading_video(link):
        now = datetime.now() # current date and time
        timeNow = now.strftime("%m-%d-%Y at %H_%M_%S")

        yt = YouTube(link)
        time.sleep(5)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        time.sleep(2)

        folderPath = os.path.join(os.getcwd(),timeNow)
        os.mkdir(folderPath)

        videoPath = os.path.join(os.getcwd(),timeNow,video.title)

        video.download(output_path = folderPath)

        return videoPath
#https://www.youtube.com/watch?v=e89XlkZrnYU
#https://www.youtube.com/watch?v=L3sR0-BJQPk
#https://www.youtube.com/watch?v=MQcXEWPesAw
#https://www.youtube.com/watch?v=HW1oG4xqzYc


for url in video_url:
    
    yt= YouTube(url).streams.first().download()
    time.sleep(5)

video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
time.sleep(2)


video_url =['https://www.youtube.com/watch?v=7pjEWc57anU'
,'https://www.youtube.com/watch?v=8dunuylUuts'
,'https://www.youtube.com/watch?v=lmOxyLJTBrM'
,'https://www.youtube.com/watch?v=OL_IcNrwWQ8','https://www.youtube.com/watch?v=JJB3cLkVHhE','https://www.youtube.com/watch?v=OxHD7I4bXKI','https://www.youtube.com/watch?v=2a0Ul8hRyqk']
