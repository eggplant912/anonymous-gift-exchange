#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 23:40:28 2022

@author: lichu
"""

import random

A="sunny.lo770@gmail.com"
B="ylc092012@gmail.com"
C="jasmine2256216@gmail.com"
D="jslinda.good@gmail.com"
E="B109143109@nkust.edu.tw"
list1 = [A,B,C,D]
random.shuffle(list1)
S= "Sunny"
Y= "Beryl"
J= "Jasmine"
L= "Linda"
list2 = [S,Y,J,L]

#list3 = [B, E]
#list4 = [1, 2]
dict1 = dict(zip(list1, list2))

import sys
sys.setrecursionlimit(7000)
import email.message
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("ylc092012@gmail.com", "brvyyarrpycfelkl")
for key in dict1:
    msg = email.message.EmailMessage()
    msg["From"] = "ylc092012@gmail.com"
    msg["To"] = key
    msg["Subject"] = "Test3"
    msg.set_content(str(dict1[key]))
    server.send_message(msg)
server.close()

