from tkinter import *
from votesFunctions import *

count = 2
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
    global count

    lastList = len(textList)
    lastPercentage = len(textPercentage)
    lastVotes = len(textVotes)

    textList.append(Entry(root, width=20, justify=CENTER))
    textList[lastList].grid(row=count, column=0, padx=5)

    textPercentage.append(Entry(root, width=5, justify=CENTER))
    textPercentage[lastPercentage].grid(row=count, column=1, padx=5)

    textVotes.append(Entry(root, width=5, justify=CENTER))
    textVotes[lastVotes].grid(row=count, column=2, padx=5)

    addButton = Button(root, text="+", command=addNewLine)
    addButton.grid(row=count, column=3)

def addNewLine():
    global count
    count += 1
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