'''
Program made in: 16/04/2020
Athors: Misha08, OrangoMango
Language: Python 3 Tkinter
'''

from tkinter import *
main = Tk()
main.title("Calculator")
def clear():
  label["text"] = ""

def insert(num):
  current_text = label["text"]
  if len(current_text) != 19:
    label["text"] = current_text + str(num)
  else:
    label["text"] = "Too long"

def delete():
  current_text = label["text"]
  out = list(current_text)
  del out[-1]
  string = ""
  for i in out:
    string += i
  label["text"] = string
  
def calculate():
  current_text = str(label["text"])
  try:
    out = eval(current_text)
  except:
    out = "Error"
  label["text"] = str(out)

label = Label(main, text="")
label.grid(column=0, row=0, columnspan=4)
#numbers
one = Button(main, text="1", command=lambda: insert(1)).grid(column=0, row=2)
two = Button(main, text="2", command=lambda: insert(2)).grid(column=1, row=2)
three = Button(main, text="3", command=lambda: insert(3)).grid(column=2, row=2)
four = Button(main, text="4", command=lambda: insert(4)).grid(column=0, row=3)
five = Button(main, text="5", command=lambda: insert(5)).grid(column=1, row=3)
six = Button(main, text="6", command=lambda: insert(6)).grid(column=2, row=3)
seven = Button(main, text="7", command=lambda: insert(7)).grid(column=0, row=4)
eight = Button(main, text="8", command=lambda: insert(8)).grid(column=1, row=4)
nine = Button(main, text="9", command=lambda: insert(9)).grid(column=2, row=4)
null = Button(main, width=7, text="0", command=lambda: insert(0)).grid(column=0, row=5, columnspan=2)
#operations
minus = Button(main, text="-", command=lambda: insert("-")).grid(column=3, row=3)
multiply = Button(main, text="*", command=lambda: insert("*")).grid(column=2, row=1)
add = Button(main, text="+", command=lambda: insert("+")).grid(column=3, row=2)
divide = Button(main, text="/", command=lambda: insert("/")).grid(column=3, row=1)
clear= Button(main, text="C", command=clear).grid(column=0, row=1)
delete = Button(main, text="DEL", command=delete).grid(column=1, row=1)
#equal
equal = Button(main, height=3, text="=", command=calculate).grid(column=3, row=4, rowspan=2)
#dot
dot = Button(main, text=".", command=lambda:insert(".")).grid(column=2, row=5)
main.mainloop()
