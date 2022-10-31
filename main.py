from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from student import Student
import os
from Train import Train
from facedetection import Face_Detection


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")
################################################
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

        img1 = Image.open(r"D:\tkimages\detection.jpg")
        img1 = img1.resize((1500, 710), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=150, width=1530, height=710)

        img2 = Image.open(r"D:\tkimages\detection.jpg")
        img2 = img2.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=150)
#################################################################################################
        title_lbl = Label(f_lbl1, text="FACE RECONIGATION ATTENCE SYSTEM  SOFTWARE", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
##########################################################
        img3 = Image.open(r"D:\tkimages\book.png")
        img3 = img3.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(f_lbl1, image=self.photoimg3,
                    command=self.student_details, cursor="hand2")
        b2.place(x=200, y=100, width=220, height=220)

        b1 = Button(f_lbl1, text="STUDENT DETAILS", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=200, y=300, width=220, height=40)

        img4 = Image.open(r"D:\tkimages\Akash.png")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2 = Button(f_lbl1, image=self.photoimg4, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        b1 = Button(f_lbl1, text="FACE DETECTION", command=self.face_detect_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=500, y=300, width=220, height=40)

        img8 = Image.open(r"D:\tkimages\attence.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Button(f_lbl1, image=self.photoimg8, cursor="hand2")
        b2.place(x=800, y=100, width=220, height=220)

        b1 = Button(f_lbl1, text="ATTENCE", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=800, y=300, width=220, height=40)

        img9 = Image.open(r"D:\tkimages\helpdesk.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Button(f_lbl1, image=self.photoimg9, cursor="hand2")
        b2.place(x=1100, y=100, width=220, height=220)

        b1 = Button(f_lbl1, text="HELP DESK", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=1100, y=300, width=220, height=40)

        img10 = Image.open(r"D:\tkimages\train.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b2 = Button(f_lbl1, image=self.photoimg10, cursor="hand2")
        b2.place(x=200, y=350, width=220, height=220)

        b1 = Button(f_lbl1, text="Train", command=self.train_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=200, y=550, width=220, height=40)

        img11 = Image.open(r"D:\tkimages\Akash.png")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2 = Button(f_lbl1, image=self.photoimg11, cursor="hand2")
        b2.place(x=500, y=350, width=220, height=220)

        b1 = Button(f_lbl1, text="Photos",command=self.open_img, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=500, y=550, width=220, height=40)

        img12 = Image.open(r"D:\tkimages\developer.jpg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b2 = Button(f_lbl1, image=self.photoimg12, cursor="hand2")
        b2.place(x=800, y=350, width=220, height=220)

        b1 = Button(f_lbl1, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=800, y=550, width=220, height=40)

        img13 = Image.open(r"D:\tkimages\Exit.png")
        img13 = img13.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        b2 = Button(f_lbl1, image=self.photoimg13, cursor="hand2")
        b2.place(x=1100, y=350, width=220, height=220)

        b1 = Button(f_lbl1, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1.place(x=1100, y=550, width=220, height=40)

        # Create function in button click

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_detect_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Detection(self.new_window)   



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
