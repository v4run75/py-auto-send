import json
import tkinter
from tkinter import *



window = tkinter.Tk()
window.title("PyBot")
# lbl = Label(window, text="Hello")

lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!")


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

window.geometry('350x200')

window.mainloop()

obj = json.loads("""{
  "firstName": "Alice",
  "lastName": "Hall",
  "age": 35
}""")

firstName = obj["firstName"]
lastName = obj["lastName"]
age = obj["age"]

print(firstName)
print(lastName)
print(age)

print(obj)
