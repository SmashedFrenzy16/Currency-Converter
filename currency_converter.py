from tkinter import *
from forex_python.converter import CurrencyRates

root = Tk()

root.title("Currency Converter By @SmashdFrenzy16")

c = CurrencyRates()

amount = Entry(root, width=100, borderwidth=5)
amount.pack()
amount.insert(0, "Enter Amount Of Money To Convert")
f_currency = Entry(root, width=100, borderwidth=5)
f_currency.pack()
f_currency.insert(0, "Enter Currency Code To Be Converted")
t_currency = Entry(root, width=100, borderwidth=5)
t_currency.pack()
t_currency.insert(0, "Enter Currency Code To Convert To")

def execute():

    global f_currency

    global t_currency

    ans = c.convert(f_currency.get(), t_currency.get(), float(amount.get()))

    output = Label(root, text=ans)
    output.pack()

submit = Button(root, text = "Enter", command = execute)
submit.pack()


root.mainloop()
