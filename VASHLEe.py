#Proje baslangıc tarihi 2023
from cryptography.fernet import Fernet
import os
import customtkinter as ctk
from tkinter import messagebox
import time
import pyperclip
import sys

base_path = os.environ["USERPROFILE"]
main_file = os.path.join(base_path, "Kasa")
pass_file = os.path.join(main_file, "pass.txt")

#bilgilendirme
def information():
    to_inform_text = """
Açıklama

Uygulamamız tüm kullanıcılarımız için ücretsizdir. 
Herhangi bir kişi veya kurum tarafından sizden ücret talep edilmesi durumunda lütfen itibar etmeyiniz. Desteğiniz ve 
güveniniz için teşekkür ederiz.


Yapımcı:Nyoxs
Github:https://github.com/NYOXS-01
Yayınlama Tarihi:23/02/2026

"""

    info = ctk.CTk()
    info.geometry("450x250")
    info.title("İnfo")
    info.resizable(height=False,width=False)

    info_text = ctk.CTkLabel(info, text=to_inform_text,wraplength=420,justify="left",font=("Ariel",15))
    info_text.place(x=15,y=5)

    info.mainloop()

#şifre ekleme
def password_add():
    global paswd_add
    paswd_add = ctk.CTk()
    paswd_add.geometry("450x250")

    paswd_add.resizable(height=False,width=False)
    paswd_add.title("Add Password")

    password_title = ctk.CTkLabel(paswd_add, text="Başlık",font=("Arial",18))
    password_title.place(x=15,y=15)

    password_title_input = ctk.CTkEntry(paswd_add,width=300)
    password_title_input.place(x=130, y=15)

    password_name = ctk.CTkLabel(paswd_add, text="Mail & İsim",font=("Arial",18))
    password_name.place(x=15,y=55)

    password_name_input = ctk.CTkEntry(paswd_add, width=300)
    password_name_input.place(x=130, y=55)

    password = ctk.CTkLabel(paswd_add, text= "Parola",font=("Arial",18))
    password.place(x=15,y=95)

    password_input = ctk.CTkEntry(paswd_add, width=300)
    password_input.place(x=130,y=95)

    password_notes = ctk.CTkLabel(paswd_add, text="Açıklama",font=("Ariel",18))
    password_notes.place(x=15,y=135)

    password_notes_input = ctk.CTkEntry(paswd_add,width=300)
    password_notes_input.place(x=130, y=135)

    def password_list_add():
        pass_data = f"""
---------------------------------------

Başlık: {password_title_input.get()}
Mail & İsim: {password_name_input.get()}
Parola: {password_input.get()}
Açıklama: {password_notes_input.get()}

"""
        try:
            with open(pass_file,"a",encoding="utf-8") as file:
                file.write(pass_data)
                file.close()
            password_title_input.delete(0,ctk.END)
            password_name_input.delete(0,ctk.END)
            password_input.delete(0,ctk.END)
            password_notes_input.delete(0,ctk.END)
            refresh_list() 
        except:
            messagebox.showerror("VASHLEe Eror","Parola kaydedilirken Hata Oluştu?")

    pass_add_button = ctk.CTkButton(paswd_add,text="Kaydet",width=120,command=password_list_add)
    pass_add_button.place(x=165,y=200)

    paswd_add.mainloop()


#şifre yönetim kısmı
def pass_manager():
    global refresh_list

    def pass_close():
        pass_manager_mainface.destroy()
        try:
             paswd_add.destroy()
        except:
            pass
        
    def refresh_list():

        with open(pass_file,"r",encoding="utf-8") as x:
            pass_data = x.read()
            pass_screen.configure(state="normal")
            pass_screen.delete("1.0",ctk.END)
            pass_screen.insert(ctk.END,pass_data)
            pass_screen.configure(state="disabled")    

    pass_manager_mainface = ctk.CTk()
    pass_manager_mainface.geometry("400x500")
    pass_manager_mainface.resizable(width=False, height=False)
    pass_manager_mainface.title("Pass Manager")
    pass_manager_mainface.protocol("WM_DELETE_WINDOW",pass_close)

    pass_screen = ctk.CTkTextbox(pass_manager_mainface, height=440,width=380,state="disabled")
    pass_screen.place(x=10,y=10)

    refresh_list()

    add_pass_list_button = ctk.CTkButton(pass_manager_mainface,text="Parola Ekle",width=160,command=password_add)
    add_pass_list_button.place(x=120,y=460)

    pass_manager_mainface.mainloop()


