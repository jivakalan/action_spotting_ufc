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



for url in video_url:
    
    yt= YouTube(url).streams.first().download()
    time.sleep(5)

video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
time.sleep(2)

video_url =['https://www.youtube.com/watch?v=kB4jgaYYBlI','https://www.youtube.com/watch?v=Ro_zceOYrb0']
    
    
    'https://www.youtube.com/watch?v=U-fhb1RnRzM']

video_url =['https://www.youtube.com/watch?v=knRMfWDjKZE','https://www.youtube.com/watch?v=RK9Wry-DHew','https://www.youtube.com/watch?v=L3sR0-BJQPk&t=1s','https://www.youtube.com/watch?v=y5tmDY9-BAU']



