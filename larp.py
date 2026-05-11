import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """ Получает абсолютный путь к ресурсам, работает и для dev, и для PyInstaller """
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

IMG_PATH = resource_path("рыбка.jpeg")

def start_hardcore_prank():
    root = tk.Tk()
    
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.overrideredirect(True)

   
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    if os.path.exists(IMG_PATH):
        img = Image.open(IMG_PATH)
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        img = img.resize((sw, sh))
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=photo, bg="black")
        label.pack()
        label.image = photo
    
    root.config(cursor="none")
    root.bind("<FocusOut>", lambda e: root.focus_force())

    root.mainloop()

if __name__ == "__main__":
    start_hardcore_prank()
