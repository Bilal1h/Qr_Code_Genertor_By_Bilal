
import qrcode as qr
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk, Image 
import time
import os
from tkinter.filedialog import asksaveasfilename


root = Tk()
root.geometry("415x350") 
root.resizable(False,False)
root.title("Qr - Code Generator")
root.wm_iconbitmap("Qr_code_icon.ico")



def qrcodes():
    global img
    qrval = qrent.get()
    qrvallen = len(qrval)
    
    img = qr.make(qrval)
    img.save("Qrcode.png")
    # img.show()
    if qrval != '' and qrvallen<29:
        # img = qr.make(qrval)
        # img.save("Qrcode.png")
        newwindow = Toplevel(root)
        newwindow.geometry("700x500") 
        newwindow.resizable(False,False)
        newwindow.wm_iconbitmap("Qr_code_icon.ico")
        # qrimg = Image.open("C:/Users/Home/Documents/Rock_Paper Scissors/Qrcode.png")
        # test = ImageTk.PhotoImage(qrimg)
        # test.pack()
        imgaddress = os.getcwd()
        # imgaddress = os.path('Qrcode.png')
        #img = PhotoImage(file='C:/Users/TALAL/Documents/Rock_Paper Scissors/Qrcode.png')
        img = PhotoImage(file=f'{imgaddress}/Qrcode.png')
        limg = Label(newwindow,image=img)
        limg.pack(expand=True)
        time.sleep(10)
    
       
        os.remove("C:/Users/Home/Documents/Rock_Paper Scissors/Qrcode.png")

        newwindow.mainloop()
    elif qrvallen>30 and qrval != '':
       
            
            newwindow1 = Toplevel(root)
            newwindow1.geometry("1000x700")
            
            newwindow1.wm_iconbitmap("Qr_code_icon.ico")
            # qrimg = Image.open("C:/Users/Home/Documents/Rock_Paper Scissors/Qrcode.png")
            # test = ImageTk.PhotoImage(qrimg)
            # test.pack()

            img = PhotoImage(file='C:/Users/Home/Documents/Rock_Paper Scissors/Qrcode.png')
            Label(newwindow1,image=img).pack(expand=True)
            newwindow1.mainloop()
    else:
        tmsg.showinfo("Error","Please Enter A Name or Link Of your QR Code")
    
    
Label(root,text="QR CODE GENRATOR",font="Roboto 30 bold",bg="gray",fg="white").pack(side=TOP,fill=X)
Label(root,text="Enter The Value OF your Targeted Qr Code : ",font="Roboto 15 bold").place(x=10,y=100)
qrent = Entry(root,font="Nexa 20 bold")
qrent.place(x=8,y=130)
qrbut = Button(root,text="Generate",font="Roboto 20 bold",command = qrcodes,borderwidth=10,relief=RAISED)
qrbut.place(x=130,y=180)
# img = qr.make("https://www.youtube.com")

# img.save("Qrcode.png")


# img.show()

root.mainloop()


    
    



