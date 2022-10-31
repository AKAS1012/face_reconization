from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import os
import cv2
import psycopg2 as db
from time import strftime
from datetime import datetime

class Face_Detection:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection")
        self.conn = db.connect(user='postgres', password='Nikhil@123',
                               host='localhost', port="5432", database="Facebook")


        title_lbl = Label(self.root, text="Face Detection system", font=(
            "times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)


    def mark_auttence(self, i,r,n,d):
        with open("akash.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            newList = []
            for line in myDataList:
                entry = line.split(("."))
                newList.append(entry[0])
            if ((i  not in newList ) and (r  not in newList ) and (d  not in newList ) and (id  not in newList )):
                date = datetime.now()
                d1 = date.strftime("%d%m%Y")
                dtString = date.strftime("%H:%M:%S")
                f.writelines(f"\n{i}{r}{d}{id}{dtString}{d1} Preset")
                

    def face_reg(self):
        def draw_boundry(img, classifier, scaleFactor,minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            coord = []
            for [x,y, h, w] in features:
                cv2.ractangle(img(x, y), (x+h, y+w), (0,255, 0), 3)
                id, predict=clf.predict(gray_image[y:y+w,x:x+h])
                confidence = int(100*(1-predict/300))
                cursor_d = self.conn.cursor()
                cursor_d.execute("select Roll from Face_recognization where student_id"+str(id))
                i = cursor_d.fetchone()
                i = "+".join(i)

                cursor_d.execute("select Name from Face_recognization where student_id"+str(id))
                r = cursor_d.fetchone()
                r = "+".join(r)

                cursor_d.execute("select department from Face_recognization where student_id"+str(id))
                d = cursor_d.fetchone()
                d = "+".join(d)

                cursor_d.execute("select department from Face_recognization where student_id"+str(id))
                id = cursor_d.fetchone()
                id = "+".join(id)

                if confidence>77:
                    cv2.putText(img, f"student_id:{i}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll:{i}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{r}", (x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"department:{d}", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_auttence(i,r,d,id)
                else:
                    cv2.ractangle(img,(x, y), (x+h, y+w), (0,255, 0), 3)
                    cv2.putText(img, "Unknown face", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord = [x, y, h, w]
            return coord
        
        def reconize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade,1.1,10,(255,255,255),"face", clf)
            return img
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        vedio_cap = cv2.VideoCapture(0)
        while True:
            ret, frame = vedio_cap.read()
            img = reconize(img, clf, face_cascade)
            cv2.imshow("Welcome to face reconization", img)
            if cv2.waitKey(1) == 13:
                        break
                
        vedio_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_Detection(root)
    root.mainloop()
