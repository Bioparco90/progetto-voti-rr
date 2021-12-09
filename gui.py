from tkinter import *
from votesFunctions import *

rowCounter = 2
textList = []
textPercentage = []
textVotes = []

def header():
    welcomeFrame = Frame(root)
    header = Label(welcomeFrame, text="Votes Analyzer", font="Helvetica 20 bold", pady=5)
    welcomeFrame.grid(row=0, column=4)
    header.grid(row=0, column=0)


def columnNames():
    listNameLabel = Label(root, text="List")
    listNameLabel.grid(row=1, column=0)

    percentageLabel = Label(root, text="%")
    percentageLabel.grid(row=1, column=1)

    votesLabel = Label(root, text="Votes")
    votesLabel.grid(row=1, column=2)


def newLine():
    placeholder = f"Lista #{rowCounter-1}"

    lastList = len(textList)
    lastPercentage = len(textPercentage)
    lastVotes = len(textVotes)

    textList.append(Entry(root, width=20, justify=CENTER))
    textList[lastList].insert(0, placeholder)
    textList[lastList].focus_set()
    textList[lastList].grid(row=rowCounter, column=0, padx=5)

    textPercentage.append(Entry(root, width=5, justify=CENTER))
    textPercentage[lastPercentage].insert(0, "0.0")
    textPercentage[lastPercentage].grid(row=rowCounter, column=1, padx=5)

    textVotes.append(Entry(root, width=5, justify=CENTER))
    textVotes[lastVotes].insert(0, "0")
    textVotes[lastVotes].grid(row=rowCounter, column=2, padx=5)

    addButton = Button(root, text="+", command=lambda: addNewLine(addButton))
    addButton.grid(row=rowCounter, column=3)


def addNewLine(b):
    global rowCounter
    b.grid_forget()
    rowCounter += 1
    newLine()


root = Tk()

root.title("Votes Analyzer RR")
root.geometry("800x600+0+0")

# Have to choose an icon, this is the facebook's icon. 
# For path issues, just add an 'r' before "". Ex: root.iconbitmap(r"fb.ico") 
# root.iconbitmap("fb.ico")

header()
columnNames()
newLine()

root.mainloop()