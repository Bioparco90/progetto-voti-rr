from tkinter import *
from functions import *

def submit():
    pass

root = Tk()

root.title("Votes Analyzer RR")
root.geometry("800x600+0+0")

# root.resizable(False, False)
# root.grid_columnconfigure(1, weight=1)


# Have to choose an icon, this is the facebook's icon. 
# For path issues, just add an 'r' before "". Ex: root.iconbitmap(r"fb.ico") 
# root.iconbitmap("fb.ico")

welcomeFrame = Frame(root)
header = Label(welcomeFrame, text="Votes Analyzer", font="Helvetica 20 bold", pady=5)
welcomeFrame.grid(row=0, column=4)
header.grid(row=0, column=0)

listNameLabel = Label(root, text="List")
listNameLabel.grid(row=1, column=0)

percentageLabel = Label(root, text="%")
percentageLabel.grid(row=1, column=1)

votesLabel = Label(root, text="Votes")
votesLabel.grid(row=1, column=2)

textList = Entry(root, width=20, justify=CENTER)
textList.grid(row=2, column=0, padx=5)

textPercentage = Entry(root, width=5, justify=CENTER)
textPercentage.grid(row=2, column=1, padx=5)

textVotes = Entry(root, width=5, justify=CENTER)
textVotes.grid(row=2, column=2, padx=5)

b1 = Button(root, text="Submit", command=submit)
b1.grid(row=2, column=3)



root.mainloop()