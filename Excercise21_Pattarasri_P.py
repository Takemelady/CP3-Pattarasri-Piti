from tkinter import *
import math

def leftClickButton(event):
    bmiResult = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if bmiResult <= 18.5:
        a = "ผอมเกิน"
    elif bmiResult <= 22.9:
        a = "ปกติ"
    elif bmiResult <= 24.9:
        a = "น้ำหนักเกิน"
    elif bmiResult <= 29.9:
        a = "อ้วน"
    elif bmiResult >= 30:
        a = "อ้วนเกินไป"
    labelResult.configure(text="ค่า BMI ของคุณคือ :" + str(bmiResult) + "  ผลการประเมินคือ : "+ a)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()