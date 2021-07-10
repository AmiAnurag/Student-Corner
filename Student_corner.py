import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from shutil import copy2
import glob
import webbrowser
import pyautogui as pt
import pyperclip as pc
import time 
import random
from datetime import datetime
from plyer import notification

window=tk.Tk()
window.geometry("750x450")
window.title("Student Corner")

link_var=tk.StringVar()
title_var=tk.StringVar()
time_var=tk.StringVar()

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

#set your own path
def UploadAction(filepath_,frame,event=None):
    filepath='C:/Users/anurag nayek/Desktop/Student Corner/'+filepath_
    filename = filedialog.askopenfilename()
    copy2(filename,filepath)
    fontstyle=tkFont.Font(family="Helvetica",size=12)
    k=filename[filename.rfind('/')+1:]
    label=tk.Label(master=frame,text="Added : "+k,bg="#9a8feb",fg="#0d0359",width=500,font=fontstyle,wraplength=300,borderwidth=1, relief="solid")
    label.pack(pady=1)



def savelink(filepath_,frame):
    link=link_var.get()+'\n'
    file=open(filepath_+'.txt','a')
    file.write(link+"\n")
    file.close()
    link_var.set("")
    label=tk.Label(master=frame,text=link,bg="#6734eb",fg="#f7faf8",width=500,wraplength=300,borderwidth=1, relief="solid")   
    label.pack()



#defining functions
#document
def doc_screen():
    try:
        window2.destroy()
    except:
        window2=tk.Toplevel() 
        window2.geometry("400x500")
        window2.grab_set()
        fr=tk.Frame(master=window2)
        fontstyle=tkFont.Font(size=20,weight="bold")
        lbl=tk.Label(master=fr,text="Your all important \ndocuments \nare kept secured here",bg="#effa16",font=fontstyle)
        lbl.pack()
        frame_doc=tk.Frame(master=window2)
        button = tk.Button(master=fr, text='Upload More Documents', command=lambda:UploadAction('document',frame_doc))
        button.pack(pady=10)
        l=(glob.glob('C:/Users/anurag nayek/Desktop/Student Corner/document/*'))
        a=[]
        z=0
        fontstyle=tkFont.Font(family="Helvetica",size=12)

        for i in l:
            for j in i:
                if j=="\\":
                    a.append(i[(i.index(j)+1):])

        for k in a:
            if z==0:
                p="#fcb3ca"
            else:
                p="#b3e4fc"
            label=tk.Label(master=frame_doc,text=k,bg=p,width=500,font=fontstyle,wraplength=300)
            label.pack()
            if z==0:
                z=1
            else:
                z=0
        fr.pack()
        frame_doc.pack()
#image files

def img_screen():
    try:
        window2.destroy()
    except:
        window2=tk.Toplevel() 
        window2.geometry("400x500")
        window2.grab_set()
        fr=tk.Frame(master=window2)
        fontstyle=tkFont.Font(size=20,weight="bold")
        lbl=tk.Label(master=fr,text="Your all important \nImages \nare kept secured here",bg="#effa16",font=fontstyle)
        lbl.pack()
        frame_doc=tk.Frame(master=window2)
        button = tk.Button(master=fr, text='Upload More Documents', command=lambda:UploadAction('image',frame_doc))
        button.pack(pady=10)

        l=(glob.glob('C:/Users/anurag nayek/Desktop/Student Corner/image/*'))
        a=[]
        z=0
        fontstyle=tkFont.Font(family="Helvetica",size=12)

        for i in l:
            for j in i:
                if j=="\\":
                    a.append(i[(i.index(j)+1):])

        for k in a:
            if z==0:
                p="#fcb3ca"
            else:
                p="#b3e4fc"
            label=tk.Label(master=frame_doc,text=k,bg=p,width=500,font=fontstyle,wraplength=300)
            label.pack()
            if z==0:
                z=1
            else:
                z=0

        fr.pack()
        frame_doc.pack()

