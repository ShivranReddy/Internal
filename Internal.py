# 91869 & 91867 Assement
# Julie's Party Hire

from tkinter import *
from tkinter import ttk

root = Tk()
def callback():
    val1 = entry.get()
    val2= entry2.get()
    print ( "Customers Full Name:" + val1)
    print("Customers Recipet Number:" + val2)
    if chvar.get() ==1:
        print("Ballons ")

    
# Create the title / label
lbltitle = ttk.Label(root, text="Julie's Party Hire" , font= (("Arial"), 32))
lbltitle.grid ( row = 0 , column = 3 , columnspan = 2 )


#### Customer Name ####

#Create an Entry Box for the customer name 
entry= ttk.Entry(root, width= 30 ) 
entry.insert(0, " " )
entry.grid(row=1, column =1)

#Create a label for customer name 
lblname = ttk.Label(text= "Your Full Name:")
lblname.grid(row=1, column=0, sticky=W)



#### Receipt Number  ####

#Create an entry box for the recipt code
entry2= ttk.Entry(root, width = 30)
entry2.insert(0, "        ")
entry2.grid(row=2, column = 1)

#Create a label for receipt number
lblname2 = ttk.Label(text="Receipt Number:")
lblname2.grid(row=2, column=0,sticky = W)


# ###  Update/ Append Details Button Button ####


####  Item Hired  #####

#Create a label for items hired
lblname3=ttk.Label(text=" Item Hired:")
lblname3.grid(row=3, column=0,sticky = W)

#Checkbox for item hired

chvar = StringVar()

cbox= Checkbutton(root, text="Ballons  ", variable =chvar,
                  font="Arial 16").grid(row=3, column=1)

#### Quit Button #####

button2=ttk.Button(text="Quit")
button2.config(command= quit)
button2.grid(row=1, column =5 , sticky = E )


##### Print Details Button ####

button3=ttk.Button(text = " Print Details")
button3.config(command = callback)
button3.grid(row=2, column = 5 , sticky = E ) 


root.geometry("1000x500") # Size of the window
root.mainloop()
