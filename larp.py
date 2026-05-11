import tkinter as tk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(__file__)
IMG_PATH = os.path.join(BASE_DIR, "рыбка.jpeg")

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
