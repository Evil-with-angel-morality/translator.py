import time
import os
from deep_translator import *
from tkinter import *



#color
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'




os.system("color 20")


def cls ():
    os.system('clear' or 'cls')
    ran()




#Update
def Update ():
    print(color.red+" [       ] 0%")
    time.sleep(1)
    print(color.abi_kamrang+" [=======   ] 20%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [============ ] 40%")
    time.sleep(0.5)
    print(color.abi_kamrang+" [================ ] 60%")
    time.sleep(0.8)
    print(color.abi_kamrang+" [==================== ] 80%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [========================= ] 100%")
    os.system('clear' or 'cls')
    os.system('python -m pip install pip')
    os.system('pip install pip')
    os.system('pip install os')
    os.system('pip install time')
    os.system('pip install sys')
    os.system('pip install socket')
    os.system('pip install colorama')
    os.system('pip install thread')










#Update
root = Tk()
root.title('Update')
root.minsize(300,100)
root.maxsize(300,80)
root.resizable(width=False,height=False)
Button(root, text='Click on me to update the translator', command=Update,bg='powder blue' ).pack()
root.mainloop()






def ran ():
    os.system("cls" or "clear")
    print("________________________WELCOM_____________________________")
    print("")
    print("-------------------Enter Langegt-----------------------------")
    print("")
    print("    Use acronyms. Proverbs => English >> en")
    print("")
    time.sleep(2)
    lan = input("  Enter home langect ==  ")
    print("")
    llan = input("  In what language should it be translated? ==  ")
    os.system('cls')
    text = input("  Enter your text ==  ")
    texttor = GoogleTranslator(source=lan,target=llan).translate(text)
    print(texttor)
    root = Tk()
    root.title('your text')
    root.minsize(400,200)
    Button(root, text= texttor).pack()
    anv = input("  and ?   (n/y)?  ==  ")
    if anv == ("y") or anv == ("Y"):
        cls()
ran()