#defining function for certificates
def cert_screen():
    try:
        window2.destroy()
    except:
        window2=tk.Toplevel() 
        window2.geometry("400x500")
        window2.grab_set()
        fr=tk.Frame(master=window2)
        fontstyle=tkFont.Font(size=20,weight="bold")
        lbl=tk.Label(master=fr,text="Your all Certificates \nare kept secured here",bg="#effa16",font=fontstyle)
        lbl.pack()
        frame_doc=tk.Frame(master=window2)#frame for the below document display
        button = tk.Button(master=fr, text='Upload More Documents', command=lambda:UploadAction('cert',frame_doc))
        button.pack(pady=10)

        l=(glob.glob('C:/Users/anurag nayek/Desktop/Student Corner/cert/*'))
        a=[]
        z=0
        fontstyle=tkFont.Font(family="Helvetica",size=12)

        for i in l:
            for j in i:
                if j=="\\":
                    a.append(i[(i.index(j)+1):])

        for k in a:
            if z==0:
                p="#fcb3ca"
            else:
                p="#b3e4fc"
            label=tk.Label(master=frame_doc,text=k,bg=p,width=500,font=fontstyle,wraplength=300)
            label.pack()
            if z==0:
                z=1
            else:
                z=0

        fr.pack()
        frame_doc.pack()

#important links
def implink_screen():
    window2=tk.Toplevel() 
    window2.geometry("400x500")
    window2.grab_set()
    fr=tk.Frame(master=window2)
    fontstyle=tkFont.Font(size=20,weight="bold")
    lbl=tk.Label(master=fr,text="Here are your links",bg="#effa16",font=fontstyle,width=700)
    lbl.pack()
    fr.pack()
    #frame of the content
    frame_content=tk.Frame(master=window2)

    frame=tk.Frame(master=window2,bg="#ed9c21")
    fontstyle=tkFont.Font(size=15)
    label1=tk.Label(master=frame,text="Enter links here to save it for future",bg="#ed9c21",font=fontstyle)
    ent=tk.Entry(master=frame,textvariable=link_var,width=50)
    btn=tk.Button(master=frame,text="Save",command=lambda:savelink('implink',frame_content))
    label1.grid(row=0,column=0,pady=10)
    ent.grid(row=1,column=0,pady=10)
    btn.grid(row=1,column=2,pady=10,padx=3)
    frame.pack(pady=20)

    file=open("implink.txt",'r')
    p=(file.readlines())
    for i in p:
        if '\n' in i:
            p[p.index(i)]=i[:-1]

    file.close()
    z=0
    for k in p:
            if z==0:
                c="#fcb3ca"
            else:
                c="#b3e4fc"
            label=tk.Label(master=frame_content,text=k,bg=c,width=500,wraplength=300)
            label.bind("<Button-1>",callback)
            label.pack()
            if z==0:
                z=1
            else:
                z=0
    frame_content.pack()

#ranfom art -- set the location of mspaint.exe as on your computer
def randon_art():
    position=pt.locateOnScreen("voiceart/Capture.PNG",confidence=0.6)
    x=position[0]
    y=position[1]
    time.sleep(1)
    pt.moveTo(x+10,y+5)
    pt.click()
    pc.copy("C:\WINDOWS\system32\mspaint.exe")
    pt.hotkey('ctrl','v')
    time.sleep(1)
    pt.press('enter')
    time.sleep(1)
    pt.moveTo(600,400)
    time.sleep(5)
    lines_of_art=random.randrange(50,60)
    while(lines_of_art):
        pixel_x=random.randrange(-30,30,5)
        pixel_y=random.randrange(-30,30,5)
        if pixel_x==0:
            pixel_x=5
        if pixel_y==0:
            pixel_y=5
        pt.drag(pixel_x, 0, 0.2, button='left')
        pt.drag(0, pixel_y, 0.2, button='left')

        lines_of_art=lines_of_art-1

