#استدعاء المكتبات 

import pyqrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk



#تصميم الدوال للبرنامج


def GenerateQrcode():
    url=Url_Input.get()
    code=pyqrcode.create(url)
    filesave=filedialog.asksaveasfilename()
    code.png(filesave,scale=7)
    code.show()


#تصميم واجهة المستخدم


app=Tk()
app.title("Qrcode App") #عنوان الواجهة
app.geometry("700x500+250+150") #حجم النافذة
app.iconbitmap("qrcode_scan_icon_136286.ico") #تحديد ايقونة النافذة
app.config(background="white")
app.resizable(False,False) #أغلاق التحكم في عرض وطول النافذة


logo=ImageTk.PhotoImage(Image.open("qrcode_scan_icon_136286.png")) #انشاء صورة للتطبيق
logolab=Label(image=logo,bg="white")
logolab.place(x=300,y=30) #عرض الصورة داخل التطبيق 


lab=Label(text="Enter Url Here",fg="#111",bg="white",font=(16,16))
lab.place(x=301,y=250)


Url_Input=Entry(width=120,bd=12,justify='center')
Url_Input.place(x=0,y=325)


Generate_Button=Button(text="Generate Qrcode",bg="green",fg="white",font=(16,16),command=GenerateQrcode)
Generate_Button.place(x=295,y=405)

lab2=Label()
app.mainloop()#تشغيل البرنامج