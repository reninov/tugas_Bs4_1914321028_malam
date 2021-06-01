# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:44:40 2021

@author: LENOVO
"""

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.wavsource.com/snds_2020-10-01_3728627494378403/people/women/computer_mail_new.wav'])