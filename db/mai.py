import tkinter as tk
from sqlalchemy import create_engine
import pandas as pd
from PIL import Image, ImageTk
from tkinter import messagebox

engine = create_engine('postgresql://postgres:admin@localhost/proba')

users_df = pd.read_sql('SELECT u.password, u.login, u.fio, r.name as role_name FROM users u JOIN role r ON u.role_id = r.id', engine)
print(users_df)

try:
    users_df = pd.read_sql('SELECT u.password, u.login, u.fio, r.name as role_name FROM users u JOIN role r ON u.role_id = r.id', engine)
    valid_role = users_df['role_name'].to_list()
    valid_password= users_df['password'].to_list()
    valid_login = users_df['login'].to_list()
    valid_fio = users_df['fio'].to_list()
except:
    valid_role = []
    valid_fio =[]
    valid_login=[]
    valid_password=[]
    messagebox.showerror('Ошибка','В бд проблема')


class MainWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('300x300')

        ima= ImageTk.PhotoImage(Image.open('icon.png').resize((60,60)))
        label =tk.Label(self.window,image=ima)
        label.image = ima
        label.pack()

        label1 = tk.Label(self.window, text='Магазин Товаров', font=('Times New Roman',20))
        label1.pack()

        label_login = tk.Label(self.window, text='Логин:', font=('Times New Roman',10))
        label_login.pack()

        self.login_inpu = tk.Entry(self.window, width=10)
        self.login_inpu.pack(pady=5,padx=5)

        label_password = tk.Label(self.window, text='Пароль:', font=('Times New Roman',10))
        label_password.pack(pady=5,padx=5)

        self.login_password = tk.Entry(self.window, width=10)
        self.login_password.pack(pady=5,padx=5)

        login_btn = tk.Button(self.window, command=self.proverka, text='Войти')
        login_btn.pack(pady=5,padx=5)





        self.window.mainloop()

    def proverka(self):
        login_imput = self.login_inpu.get()
        password_input = self.login_password.get()

        if login_imput in valid_login:
            index = valid_login.index(login_imput)
            if password_input == valid_password[index]:
                fio = valid_fio[index]
                role = valid_role[index]
                self.window.destroy()
                TwoWindow(fio,role)
            else:
                messagebox.showerror('Ошибка','не в БД параша')
        else:
            messagebox.showerror('Ошибка','не в БД параша')

def TwoWindow(self, fio, role):
        self.window1 = tk.Tk()
        self.window1.geometry('300x300')
        
        label_login = tk.Label(self.window, text='Добро пожаловать' + fio, font=('Times New Roman',10))
        label_login.pack()

        

        self.window1.mainloop()











a = MainWindow()
        