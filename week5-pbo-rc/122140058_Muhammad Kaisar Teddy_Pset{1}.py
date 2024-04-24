import tkinter as tk
from tkinter import messagebox
import random

class Login:
    def __init__(self):
        self.boxlogin = tk.Tk()
        self.boxlogin.title('Login')
        self.boxlogin.geometry('300x250')

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.captcha_text, self.captcha_answer = self.generate_captcha()

        tk.Label(self.boxlogin, text='Username:').pack()
        self.username_entry = tk.Entry(self.boxlogin, textvariable=self.username)
        self.username_entry.pack()

        tk.Label(self.boxlogin, text='Password:').pack()
        self.password_entry = tk.Entry(self.boxlogin, textvariable=self.password, show='*')
        self.password_entry.pack()

        tk.Label(self.boxlogin, text=f'CAPTCHA: {self.captcha_text}').pack()  # Menampilkan CAPTCHA
        self.captcha_entry = tk.Entry(self.boxlogin)
        self.captcha_entry.pack()

        tk.Button(self.boxlogin, text='Login', command=self.check).pack()
        tk.Button(self.boxlogin, text='Register', command=self.open_register).pack()

        self.users = {'kaisar': 'yangtautauaja', 'kopraljono': 'jenderal'}
        
        self.boxlogin.bind('<Return>', self.check)

    def check(self, event=None):
        if self.username.get() in self.users and self.password.get() == self.users[self.username.get()]:
            if self.captcha_entry.get().lower() == self.captcha_answer.lower():
                messagebox.showinfo('Berhasil login', 'Welcome user')
            else:
                messagebox.showerror('Gagal login', 'CAPTCHA salah')
        else:
            messagebox.showerror('Gagal login', 'Apakah anda terdaftar?')

    def open_register(self):
        self.boxlogin.withdraw()
        self.jendela_register = Register(self.boxlogin, self.users, self.tutup_register)
        self.jendela_register.jendela.protocol("WM_DELETE_WINDOW", lambda: self.tutup_register())
        self.jendela_register.mainloop()

    def close_register(self):
        self.boxlogin.deiconify()

    def run(self):
        self.boxlogin.mainloop()

    def generate_captcha(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            result = num1 * num2
        captcha_text = f'{num1} {operator} {num2} = ?'
        return captcha_text, str(result) 

class Register:
    def __init__(self, master, users, callback):
        self.jendela = tk.Toplevel()
        self.jendela.title('Register')
        self.jendela.geometry('300x350')

        self.users = users
        self.callback = callback  
        self.username_register = tk.StringVar()
        self.password_register = tk.StringVar()
        self.cek_password = tk.StringVar()
        self.captcha = self.generate_captcha()

        tk.Label(self.jendela, text='Username:').pack()
        self.username_entry = tk.Entry(self.jendela, textvariable=self.username_register)
        self.username_entry.pack()

        tk.Label(self.jendela, text='Password:').pack()
        self.password_entry = tk.Entry(self.jendela, textvariable=self.password_register)
        self.password_entry.pack()

        tk.Label(self.jendela, text='Confirm Password:').pack()
        self.confirm_password_entry = tk.Entry(self.jendela, textvariable=self.cek_password)
        self.confirm_password_entry.pack()

        tk.Label(self.jendela, text='CAPTCHA: ' + self.captcha[0]).pack()  
        self.captcha_entry = tk.Entry(self.jendela, textvariable=tk.StringVar())
        self.captcha_entry.pack()  

        tk.Button(self.jendela, text='Register', command=self.tombol_register).pack()

        self.jendela.bind('<Return>', self.tombol_register)

    def tombol_register(self, event=None):
        
        if self.captcha[1].lower() == self.captcha_entry.get().lower():
            if self.password_register.get() == self.confirm_password_entry.get():
                if not self.ada_username(self.username_register.get()):
                    self.users[self.username_register.get()] = self.password_register.get()
                    messagebox.showinfo('Registrasi diterima', 'Selamat!')
                    self.callback() 
                    self.jendela.destroy()
                else:
                    messagebox.showerror('Register Gagal', 'Ulangi registrasi')
            else:
                messagebox.showerror('Error', 'Password tidak sesuai')
        else:
            messagebox.showerror('Error', 'CAPTCHA ditolak')

    def ada_username(self, username):
        return username in self.users

    def generate_captcha(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            result = num1 * num2
        captcha_text = f'{num1} {operator} {num2} = ?'
        return (captcha_text, str(result))

login = Login()
login.run()
