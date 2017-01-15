
"""
Jednoducha aplikace, ktera pocita zakladni operace se zlaomky
Pro UI byl pouzit Tkinter
"""

from Tkinter import *
from zlomky import Zlomek
   
root = Tk()
root.title(u"Kalkulator zlomku")
root.geometry("500x400")


frame = Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

lhsEntry = StringVar()
lhsText = StringVar()
lhsText.set("1/1")
lhsZlomek = Zlomek()
rhsEntry = StringVar()
rhsText = StringVar()
rhsText.set("1/1")
rhsZlomek = Zlomek()
operator = IntVar()
operator.set(1)
expression = StringVar()
result = StringVar()
OPERATORS = {1:'+', 2:'-', 3:'*', 4:'I'}

def processLhsEntry(*args):
    global lhsZlomek
    try:
        entry = lhsEntry.get()
        zlomek = entry.split("/")
        citatel = int(zlomek[0])
        jmenovatel = int(zlomek[1])
        lhsZlomek = Zlomek(citatel, jmenovatel)
        lhsText.set(lhsZlomek)
    except ValueError:
        lhsText.set(u"Zadej zlomek lamo!")
    except IndexError:
        lhsText.set(u"Zadej zlomek lamo!")

    lhsEntry.set("")

def processRhsEntry(*args):
    global rhsZlomek
    try:
        entry = rhsEntry.get()
        zlomek = entry.split("/")
        citatel = int(zlomek[0])
        jmenovatel = int(zlomek[1])
        rhsZlomek = Zlomek(citatel, jmenovatel)
        rhsText.set(rhsZlomek)
    except ValueError:
        rhsText.set(u"Zadej zlomek lamo!")
    except IndexError:
        lhsText.set(u"Zadej zlomek lamo!")

    rhsEntry.set("")

def calculateClick(*args):
    try:
        opNum = operator.get()
        opSym = OPERATORS[opNum]
        expression.set("{0} {1} {2}".format(lhsZlomek, opSym, rhsZlomek))
        if opNum == 1:
            result.set(lhsZlomek + rhsZlomek)
        elif opNum == 2:
            result.set(lhsZlomek - rhsZlomek)
        elif opNum == 3:
            result.set(lhsZlomek * rhsZlomek)
        else:
            result.set(lhsZlomek / rhsZlomek)
    except ValueError:
            result.set("Not defined")
        

Label(frame, text="lhsZlomek (citatel/jmenovatel)").grid(column=0, row=0, sticky=W)
lhs_entry = Entry(frame, width=7, textvariable=lhsEntry)
lhs_entry.grid(column=0, row=1, sticky=(W, E))
Label(frame, textvariable=lhsText).grid(column=0, row=2, sticky=(W,E))

Label(frame, text="rhsZlomek (citatel/jmenovatel)").grid(column=2, row=0, sticky=W)
rhs_entry = Entry(frame, width=7, textvariable=rhsEntry)
rhs_entry.grid(column=2, row=1, sticky=(W, E))
Label(frame, textvariable=rhsText).grid(column=2, row=2, sticky=(W,E))

Label(frame, text="Zvol operator").grid(column=1, row=1, sticky=W)
Radiobutton(frame, text="Soucet", variable=operator, value=1).grid(column=1, row=2, sticky=W)
Radiobutton(frame, text="Rozdil", variable=operator, value=2).grid(column=1, row=3, sticky=W)
Radiobutton(frame, text="Soucin", variable=operator, value=3).grid(column=1, row=4, sticky=W)
Radiobutton(frame, text="Podil", variable=operator, value=4).grid(column=1, row=5, sticky=W)

Button(frame, text=u"Vypočítej", command=calculateClick).grid(column=1, row=6, sticky=W)

Label(frame, text="Vyraz").grid(column=0, row=7, sticky=(W,E))
Label(frame, textvariable=expression).grid(column=1, row=7, sticky=(W,E))

Label(frame, text="Vysledek").grid(column=0, row=8, sticky=(W,E))
Label(frame, textvariable=result).grid(column=1, row=8, sticky=(W,E))

for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)

lhs_entry.focus()
lhs_entry.bind('<Return>', processLhsEntry)
rhs_entry.bind('<Return>', processRhsEntry)

root.mainloop()