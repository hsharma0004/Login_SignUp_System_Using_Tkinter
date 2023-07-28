from tkinter import *
from PIL import ImageTk, ImageFont
from tkinter import messagebox
import ast


class Login():
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+150+90")
        self.root.resizable(False, False)  # To Disable the maximize button
        # ------BGImage--------
        self.bg = ImageTk.PhotoImage(file="D:\VS STUDIO/Login Image.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, width=1199, height=600)

        Login_Frame = Frame(self.root, bg="#66CDAA")
        Login_Frame.place(x=40, y=200, height=350, width=300)

        title = Label(Login_Frame, text="Login Here ", font=(
            "Impact", 30, "bold", "italic"), fg="Black", bg="#66CDAA").place(x=30, y=30)
        descrip = Label(Login_Frame, text="Fellow Coder's Login Area", font=(
            "Goudy old style", 15, "bold", "italic"), fg="black", bg="#66CDAA").place(x=30, y=85)
        lbl_user = Label(Login_Frame, text="Username", font=(
            "Goudy old style", 15, "bold", "italic"), fg="black", bg="#66CDAA").place(x=30, y=125)

        self.text_user = Entry(Login_Frame, font=(
            "Times New Roman", 13, "italic"))
        self.text_user.place(x=30, y=155, width=200, height=30)
        lbl_pass = Label(Login_Frame, text="Password", font=(
            "Goudy old style", 15, "bold", "italic"), fg="black", bg="#66CDAA").place(x=30, y=185)
        self.text_pass = Entry(Login_Frame, font=(
            "Times New Roman", 13, "italic"))
        self.text_pass.place(x=30, y=215, width=200, height=30)

        signup = Button(Login_Frame, text="Sign up? ", fg="blue", font=(
            "Times New Roman", 12), bg="#66CDAA", bd=0, command=self.sign_up).place(x=30, y=250)

        Login_btn = Button(Login_Frame, text="Login", fg="black", font=(
            "Times New Roman", 18), bg="orange", command=self.login_function).place(x=90, y=300, width=100, height=40)

    def login_function(self):
        name = self.text_user.get()
        pass_word = self.text_pass.get()
        f1 = open('Data_Sheet.txt', 'r')
        d1 = f1.read()
        r1 = ast.literal_eval(d1)
        f1.close()

        print(r1.keys())
        print(r1.values())

        if name in r1.keys() and pass_word == r1[name]:
            messagebox.showinfo('Login In', 'Logged In Successfully')
        elif name == '' and pass_word == '':
            messagebox.showerror("Warning", "All Fields required")
        else:
            messagebox.showerror(
                "Alert", "You entered wrong Username/Password")

# The code opens the file 'Data_Sheet.txt' in read mode ('r') using the open() function and assigns the file object to the variable f1.

# It reads the contents of the file using f1.read(), which returns the data as a string. The data in the file is expected to be in a dictionary format.

# The code uses ast.literal_eval(d1) to convert the string read from the file into a Python dictionary (r1). This step assumes that the content of 'Data_Sheet.txt' is a valid dictionary in string format. If the conversion fails due to invalid data, it may raise a ValueError.

# After reading and converting the data, the file is closed using f1.close(). This is good practice as it frees up system resources associated with the file.

# The code then prints the keys and values of the dictionary r1 obtained from the file. r1.keys() prints all the keys in the dictionary, and r1.values() prints all the corresponding values.

    def sign_up(self):
        sign_frame = Frame(self.root, bg="white")
        sign_frame.place(x=450, y=0, height=600, width=1000)

        self.sign_img = ImageTk.PhotoImage(file="D:\VS STUDIO/Sign_up.jpg")
        self.bg_sign_img = Label(
            sign_frame, image=self.sign_img).place(x=0, y=0)

        sign_up_frame = Frame(self.root, bg="white",)
        sign_up_frame.place(x=0, y=0, height=600, width=450)

        sign_title = Label(sign_up_frame, text="Sign Up ", font=(
            "Impact", 40, "italic"), fg="Black", bg="white").place(x=50, y=60)

        sing_up_user = Label(sign_up_frame, text="Enter Username", font=(
            "Goudy old style", 15, "bold", "italic"), fg="black", bg="white").place(x=50, y=180)
        self.sign_up_text_user = Entry(sign_up_frame, font=(
            "Times New Roman", 12), fg="black", bg="white")
        self.sign_up_text_user.place(
            x=50, y=220, bordermode=INSIDE, height=30, width=251)

        sing_up_pass = Label(sign_up_frame, text="Enter Password", font=(
            "Goudy old style", 15, "bold", "italic"), fg="black", bg="white").place(x=50, y=270)
        self.sign_up_pass = Entry(sign_up_frame, font=(
            "Times New Roman", 12), fg="black", bg="white")
        self.sign_up_pass.place(
            x=50, y=300, bordermode=INSIDE, height=30, width=251)

        sing_up_con_pass = Label(sign_up_frame, text="Confirm Password", font=(
            "Goudy old style", 15, "bold", "italic"), fg="black", bg="white").place(x=50, y=350)
        self.sign_up_con_pass = Entry(sign_up_frame, font=(
            "Times New Roman", 12), fg="black", bg="white")
        self.sign_up_con_pass.place(
            x=50, y=380, bordermode=INSIDE, height=30, width=251)

        Sign_up_btn = Button(sign_up_frame, text="Sign Up ", fg="white", font=(
            "Times New Roman", 18), bg="Blue", command=self.signup).place(x=130, y=470, width=100, height=40)

    def signup(self):
        username = self.sign_up_text_user.get()
        password = self.sign_up_pass.get()
        con_pass = self.sign_up_con_pass.get()

        if username == '' or password == '':
            messagebox.showinfo('Warning', 'Please fill all the fields')
        elif password == con_pass:
            try:
                file = open('Data_Sheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
               # file.truncate(0)
                file.close()

                file = open('Data_Sheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Sign Up', 'Successfully Signed Up')
            except:
                file = open("Data_Sheet.txt", "w")
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()
        elif password != con_pass:
            messagebox.showerror("Error", "Both Passwords Should match")


'''
Explaination of the above function
In the provided code, file.truncate(0) is used to truncate (empty) the contents of the file opened in write mode. In this context, the file being referred to is 'Data_Sheet.txt', which is being used to store user data.

Here's a breakdown of how it works:

1) The code opens the file 'Data_Sheet.txt' in read and write mode ('r+'). This mode allows the file to be read and written to.

2) It then reads the contents of the file using file.read(). The data is read as a string.

3) The code uses ast.literal_eval(d) to convert the string read from the file into a Python dictionary (r). The data in the file is expected to be in a dictionary format.

4) It then creates a new dictionary dict2 containing the username as the key and password as the value.

5) The code updates the existing dictionary r with the new key-value pair from dict2 using r.update(dict2). Now, r contains the updated user data with the new user's information.

6) The next step is to clear the contents of the file in preparation for writing the updated data back into it. This is done by using file.truncate(0). The argument 0 passed to truncate() indicates that the file's size should be set to 0, effectively clearing its contents.

7) The file is then closed with file.close().

8) After truncating and closing the file, it is reopened in write mode ('w') to write the updated data back into it.

9) The updated dictionary r is converted back into a string using str(r), and this string representation of the dictionary is written into the file using file.write().

So, in summary, file.truncate(0) is used to clear the contents of the file, allowing new data to be written to it in the next steps. This ensures that the file is ready to store the updated user data after adding a new user during the signup process.

'''
root = Tk()
obj = Login(root)
root.mainloop()