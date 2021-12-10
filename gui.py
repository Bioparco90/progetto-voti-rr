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

    addButton = Button(root, text="+", command=lambda: addNewLine(addButton, submitButton))
    addButton.grid(row=rowCounter, column=3)
    
    submitButton = Button(root, text="Submit", command=lambda: submit(addButton, submitButton))
    submitButton.grid(row=rowCounter+1, column=3)


def addNewLine(b, s):
    global rowCounter
    b.grid_forget()
    s.grid_forget()
    rowCounter += 1
    newLine()


def submit(b, s):
    b.grid_forget()
    s.grid_forget()
    check(b, s)

def check(b, s):
    totalPercentage = 0
    
    for n in textPercentage:
        totalPercentage += float(n.get())

    warningMessage = f'Warning, the total percentage is {totalPercentage}, please check and try again'

    if totalPercentage != 100:
        resultsFrame = Frame(root)
        resultsFrame.grid(row=rowCounter+1, column=4)
        warning = Label(resultsFrame, text=warningMessage)
        warning.grid(row=0, column=0)
        
        retryButton = Button(resultsFrame, text="try again", command=lambda: tryAgain())
        retryButton.grid(row=0, column=1)
    # print(totalPercentage) #debug print

def tryAgain():
    global rowCounter, textList, textPercentage, textVotes
    
    for widget in root.winfo_children():
        widget.destroy()
    
    rowCounter = 2
    textList = []
    textPercentage = []
    textVotes = []
    header()
    columnNames()
    newLine()


root = Tk()

root.title("Votes Analyzer RR")
root.geometry("800x600+0+0")

header()
columnNames()
newLine()

root.mainloop()