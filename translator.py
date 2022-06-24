from tkinter import *
from deep_translator import *



def notpad():
    root = Tk()
    root.title('NOTPAD PRO')
    root.minsize(600,400)
    tn = Text(root).pack()
    root.mainloop()





window = Tk()


window.minsize(400,200)
window.maxsize(1000,200)
window.title("transltor")



def Translation():
    texttor = GoogleTranslator(source=name.get(),target=family_name.get()).translate(txt.get())
    user_name.configure(text=texttor)
    roo = Tk()
    roo.title('Translation')
    Label(roo, text=texttor).pack()
    roo.mainloop()




Label(window, text="Home language").pack()
name = Entry(window)
name.pack()


Label(window, text="In what language should it be translated?").pack()
family_name = Entry(window)
family_name.pack()


Label(window, text="Text").pack()
txt = Entry(window)
txt.pack()



notp = Button(window,text="Open notPad",command=notpad)
notp.pack()


btn = Button(window,text="Translation",command=Translation)
btn.pack()


user_name = Label(window)
user_name.pack()


window.mainloop()

