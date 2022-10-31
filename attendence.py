from tkinter import *
from tkinter import ttk
from turtle import update
import psycopg2 as db
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
import numpy as np


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("attendence Management system")
        self.conn = db.connect(user='postgres', password='Nikhil@123',
                               host='localhost', port="5432", database="Facebook")

         
        img = Image.open(r"D:\tkimages\sherry.jpg")
        img = img.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        img5 = Image.open(r"D:\tkimages\Vyom.jpg")
        img5 = img5.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl = Label(self.root, image=self.photoimg5)
        f_lbl.place(x=830, y=0, width=165, height=150)

        img6 = Image.open(r"D:\tkimages\Atul.jpg")
        img6 = img6.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        f_lbl = Label(self.root, image=self.photoimg6)
        f_lbl.place(x=500, y=0, width=165, height=150)

        img7 = Image.open(r"D:\tkimages\Akashy.jpg")
        img7 = img7.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        f_lbl = Label(self.root, image=self.photoimg7)
        f_lbl.place(x=660, y=0, width=165, height=150)

        img8 = Image.open(r"D:\tkimages\detection.jpg")
        img8 = img8.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        f_lbl = Label(self.root, image=self.photoimg8)
        f_lbl.place(x=1000, y=0, width=500, height=150)

        ##########################################################
        img1 = Image.open(r"D:\tkimages\detection.jpg")
        img1 = img1.resize((1500, 710), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(f_lbl1, text="ATTENDENCE MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(f_lbl1, bd=2, bg="white")
        main_frame.place(x=20, y=40, width=1480, height=600)

        left_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                text="stuedent details", font=("times new roman", 14, "bold"))
        left_frame.place(x=10, y=50, width=720, height=580)

        right_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                text="stuedent details", font=("times new roman", 14, "bold"))
        right_frame.place(x=750, y=50, width=720, height=580)

       
     
       

       

        

        

 


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