#notification
def notify_window():
    try:
        window2.destroy()
    except:
        window2=tk.Toplevel() 
        window2.geometry("400x150")
        window2.grab_set()
        fr=tk.Frame(master=window2)
        fontstyle=tkFont.Font(size=15)
        label=tk.Label(master=fr,text="Add Meeting Reminder",font=fontstyle,bg="#bb1bf5",width=400)
        label.pack()
        frame=tk.Frame(master=window2)
        label2=tk.Label(master=frame,text="Add title")
        ent1=tk.Entry(master=frame,textvariable=title_var,width=50)
        label3=tk.Label(master=frame,text="Add time")
        ent2=tk.Entry(master=frame,textvariable=time_var,width=50)
        btn=tk.Button(master=frame,text="Set Alarm",width=10,height=2,command=set_alarm)
        label2.grid(row=0,column=0)
        ent1.grid(row=0,column=1)
        label3.grid(row=1,column=0)
        ent2.grid(row=1,column=1)
        btn.grid(row=2,column=1)
        fr.pack()
        frame.pack()
        window2.configure(bg="#bb1bf5")

def set_alarm():
    hour=time_var.get()[:2]
    minute=time_var.get()[3:5]
    try:
     if int(hour)>=0 and int(hour)<24 and int(minute)>=0 and int(minute)<=60:

        position=pt.locateOnScreen("voiceart/Capture.PNG",confidence=0.6)
        x=position[0]
        y=position[1]
        pt.moveTo(x+10,y+5)
        pt.click()
        pc.copy("alarms & Clock")
        pt.hotkey('ctrl','v')
        time.sleep(1)
        pt.press('enter')
        time.sleep(5)
        pos=pt.locateOnScreen("alarm_meeting/alarm.PNG",confidence=0.6)
        pt.moveTo(pos[0]+10,pos[1]+10)
        pt.click()
        
        time.sleep(0.5)
        pt.write(hour)
        pt.press('tab')
        pt.write(minute)
        pt.press('tab')
        pt.write(title_var.get(),interval=0.01)
        for i in range(5):
            pt.press('tab')
            time.sleep(0.2)
        pt.press('enter')
     else:
        notification.notify(
                title = "Wrong Time",     # title of message
                message = "Correct the time", # message body
                app_icon = "",     # ico path with .ico file
                timeout = 5        # time for notification to stay on screen
            )
    except Exception as e:
                notification.notify(
                title = "Wrong Time",     # title of message
                message = "Correct the time", # message body
                app_icon = "",     # ico path with .ico file
                timeout = 5        # time for notification to stay on screen
            )
                print(e)


#main screen
frame=tk.Frame(master=window,width=100,height=100)
fontstyle=tkFont.Font(size=20,weight="bold")
label=tk.Label(master=frame,text="Student Corner",bg="#effa16",width=400,font=fontstyle)
label.pack()
frame.pack()
#frame for all buttons
button_frame=tk.Frame(master=window,bg="#6dbd83")
btn1=tk.Button(master=button_frame,text="Your Documents",bg="#167dfa",fg="#faf5f5",width=18,height=7,command=doc_screen)
btn2=tk.Button(master=button_frame,text="Your Images",bg="#167dfa",fg="#faf5f5",width=18,height=7,command=img_screen)
btn3=tk.Button(master=button_frame,text="Your Certificates",bg="#167dfa",fg="#faf5f5",width=18,height=7,command=cert_screen)
btn4=tk.Button(master=button_frame,text="Mr Designer",bg="#167dfa",fg="#faf5f5",width=18,height=7,command=randon_art)
btn5=tk.Button(master=button_frame,text="Important Links",bg="#167dfa",fg="#faf5f5",width=18,height=7,command=implink_screen)
btn6=tk.Button(master=button_frame,text="Add Meeting reminder",bg="#167dfa",fg="#faf5f5",width=18,height=7,command=notify_window)
#btn1.pack(side=tk.LEFT)
btn1.grid(row=0,column=0,padx=30,pady=30)
btn2.grid(row=0,column=1,padx=30,pady=30)
btn3.grid(row=0,column=2,padx=30,pady=30)
btn4.grid(row=1,column=0,padx=30,pady=30)
btn5.grid(row=1,column=1,padx=30,pady=30)
btn6.grid(row=1,column=2,padx=30,pady=30)
button_frame.pack(pady=15)

#meeting reminder
meet_rem_frame=tk.Frame(master=window)
fontstyle1=tkFont.Font(size=15,slant="italic")
label_rem=tk.Label(master=window,text="Updates coming soon",bg="#c755ed",fg="#09014a",font=fontstyle1,width=700)
label_rem.pack()
meet_rem_frame.pack()

window.resizable(False, False) 
window.mainloop()

