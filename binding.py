# načtení modulů
from tkinter import *

# Scope globálních proměnných
counter = 0


# Deklarace funkcí
def increase_value(event):
    global counter
    counter = counter + 1
    label1.config(text=str(counter))


# Vytvoření okna
window = Tk()
window.title("Vazby na události")
window.geometry("100x105")

# Vytvoření widgetů
label1 = Label(window, text="0", width=10)
button1 = Button(window, text="Counter", width=10)

# Umístění widgetů do mřížky
label1.grid(row=0, column=0)
button1.grid(row=1, column=0)

# Svázání události widgetu s funkcí
button1.bind("# TODO zadejte název vstupní událostí, se kterou se má tlačítko propojit", increase_value)

# Otevření okna
window.mainloop()
