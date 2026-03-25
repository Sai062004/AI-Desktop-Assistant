import tkinter as tk
from tkinter import LabelFrame, Label, Text, Entry, Button, CENTER, SOLID, END
from PIL import Image, ImageTk # type: ignore
import speech_to_text
import Action
root = tk.Tk()
root.title("AI Assistant")
root.geometry("600x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")
4
# Ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = Action.Action(user_val)  
    text.insert(END, "User---> " + user_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT<--- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()  

# Send function
def send():
    send = entry.get()
    bot = Action.Action(send)
    text.insert(END, "User---> " + send + "\n")
    if bot is not None:
        text.insert(END, "BOT<--- " + str(bot) + "\n")

    if bot == "ok sir":
        root.destroy() 

# Delete function
def del_text():
    text.delete(1.0, "end")  

# Frame
frame = LabelFrame(root, padx=120, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text label
text_label = Label(frame, text="AI Assistant", font=("Times New Roman", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image_path = r"C:\Users\Public\Venkyyy\Projects\ai assistant\assitant.png"
try:
    image = ImageTk.PhotoImage(Image.open(image_path))
    image_label = Label(frame, image=image)
    image_label.grid(row=1, column=0, pady=20)
except Exception as e:
    print(f"Error loading image: {e}")

# Adding a text widget
text = Text(root, font=('Courier 10 bold'), bg="#356696")
text.place(x=100, y=375, width=400, height=100)

# Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=125, y=500, width=350, height=30)

# Button 1
Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# Button 2
Button2 = Button(root, text="SEND", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# Button 3
Button3 = Button(root, text="DELETE", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)

root.mainloop()
