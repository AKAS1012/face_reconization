from tkinter import *
from tkinter import ttk
from turtle import update
import psycopg2 as db
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
import numpy as np


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management system")
        self.conn = db.connect(user='postgres', password='Nikhil@123',
                               host='localhost', port="5432", database="Facebook")

        # Text variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_rollno = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phoneno = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
      

    # ##########################################################
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

        title_lbl = Label(f_lbl1, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

       ##############################################################
        main_frame = Frame(f_lbl1, bd=2, bg="white")
        main_frame.place(x=20, y=40, width=1480, height=600)

        left_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                text="stuedent details", font=("times new roman", 14, "bold"))
        left_frame.place(x=10, y=50, width=720, height=580)

        img2 = Image.open(r"D:\tkimages\detection.jpg")
        img2 = img2.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=14, y=200, width=710, height=100)

        current_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                   text="Current Course details ", font=("times new roman", 14, "bold"))
        current_frame.place(x=14, y=150, width=700, height=150)

        dep_lbl = Label(current_frame, text="Management", font=(
            "times new roman", 12, "bold"))
        dep_lbl.grid(row=0, column=0)

        dep_combo = ttk.Combobox(current_frame, textvariable=self.var_dep, font=(
            "new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("select department", "Computer",
                               "Information Technology", "Civil", "Mechinical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        course_lbl = Label(current_frame, text="Course", font=(
            "times new roman", 12, "bold"))
        course_lbl.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_frame, textvariable=self.var_course, font=(
            "new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("select Course", "IT", "ME", "CE", "ME")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        year_lbl = Label(current_frame, text="Year", font=(
            "times new roman", 12, "bold"))
        year_lbl.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_frame, textvariable=self.var_year, font=(
            "new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("select Year", "2021-22",
                                "2021-23", "2021-24", "2021-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        sem_lbl = Label(current_frame, text="semnster", font=(
            "times new roman", 12, "bold"))
        sem_lbl.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_frame, textvariable=self.var_sem, font=(
            "new roman", 12, "bold"), state="readonly", width=20)
        sem_combo["values"] = ("select Semester", "I", "II", "III", "IV")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

       ################################################################################
        right_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                 text="Class student details", font=("times new roman", 14, "bold"))
        right_frame.place(x=14, y=280, width=700, height=300)

        class_student_lbl = Label(right_frame, text="student:", font=(
            "times new roman", 12, "bold"))
        class_student_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = Entry(right_frame, textvariable=self.var_std, font=(
            "times new roman", 12, "bold"), width=13)
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        student_lbl = Label(right_frame, text="student name", font=(
            "times new roman", 15, "bold"))
        student_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_entry = Entry(right_frame, textvariable=self.var_std_name, font=(
            "times new roman", 12, "bold"), width=15)
        student_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        class_div_lbl = Label(right_frame, text="class Division", font=(
            "times new roman", 15, "bold"))
        class_div_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # div_entry = Entry(right_frame, textvariable=self.var_div, font=(
        #     "times new roman", 12, "bold"), width=15)
        # div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        division_combo = ttk.Combobox(right_frame, textvariable=self.var_div, font=(
            "new roman", 12, "bold"), state="readonly", width=20)
        division_combo["values"] = ("A", "B", "C")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        roll_lbl = Label(right_frame, text="Roll no", font=(
            "times new roman", 15, "bold"))
        roll_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_entry = Entry(right_frame, textvariable=self.var_rollno, font=(
            "times new roman", 15, "bold"), width=15)
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        gender_lbl = Label(right_frame, text="Gender", font=(
            "times new roman", 15, "bold"))
        gender_lbl.grid(row=2, column=0, padx=10, sticky=W)

        # gender_entry = Entry(right_frame, textvariable=self.var_gender, font=(
        #     "times new roman", 15, "bold"), width=15)
        # gender_entry.grid(row=2, column=1, padx=10, sticky=W)
        gender_combo = ttk.Combobox(right_frame, textvariable=self.var_gender, font=(
            "new roman", 12, "bold"), state="readonly", width=20)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, sticky=W)

        dob_lbl = Label(right_frame, text="DOB", font=(
            "times new roman", 12, "bold"))
        dob_lbl.grid(row=2, column=2, padx=10, sticky=W)

        dob_entry = Entry(right_frame, textvariable=self.var_dob, font=(
            "times new roman", 12, "bold"), width=13)
        dob_entry.grid(row=2, column=3, padx=10, sticky=W)

        mail_lbl = Label(right_frame, text="Email", font=(
            "times new roman", 12, "bold"))
        mail_lbl.grid(row=3, column=0, padx=10, sticky=W)

        mail_entry = Entry(right_frame, textvariable=self.var_email, font=(
            "times new roman", 12, "bold"), width=13)
        mail_entry.grid(row=3, column=1, padx=10, sticky=W)

        no_lbl = Label(right_frame, text="Phone No", font=(
            "times new roman", 12, "bold"))
        no_lbl.grid(row=3, column=2, padx=10, sticky=W)

        no_entry = Entry(right_frame, textvariable=self.var_phoneno, font=(
            "times new roman", 12, "bold"), width=13)
        no_entry.grid(row=3, column=3, padx=10, sticky=W)

        add_lbl = Label(right_frame, text="Address", font=(
            "times new roman", 12, "bold"))
        add_lbl.grid(row=4, column=0, padx=10, sticky=W)

        add_entry = Entry(right_frame, textvariable=self.var_address, font=(
            "times new roman", 12, "bold"), width=13)
        add_entry.grid(row=4, column=1, padx=10, sticky=W)

        techer_lbl = Label(right_frame, text="Teacher", font=(
            "times new roman", 12, "bold"))
        techer_lbl.grid(row=4, column=2, padx=10, sticky=W)

        techer_entry = Entry(right_frame, textvariable=self.var_teacher, font=(
            "times new roman", 12, "bold"), width=13)
        techer_entry.grid(row=4, column=3, padx=10, sticky=W)
