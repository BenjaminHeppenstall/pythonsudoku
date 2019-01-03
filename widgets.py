from tkinter import *

window = Tk()

entry1 = Text(window, height=1, width=2)
entry1.insert(END, "8")
entry2 = Text(window, height=1, width=2)
entry2.insert(END, "1")
entry3 = Text(window, height=1, width=2)
entry3.insert(END, "5")
entry4 = Text(window, height=1, width=2)
entry4.insert(END, "9")
entry5 = Text(window, height=1, width=2)
entry5.insert(END, "6")
entry6 = Text(window, height=1, width=2)
entry6.insert(END, "2")
entry7 = Text(window, height=1, width=2)
entry7.insert(END, "7")

array = [entry1, entry2, entry3]

for value in array:
	inputValue=value.get("1.0", "end-1c")
	print(inputValue)

window.mainloop()