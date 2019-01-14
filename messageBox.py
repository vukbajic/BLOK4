from tkinter import *
from tkinter import messagebox


def MessageBox(title, message):         #Do you want to exit poruka u posebnom prozoru

    window = Tk()
    window.geometry("90x200")
    window.wm_withdraw()    # pravi prozor u pozadini
    result = messagebox.askyesno(title, message)        # ask yes or no - ocekuje klik na neko od dva ponudjena dugmeta i vraca true-false

    window.destroy()        #unistava prozor u pozadini
    return result
