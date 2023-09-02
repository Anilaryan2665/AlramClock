from tkinter import *
from tkinter import messagebox as msgbx
import datetime as dt
import time
import winsound as ws
import os


def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %Y")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            ws.PlaySound("ringtones/beep.wav", ws.SND_ASYNC)
            msgbx.showinfo("Alert","It is time to wake up")
            break


def getAlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)


guiWindow = Tk()
guiWindow.title("Alarm Clock")
guiWindow.geometry("600x350")
guiWindow.config(bg="#d8dbe2")
guiWindow.resizable(width=False, height=False)


add_time = Label(
    guiWindow, text="Hour  :  Minute  :  Second", font=("Times",16,"bold"), fg="black",bg="white"
).place(x=180, y=100)

add_title=Label(
    guiWindow,text="ALARM CLOCK",font=("Times",20,"bold"),bg="#66FFCC",fg="black"
).place_configure(x=200,y=20)


setAlarm = Label(
    guiWindow,
    text="Set Time: ",
    fg="black",
    bg="#CCCC64",
    width=9,
    font=("Times", 13, "bold"),
).place(x=50, y=150)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow, textvariable=hour, fg="white", bg="#778da9", width=4, font=(20)
).place(x=180, y=150)
minuteTime = Entry(
    guiWindow, textvariable=minute, fg="white", bg="#778da9", width=4, font=(20)
).place(x=260, y=150)
secondTime = Entry(
    guiWindow, textvariable=second, fg="white", bg="#778da9", width=4, font=(20)
).place(x=350, y=150)

submit = Button(
    guiWindow,
    text="Set Alarm",
    fg="black",
    font=("Times",14,"bold"),
    bg="#0099CC",
    width=14,
    command=getAlarmTime,
).place(x=180, y=220)

guiWindow.mainloop()
