import sqlite3
import tkinter
from tkinter import messagebox
import utilsateurs
window=tkinter.Tk()
window.title('Login From')
window.geometry("340x440")
window.config(bg="#333333")
frame=tkinter.Frame(bg="#333333")

def login():
    #Recupiration des valeurs saisies par l'utilisateurs
    u_input=username_entry.get()
    p_input=password_entry.get()

    #Connexion a la base de données
    conn=sqlite3.connect("utilisateurs.db")
    cursor=conn.cursor()

    #Requests SQL securisee pour chercher l'utilsateurs est le mot de passe
    cursor.execute('SELECT * FROM users WHERE username = ? and password = ?',(u_input,p_input))
    result=cursor.fetchone() #recuperer le premier resultat



    if result:
        print("---Contenu de la base de Données---")
        cursor.execute("SELECT * FROM users")
        utt = cursor.fetchall()
        for ligne in utt:
            print(f"ID: {ligne[0]} | Username : {ligne[1]}  | Password: {ligne[2]}")
            print("--------------------------------------------------------------------")
        messagebox.showinfo(title="Login Succes",message="You Successfully Logged in.")
    else:
        messagebox.showinfo(title="Login Failed",message="Invalid Logged.")
    conn.close()

#Creating Widgets
login_label=tkinter.Label(frame,text="Login",bg="#333333",fg="#ffffff",font=('Arial',30))

#Username
username_label=tkinter.Label(frame,text="Username",bg="#333333",fg="#ffffff",font=('Arial',16))
username_entry=tkinter.Entry(frame,font=("Arial",16))

#Password
password_label=tkinter.Label(frame,text="Password",bg="#333333",fg="#ffffff",font=('Arial',16))
password_entry=tkinter.Entry(frame,show="*",font=("Arial",16))

#Button
login_button=tkinter.Button(frame,bg="#ff3399",fg="#ffffff",text="Login",font=('Arial',16),command=login)

#Placing widgets on the screen
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=30)

#Username
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)

#Password
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)

#Button
login_button.grid(row=3,column=0,columnspan=2,pady=30)

frame.pack()
window.mainloop()