#Yeni Key oluşturma kısmı
def new_key(file):
    global KEY 
    KEY = Fernet.generate_key()
    pyperclip.copy(KEY.decode())
    messagebox.showinfo("VAHSLEe","Key Kopyalandı.")
    encrypt_folder(file)


#dosya şifreleme kısmı
def encrypt(file_path):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        fernet = Fernet(KEY)
        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, "wb") as encrypt_write:
            encrypt_write.write(encrypted_data) 

    except Exception as e:
        messagebox.showerror("VASHLEe","Dosya Şifrelenirken Hata Oluştu.")
        print(f"Dosya Şifrelenirken Hata Oluştu: {e}")

def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Şifreleniyor: {file_path}")
            encrypt(file_path)


#dosya şifre açma kısmı
def decrypt(file_path, key):
    try:
        with open(file_path, "rb") as f:
            encrypted = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted)

        with open(file_path, "wb") as f:
            f.write(decrypted)

        return True
    except Exception as e:
        print("Şifre çözme hatası:", e)
        return False

# -------------------------------------------------
# KLASÖR ŞİFRE AÇ (KRİTİK KISIM)
# -------------------------------------------------
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            path = os.path.join(root, name)
            print("Açılıyor:", path)

            if not decrypt(path, key):
                messagebox.showerror("VASHLEe Eror","Key Yanlış!")
                return  

    # SADECE HER ŞEY BAŞARILIYSA
    login_root.destroy()
    main_interface()

#ilk kurulum oluşturma
def initially():
    if os.path.exists(main_file):
        login_main_interface()
    else:
        os.mkdir(main_file)
        with open(os.path.join(main_file, "pass.txt"), "wb") as main_filex:
            main_filex.close()
        time.sleep(3)
        information()
        new_key(main_file)


#şifreli dosya klasörü açma bölümü
def file_manager_open():
    os.startfile(main_file)


#key kontrol
def login_main_interface():
    global input_key
    global login_root
    key_attempt = 0

    login_root = ctk.CTk()
    login_root.title("Login")
    login_root.geometry("300x120")
    login_root.resizable(width=False, height=False)

    Key_screen = ctk.CTkLabel(login_root, text="KEY", font=("Arial", 21))
    Key_screen.place(x=10, y=15)

    input_key = ctk.CTkEntry(login_root, width=230)
    input_key.place(x=55, y=16)

    def login():
        nonlocal key_attempt

        key = input_key.get().encode()
        if len(key) == 44:
            decrypt_folder(main_file, key)
        else:
            key_attempt += 1
            if key_attempt >= 3:
                messagebox.showerror("VASHLEe Eror", "Deneme Haklarınız Bitti Uygulama Kapatılıyor.")
                sys.exit()
            else:
                messagebox.showerror("VASHLEe Eror", "Key hatalı! En fazla 3 deneme hakkınız vardır.")

    login_button = ctk.CTkButton(login_root, text="Login", command=login)
    login_button.place(x=85, y=80) 

    login_root.mainloop()


#ana menü
def main_interface():
    global till_situation
    global root

    def exit_encrypted():
        new_key(main_file)
        sys.exit()
    root = ctk.CTk()
    root.geometry("400x250")
    root.resizable(width=False, height=False)
    root.title("VASHLEe Crypt")
    root.protocol("WM_DELETE_WINDOW",exit_encrypted)
    # Buton oluştur
    till_encrypt_button = ctk.CTkButton(root, text="Dosya Yöneticisi", compound="left", width=200, height=40, command=file_manager_open)
    till_encrypt_button.place(x=100, y=70)

    pass_manager_button = ctk.CTkButton(root, text="Parola Yöneticisi", compound="left", width=200, height=40,command=pass_manager)
    pass_manager_button.place(x=100, y=120)

    root.mainloop()
initially()
