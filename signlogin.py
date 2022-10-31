from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from main import Face_Recognition_System
from tkinter import messagebox


class Signup_Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")
################################################

        self.var_username = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_password1 = StringVar()
        self.var_email1 = StringVar()
        self.var_pass = StringVar()

        f_title = Label(self.root)
        f_title.place(x=0, y=130, width=1530, height=710)


#################################################################################################
        title_lbl = Label(f_title, text="USER REGISTER AND LOGIN", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

##########################################################

        left_frame = LabelFrame(f_title, bd=2, bg="white", relief=RIDGE)
        left_frame.place(x=200, y=100, width=500, height=300)

        Heading_lbl = Label(f_title, text="Student Signup", font=(
            "times new roman", 15, "bold"), bg="white", fg="blue")
        Heading_lbl.place(x=220, y=120, width=400, height=40)

        username_lbl = Label(f_title, text="User Name",
                             font=("times new roman", 15, "bold"), bg="white")
        username_lbl.place(x=280, y=160)

        username_entry = Entry(f_title, textvariable=self.var_username, font=(
            "times new roman", 15, "bold"), width=15)
        username_entry.place(x=400, y=160)

        email_lbl = Label(f_title, text="Email", font=(
            "times new roman", 15, "bold"), bg="white")
        email_lbl.place(x=280, y=190)

        email_entry = Entry(f_title, textvariable=self.var_email, font=(
            "times new roman", 15, "bold"), width=15)
        email_entry.place(x=400, y=190)

        password_lbl = Label(f_title, text="Password",
                             font=("times new roman", 15, "bold"), bg="white")
        password_lbl.place(x=280, y=220)

        password_entry = Entry(f_title, textvariable=self.var_password, font=(
            "times new roman", 15, "bold"), width=15)
        password_entry.place(x=400, y=220)

        password1_lbl = Label(f_title, text="Password1",
                              font=("times new roman", 15, "bold"), bg="white")
        password1_lbl.place(x=280, y=260)

        password1_entry = Entry(f_title, textvariable=self.var_password1, font=(
            "times new roman", 15, "bold"), width=15)
        password1_entry.place(x=400, y=260)

    # ##################################Login ################
        right_frame = LabelFrame(f_title, bd=2, bg="white", relief=RIDGE)
        right_frame.place(x=800, y=100, width=500, height=300)

        Heading_lbl = Label(f_title, text="Student Login", font=(
            "times new roman", 15, "bold"), bg="white", fg="blue")
        Heading_lbl.place(x=840, y=120, width=400, height=40)

        email_lbl = Label(f_title, text="Email", font=(
            "times new roman", 15, "bold"), bg="white")
        email_lbl.place(x=920, y=160)

        email_entry = Entry(f_title, textvariable=self.var_email1, font=(
            "times new roman", 15, "bold"), width=15)
        email_entry.place(x=1000, y=160)

        password_lbl = Label(f_title, text="Password",
                             font=("times new roman", 15, "bold"),bg="white")
        password_lbl.place(x=900, y=200)

        password_entry = Entry(f_title, textvariable=self.var_pass, font=(
            "times new roman", 15, "bold"), width=15)
        password_entry.place(x=1000, y=200)

        signup_b = Button(f_title, text="Signup", command=self.signup, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="white")
        signup_b.place(x=280, y=300, width=300, height=40)
        login_b = Button(f_title, text="Login", command=self.login, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="white")
        login_b.place(x=900, y=240, width=300, height=40)

   
    # Create function in button click

    def signup(self):
        if (self.var_username.get() == "" or self.var_email.get() == "" or self.var_password.get() == "" or self.var_password1.get() == ""):
            if self.var_password.get() == self.var_password1.get():
                messagebox.showinfo("Error", "Dute to :", parent=self.root)
        else:
            messagebox.showinfo("Success", "student deatils add successfully", parent=self.root)

    def login(self):
        if ( self.var_email1.get() == "" or self.var_pass.get() == "" ):
            messagebox.showinfo("Error", "Dute to :", parent=self.root)
        else:
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)
            # messagebox.showinfo("Success", "student deatils add successfully", parent=self.root)

        


if __name__ == "__main__":
    root = Tk()
    obj = Signup_Login(root)
    root.mainloop()
