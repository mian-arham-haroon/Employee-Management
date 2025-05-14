from customtkinter import *
from PIL import Image
from tkinter import messagebox 

#------------------------------------------------------------------------#
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("Error","All fields are required")
    elif usernameEntry.get()=='arham' and passwordEntry.get()=='1234':
        messagebox.showinfo('Sucess','login is sucessfull')
        root.destroy()
        import ems
    else:
        messagebox.showerror("Error","wrong credentials")



#------------------------------------------------------------------------#
root=CTk(set_appearance_mode('light'))
root.geometry("930x478")
root.resizable(False,False)
root.title("Login page")
image=CTkImage(Image.open('login.PNG'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='white',font=('Goudy Old style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20,y=100)
usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180,text_color='dark blue',bg_color='white')
usernameEntry.place(x=50,y=150)
passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180,text_color='dark blue',bg_color='white',show='*')
passwordEntry.place(x=50,y=200)
loginButton=CTkButton(root,text="Login",cursor='hand2',command=login)
loginButton.place(x=70,y=250)  
#------------------------------------------------------------------------#




#------------------------------------------------------------------------#
root.mainloop()