import tkinter as tk

racine = tk.Tk()
label = tk.Label(racine, text="J'adore Python !")
zone = tk.Entry(racine)

def change_text():
    s = zone.get()
    label["text"] = s


boutonQuit = tk.Button(racine,text ="Quitter ", fg="red", command=racine.destroy)
boutonModifyText = tk.Button(racine,text ="Modifier texte ", fg="Blue", command=change_text)

label.pack()
zone.pack()
boutonQuit.pack()
boutonModifyText.pack()

racine.mainloop()






