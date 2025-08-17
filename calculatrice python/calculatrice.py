import tkinter as tk

expression = ""


root=tk.Tk()
root.title("calculatrice")
root.geometry("400x500")
root.configure(bg="#808080")
affichage = tk.StringVar()

ecran = tk.Entry(root, textvariable=affichage, font=("Arial", 24), bd=10, relief="ridge", justify="right")
ecran.place(x=20, y=20, width=360, height=60)


def bouton_clique(valeur):
 global expression
 expression += str(valeur)
 affichage.set(expression)

def calculer(event=None):
 global expression
 resultat = eval(expression)
 affichage.set(f"{expression} = {resultat}")

root.bind("<Return>", calculer)

for i, label in enumerate(["1", "2", "3"]):
    bouton = tk.Button(root, text=label, width=5, height=2, font=("Arial", 16),
                       command=lambda v=label: bouton_clique(v))
    bouton.place(x=50 + i*80, y=260)


for i, label in enumerate(["4", "5", "6"]):
    bouton = tk.Button(root, text=label, width=5, height=2, font=("Arial", 16),
                       command=lambda v=label: bouton_clique(v))
    bouton.place(x=50 + i*80, y=330)


for i, label in enumerate(["7", "8", "9"]):
    bouton = tk.Button(root, text=label, width=5, height=2, font=("Arial", 16),
                       command=lambda v=label: bouton_clique(v))
    bouton.place(x=50 + i*80, y=400)

for i, label in enumerate(["*", "+", "-","/"]):
    bouton = tk.Button(root, text=label, width=5, height=2, font=("Arial", 16),
                       command=lambda v=label: bouton_clique(v))
    bouton.place(x=310, y=400 - i*70)

egal_btn = tk.Button(root, text="=", width=5, height=2, font=("Arial", 16), command=calculer)
egal_btn.place(x=210, y=190)






root.mainloop()

