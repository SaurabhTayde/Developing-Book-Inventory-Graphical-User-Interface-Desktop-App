"""
(Refer to images named 'Raw sketch' and 'Grid' to get idea of what we need to build)
A program that stores this book information:
Title, Author
Year, ISBN

User should be able to do following:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

"""
To make GUI with Tkinter we can use 'Pack Method' to pack your widgets or 'Grid Method'.
We will be using grid method
"""

from tkinter import *

window =  Tk()

l1 = Label(window, text = 'Title')
l1.grid(row = 0, column = 0)

l2 = Label(window, text = 'Author')
l2.grid(row = 0, column = 2)

l3 = Label(window, text = 'Year')
l3.grid(row = 1, column = 0)

l4 = Label(window, text = 'ISBN')
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 5, width = 35)
list1.grid(row=2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = 'View All', width = 12)
b1.grid(row=2, column=3)

b2 = Button(window, text = 'Search entry', width = 12)
b2.grid(row=3, column=3)

b3 = Button(window, text = 'Add entry', width = 12)
b3.grid(row=4, column=3)

b4 = Button(window, text = 'Update selected', width = 12)
b4.grid(row=5, column=3)

b5 = Button(window, text = 'Delete selected', width = 12)
b5.grid(row=6, column=3)

b6 = Button(window, text = 'Close', width = 12)
b6.grid(row=7, column=3)

window.mainloop()
