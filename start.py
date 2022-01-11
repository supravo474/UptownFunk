from tkinter import *
import os
window=Tk()
window.geometry("300x200+10+10")
window.eval('tk::PlaceWindow . center')
lbl=Label(window, text="UPTOWN PUNK", fg='red', font=("Helvetica", 16))
lbl.place(x=80, y=50)
window.title('UPTOWN PUNK')
def take():
    os.system('python main.py')
    window.quit()
btn=Button(window, text="Play!!!!", fg='blue',command = take)
btn.place(x=130, y=100)
def quit():
    window.quit()
btn2=Button(window, text="Quit", fg='blue',command = quit)
btn2.place(x=134, y=130)


window.mainloop()