from tkinter import Tk, Entry, END, Listbox, Button

#création de la fuente de calculatrice
fenetre = Tk()
fenetre.title("Calculatrice")

#ecran pour afficher les résultat
ecran = Entry(fenetre, width=28, borderwidth=5, font=("Arial", 23))
ecran.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)

#ecran pour sauvegarder les résultats des calcule
history = []
list_history = Listbox(fenetre, width=60, height=4)
list_history.grid(row=7, column=0, padx=10, pady=10, columnspan=5)

#la fonction pour sauvegarde les résultats des calcule
def update_history(calculation):
    history.append(calculation)
    list_history.insert(END, calculation)

#la fonction de bouton pour supprimer l'historique
def clear_history():
    history.clear()
    list_history.delete(0, END)

#la fonction de bouton egale
def button_equal():
    calculation = ecran.get()
    ecran.delete(0, END)
    try:
        result = eval(calculation)
        ecran.insert(0, result)
        update_history(calculation + " = " + str(result))
    except:
        ecran.insert(0, "Vous avez fait une erreur")

#la fonction de bouton click
def button_click(number):
    current = ecran.get()
    ecran.delete(0, END)
    ecran.insert(0, str(current) + str(number))

#la fonction de bouton pour effacer
def button_clear():
    ecran.delete(0, END)

#la fonction de bouton pour effacer le dernier  caractere
def button_clear_last():
    current = ecran.get()
    ecran.delete(len(current)-1, END)


#tout les bouton de la calculatrice
button_1 = Button(fenetre, text="1", width=6, height=3, font=("Arial", 18), command=lambda:button_click('1'))
button_2 = Button(fenetre, text="2", width=6, height=3, font=("Arial", 18), command=lambda:button_click('2'))
button_3 = Button(fenetre, text="3", width=6, height=3, font=("Arial", 18), command=lambda:button_click('3'))
button_4 = Button(fenetre, text="4", width=6, height=3, font=("Arial", 18), command=lambda:button_click('4'))
button_5 = Button(fenetre, text="5", width=6, height=3, font=("Arial", 18), command=lambda:button_click('5'))
button_6 = Button(fenetre, text="6", width=6, height=3, font=("Arial", 18), command=lambda:button_click('6'))
button_7 = Button(fenetre, text="7", width=6, height=3, font=("Arial", 18), command=lambda:button_click('7'))
button_8 = Button(fenetre, text="8", width=6, height=3, font=("Arial", 18), command=lambda:button_click('8'))
button_9 = Button(fenetre, text="9", width=6, height=3, font=("Arial", 18), command=lambda:button_click('9'))
button_0 = Button(fenetre, text="0", width=6, height=3, font=("Arial", 18), command=lambda:button_click('0'))
button_c = Button(fenetre, text="C", width=6, height=3, font=("Arial", 18), bg='Orange', command=lambda:button_clear())
button_plus = Button(fenetre, text="+", width=6, height=3, font=("Arial", 18), command=lambda:button_click('+'))
button_moins = Button(fenetre, text="-", width=6, height=3, font=("Arial", 18), command=lambda:button_click('-'))
button_division = Button(fenetre, text="/", width=6, height=3, font=("Arial", 18), command=lambda:button_click('/'))
button_multiplication = Button(fenetre, text="*", width=6, height=3, font=("Arial", 18), command=lambda:button_click('*'))
button_porsontage = Button(fenetre, text="%", width=6, height=3, font=("Arial", 18), command=lambda:button_click('/100'))
button_e = Button(fenetre, text="=", width=14, height=3, font=("Arial", 18), bg='green', command=lambda:button_equal())
button_aucaree = Button(fenetre, text="x\U000000B2", width=6, height=3, font=("Arial", 18), command=lambda:button_click('**2'))
button_racine = Button(fenetre, text="\U0000221A", width=6, height=3, font=("Arial", 18), command=lambda:button_click('**0.5'))
button_back = Button(fenetre, text="\U0000232B", width=6, height=3, font=("Arial", 18), command=button_clear_last)
button_parenthese = Button(fenetre, text=")", width=6, height=3, font=("Arial", 18), command=lambda:button_click(')'))
button_parenthese1 = Button(fenetre, text="(", width=6, height=3, font=("Arial", 18), command=lambda:button_click('('))
button_point = Button(fenetre, text=".", width=6, height=3, font=("Arial", 18), command=lambda:button_click('.'))
button_puissance = Button(fenetre, text="x\U000002E3", width=6, height=3, font=("Arial", 18), command=lambda:button_click('**'))
button_pi = Button(fenetre, text="\U000003C0", width=6, height=3, font=("Arial", 18), command=lambda:button_click('3.14159265359'))
supprimer_lhistorique = Button(fenetre, text="supprimer l'historique", bg='red', font=("Arial", 18), command=clear_history)

#les emplacement des bouton
#ligne 1
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_puissance.grid(row=1, column=3)
button_c.grid(row=1, column=4)


#ligne 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_plus.grid(row=2, column=3)
button_back.grid(row=2, column=4)

#ligne 3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_moins.grid(row=3, column=3)

#ligne 4
button_0.grid(row=4, column=0)
button_division.grid(row=4, column=1)
button_multiplication.grid(row=4, column=2)
button_porsontage.grid(row=4, column=3)

#ligne 5
button_aucaree.grid(row=5, column=1)
button_racine.grid(row=5, column=0)
button_point.grid(row=5, column=3)
button_pi.grid(row=5, column=2)

#ligne 6
button_parenthese1.grid(row=6, column=2)
button_parenthese.grid(row=6, column=3)
button_e.grid(row=6, column=0, columnspan=2,)

#ligne 8
supprimer_lhistorique.grid(row=8, column=0, columnspan=4)

#l'affichage de calculatrice
fenetre.mainloop()

