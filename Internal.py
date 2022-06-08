# 91869 & 91867 Assement
# Julie's Party Hire

from tkinter import *
from tkinter import ttk

root = Tk()
def callback():
    val1 = entry.get()
    print("Customer Name " + val1)
    Intval2= entry.get()
    print("Receipt Number " + Intval2)

# Create the title / label
lbltitle = ttk.Label(root, text="Julies Party Hire" , font= (("Arial"), 22))
lbltitle.grid ( row = 0 , column = 0 , columnspan = 2 )


#Customer Name Code

#Create an Entry Box for the customer name 
entry= ttk.Entry(root, width= 30 )
entry.insert(0, "       " )
entry.grid(row=1, column =1)

#Create a label for customer name 
lblname = ttk.Label(text= "Your Full Name:")
lblname.grid(row=1, column=0, sticky=W)
button.grid(row=3, column=1, sticky=W+E, pady=5)

#Receipt Number Code
entry= ttk.Entry(root, witdh = 30)
entry.insert(0, "        ")
entry.grid(row=2, column = 1)

#Create a label for receipt number
