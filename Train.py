from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import os
import cv2 as cv
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")

        title_lbl = Label(self.root, text="Train Data set", font=(
            "times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        train = Button(self.root, text="Update",command=self.train_classifier, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        train.place(x=0, y=380)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")
            imageNp = np.array(img, 'unit8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv.imshow("Training", imageNp)
            cv.waitKey(1) == 13
        ids = np.array(ids)
        
        clf = cv.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv.destroyAllWindows()
        messagebox.showinfo("Result", "Traing data set")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
