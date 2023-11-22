from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

window = Tk()

window.geometry("345x320")
window.title("CurrencyConverter")
window.resizable(height=FALSE, width=FALSE)

top = Frame(window, width=300, height=60, bg="blue")
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg="white")
main.grid(row=1, column=0)


header = Label(top, text="WORLD CURRENCY CONVERTER", height=3, pady=5, padx=75, bg="blue", anchor=CENTER,
               font=("Times New Roman", 10), fg="black")
header.pack()

apiKey = "aa5ce13c4947944e04343f52"


# Function to get value inputs
def converter():
    this = myEntry1.get()
    that = myEntry2.get()

    # Api call
    try:
        url = f"https://v6.exchangerate-api.com/v6/{apiKey}/pair/{this}/{that}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            Exchange_Rate = data['conversion_rate']
            Amount = Exchange_Rate * int(myEntry3.get())  # get the value input and multiply it by the exchange rate
            resultBox.configure(text=Amount)
    except:

        errorMsg.configure(text='Something went wrong')
        print('error')



errorMsg = Label(main, text="", height=1, pady=2, padx=75, bg='white', anchor=CENTER,
               font=("Times New Roman", 10), fg="red")
errorMsg.place(x=1, y=20)

# From
this = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW,
             font=("Times New Roman", 10), bg="white", fg="black")
this.place(x=48, y=50)
myEntry1 = Entry(main, width=8, justify=CENTER, relief="solid", font=("Times New Roman", 12))
myEntry1.place(x=50, y=75)

# To
that = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NE, font=("Times New Roman", 10),
             bg="white", fg="black")
that.place(x=158, y=50)
myEntry2 = Entry(main, width=8, justify=CENTER, relief="solid", font=("Times New Roman", 12))
myEntry2.place(x=160, y=75)

# Value From
insert = Label(main, text="Value From", width=8, height=1, pady=0, padx=2, relief="flat", anchor=NE,
               font=("Times New Roman", 10), bg="white", fg="black")
insert.place(x=50, y=105)
myEntry3 = Entry(main, width=8, justify=CENTER, relief="solid", font=("Times New Roman", 12))
myEntry3.place(x=52, y=135)

# Result
resultBox = Label(main, text=" ", width=8, height=1, pady=0, padx=0, relief="solid", anchor=NE,
                  font=("Times New Roman", 15), bg="white", fg="black")
resultBox.place(x=160, y=135)

button = Button(main, text="Convert", width=19, padx=5, anchor=CENTER, height=1, bg="blue", fg="Black",
                font=("Times New Roman", 15), command=converter)
button.place(x=50, y=210)

window.mainloop()