##################################
       
        radiobtn1 = ttk.Radiobutton(right_frame, variable=self.var_radio1, text="Take Photo sample", value="Yes")
        radiobtn1.grid(row=5, column=0)
       
        radiobtn2 = ttk.Radiobutton(right_frame, variable=self.var_radio1, text="No Photo sample", value="No")
        radiobtn2.grid(row=5, column=1)

    ############################################################################
        btn_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=200, width=717, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.save, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset, text="reset", width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=2, pady=0, sticky=W)

        photo_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        photo_frame.place(x=5, y=235, width=717, height=35)

        take_photo_btn = Button(photo_frame, command=self.generate_data, text="Take Photo sample", width=40, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(photo_frame, text="Update photo sample ", width=40, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1)

        left_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                text="stuedent details", font=("times new roman", 14, "bold"))
        left_frame.place(x=750, y=50, width=720, height=580)

        img4 = Image.open(r"D:\tkimages\detection.jpg")
        img4 = img4.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(self.root, image=self.photoimg4)
        f_lbl.place(x=760, y=200, width=710, height=100)

        search_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 14, "bold"))
        search_frame.place(x=760, y=180,  width=700, height=70)

        dep_lbl = Label(search_frame, text="Search By", font=(
            "times new roman", 12, "bold"), bg="red")
        dep_lbl.grid(row=0, column=0)

        dep_combo = ttk.Combobox(search_frame, font=(
            "new roman", 12, "bold"), state="readonly", width=15)
        dep_combo["values"] = ("select ", "Roll no", "Phone No", "EC", "EE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=15, sticky=W)

        studentID_entry = Entry(search_frame, font=(
            "times new roman", 12, "bold"), width=17)
        studentID_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        save_btn = Button(search_frame, text="Search", width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=3, padx=4)

        update_btn = Button(search_frame, text="Show All", width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=4, padx=4)

     ############################################################################
        table_frame = LabelFrame(f_lbl1, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=760, y=250,  width=700, height=270)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "IT", "course", "year", "sem", "id", "name", "div", "roll", "gen", "dob", "mail", "mob", "add", "tech","photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("IT", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="semnster")
        self.student_table.heading("id", text="student")
        self.student_table.heading("name", text="student name")
        self.student_table.heading("div", text="class Division")
        self.student_table.heading("roll", text="Roll no")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("mail", text="Email")
        self.student_table.heading("mob", text="Phone No")
        self.student_table.heading("add", text="Address")
        self.student_table.heading("tech", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("IT", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gen", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("mail", width=100)
        self.student_table.column("mob", width=100)
        self.student_table.column("add", width=100)
        self.student_table.column("tech", width=100)
        self.student_table.column("photo", width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
# ####  Button Click functiontes########################

    def save(self):
        if self.var_dep.get() == "select department" or self.var_std_name.get() == "" or self.var_std.get() == "":
            messagebox.showerror(
                "Error", "All Field is required", parent=self.root)
        else:
            try:
                cursor = self.conn.cursor()
                result = cursor.execute("insert into Face_recognization(dep,courses,yyear,semester,student_id,sname, division, roll, gender, dob, email, phoneno, address, teacher, photosample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_dep.get(),
                                                                                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                                                                                         self.var_sem.get(),
                                                                                                                                                                                                                                                         self.var_std.get(),
                                                                                                                                                                                                                                                         self.var_std_name.get(),
                                                                                                                                                                                                                                                         self.var_div.get(),
                                                                                                                                                                                                                                                         self.var_rollno.get(),
                                                                                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                                                                         self.var_phoneno.get(),
                                                                                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                                                                                         self.var_teacher.get(),
                                                                                                                                                                                                                                                         self.var_radio1.get()
                                                                                                                                                                                                                                                         ))

                self.conn.commit()
                print(result)
                self.fetch_data()
                self.conn.close()
                messagebox.showinfo(
                    "Success", "student deatils add successfully", parent=self.root)
            except Exception as ex:
                messagebox.showinfo(
                    "Error", f"Dute to :{str(ex)}", parent=self.root)

    def fetch_data(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from Face_recognization")
        data = cursor.fetchall()
        print(data)
        if (len(data) != 0):
            for i in data:
                self.student_table.insert("", END, values=i)
            self.conn.commit()
        # self.conn.close()

    def get_cursor(self, event=""):
        content_focus = self.student_table.focus()
        content = self. student_table.item(content_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phoneno.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get() == "select department" or self.var_std_name.get() == "" or self.var_std.get() == "":
            messagebox.showerror(
                "Error", "All Field is required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Student Update page", "do you want update this student details", parent=self.root)
                if update > 0:
                    cursor_d = self.conn.cursor()
                    result = cursor_d.execute("update Face_recognization set dep=%s,yyear=%s,semester=%s,student_id=%s,sname=%s, division=%s,roll=%s, gender=%s, dob=%s, email=%s, phoneno=%s, address=%s, teacher=%s, photosample=%s where student_id=%s ",
                                              (self.var_dep.get(), self.var_year.get(), self.var_sem.get(), self.var_std.get(), self.var_std_name.get(), self.var_div.get(), self.var_rollno.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phoneno.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_std.get(), ))
                    self.conn.commit()
                    print(result)
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "success", "Update succesfull this sudent", parent=self.root)
                self.conn.commit()
                print(result)
                self.fetch_data()
                self.conn.close()
            except Exception as ex:
                messagebox.showinfo(
                    "Error", f"Dute to :{str(ex)}", parent=self.root)

    def delete_data(self):
        if self.var_std.get() == "":
            messagebox.showerror(
                "Error", "student id should be required", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno(
                    "Student delete page", "do you want delete this sudent", parent=self.root)
                if Delete > 0:
                    cursor_d = self.conn.cursor()
                    result = "delete from Face_recognization where student_id=%s"
                    val = (self.var_std.get(),)
                    cursor_d.execute(result, val)
                else:
                    if not Delete:
                        return
                self.conn.commit()
                self.fetch_data()
                self.conn.close()
                messagebox.showinfo(
                    "success", "delete succesfull this student", parent=self.root)
            except Exception as ex:
                messagebox.showinfo(
                    "Error", f"Dute to :{str(ex)}", parent=self.root)

    def reset(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_std.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_rollno.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phoneno.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    def generate_data(self):
        if self.var_dep.get() == "select department" or self.var_std_name.get() == "" or self.var_std.get() == "":
            messagebox.showerror(
                "Error", "All Field is required", parent=self.root)
        else:
            try:
                messagebox.askyesno(
                    "Student Update page", "do you want update this student details", parent=self.root)
                cursor_d = self.conn.cursor()
                result = cursor_d.execute("select * from Face_recognization")
                cursor_d.fetchall()
                id = 0
                for x in result:
                    id += 1
                # update()
                cursor_d.execute("update Face_recognization set dep=%s,yyear=%s,semester=%s,student_id=%s,sname=%s, division=%s,roll=%s, gender=%s, dob=%s, email=%s, phoneno=%s, address=%s, teacher=%s, photosample=%s where student_id=%s ", (self.var_dep.get(),
                                                                                                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                                                                                                 self.var_sem.get(),

                                                                                                                                                                                                                                                 self.var_std_name.get(),
                                                                                                                                                                                                                                                 self.var_div.get(),
                                                                                                                                                                                                                                                 self.var_rollno.get(),
                                                                                                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                                                                                                 self.var_phoneno.get(),
                                                                                                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                                                                                                 self.var_teacher.get(),
                                                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                                                 self.var_std.get() == id+1
                                                                                                                                                                                                                                                 ))
                self.conn.commit()
                self.fetch_data()
                self.reset()
                self.conn.close()
                
                face_classifer = cv2.CascadeClassifier('D:\\face_recognization\\haarcascade_frontalface_default.xml')
                print(face_classifer)
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifer.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+w, x:x+h]
                        return face_cropped

                cap = cv2.VideoCapture(0) 
                img_id = 0
                while True:
                    ret, frame = cap.read()
                    if face_cropped(frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user" + str(id) + "."+str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Face cropeed", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Succes", "Image", )
            except Exception as ex:
                messagebox.showinfo(
                    "Error", f"Dute to :{str(ex)}", parent=self.root)

    def searchAll(self):
        pass


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


