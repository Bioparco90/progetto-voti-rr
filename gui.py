from tkinter import *
from typing import Counter
from votesFunctions import *

rowCounter = 1
textList = []
textPercentage = []
textVotes = []
hiddenRemains = []
allDataFromUser = []
totalVotes = 0
singleSeat = 0


# def header():
#     welcomeFrame = Frame(root)
#     header = Label(welcomeFrame, text="Votes Analyzer", font="Helvetica 20 bold", pady=5)
#     welcomeFrame.grid(row=0, column=3)
#     header.grid(row=0, column=0, sticky="W")


def columnNames(myFrame):
    listNameLabel = Label(myFrame, text="Lista")
    listNameLabel.grid(row=0, column=0, sticky="W")

    percentageLabel = Label(myFrame, text="%")
    percentageLabel.grid(row=0, column=1, sticky="W")

    votesLabel = Label(myFrame, text="Voti")
    votesLabel.grid(row=0, column=2, sticky="W")


def newLine(frame):
    placeholder = f"Lista #{rowCounter-1}"

    lastList = len(textList)
    lastPercentage = len(textPercentage)
    lastVotes = len(textVotes)

    textList.append(Entry(frame, width=20, justify=CENTER))
    textList[lastList].insert(0, placeholder)
    textList[lastList].focus_set()
    textList[lastList].grid(row=rowCounter, column=0, sticky="W", padx=5)

    textPercentage.append(Entry(frame, width=5, justify=CENTER))
    textPercentage[lastPercentage].insert(0, "0.0")
    textPercentage[lastPercentage].grid(row=rowCounter, column=1, sticky="W", padx=5)

    textVotes.append(Entry(frame, width=5, justify=CENTER))
    textVotes[lastVotes].insert(0, "0")
    textVotes[lastVotes].grid(row=rowCounter, column=2, sticky="W", padx=5)

    hiddenRemains.append(0)

    addButton = Button(frame, text="+", command=lambda: addNewLine(addButton, submitButton, frame))
    addButton.grid(row=rowCounter, column=3, sticky="W")
    
    submitButton = Button(frame, text="Calcola", command=lambda: submit(addButton, submitButton, frame))
    submitButton.grid(row=rowCounter+1, column=3, sticky="W")


def addNewLine(b, s, frame):
    global rowCounter
    b.grid_forget()
    s.grid_forget()
    rowCounter += 1
    newLine(frame)


def submit(b, s, frame):
    b.grid_forget()
    s.grid_forget()

    global allDataFromUser
    for n in range(len(textList)):
        allDataFromUser.append([textList[n].get(), float(textPercentage[n].get()), int(textVotes[n].get()), hiddenRemains[n]])

    average = 0
    amountList = 0
    totalPercentage = 0
    
    for n in textPercentage:
        totalPercentage += float(n.get())
    
    totalPercentage = int(totalPercentage)
    
    for n in range(len(allDataFromUser)):
        if allDataFromUser[n][2] > 0:
            average += allDataFromUser[n][2]
            amountList += 1

    if allDataFromUser[0][2] > 0 and totalPercentage == 100 and amountList > 0 and average > 0:
        resultsFromData(average, amountList)
        innerCounter = showResults()
        reset(innerCounter)
    else:
        if allDataFromUser[0][2] == 0:
            warningMessage = "Inserisci per primo il partito di cui conosci i voti e "
            errorFrame(warningMessage, frame)
        elif totalPercentage != 100:
            warningMessage = f'Attenzione, la percentuale totale è {totalPercentage}, controlla e '
            errorFrame(warningMessage, frame)
        elif amountList == 0 or average == 0:
            warningMessage = "Inserisci il totale dei voti di almeno un partito e"
            errorFrame(warningMessage, frame) 


def errorFrame(message, frame):
        checkResultsFrame = Frame(root)
        checkResultsFrame.grid(row=rowCounter+1, column=0)
        warning = Label(checkResultsFrame, text=message)
        warning.grid(row=0, column=0)
        
        retryButton = Button(checkResultsFrame, text="riprova", command=lambda: tryAgain())
        retryButton.grid(row=0, column=1)

def tryAgain():
    global rowCounter, textList, textPercentage, textVotes, hiddenRemains, allDataFromUser, totalVotes, singleSeat
    
    for widget in root.winfo_children():
        widget.destroy()
    
    rowCounter = 1
    textList = []
    textPercentage = []
    textVotes = []
    hiddenRemains = []
    allDataFromUser = []
    totalVotes = 0
    singleSeat = 0
    firstFrame = Frame(root)
    firstFrame.grid(row=0, column=0, pady=5, sticky="W")
    columnNames(firstFrame)
    newLine(firstFrame)


def resultsFromData(average, amountList):
    global allDataFromUser, totalVotes, singleSeat

    average /= amountList
    totalVotes = findTotalVotes(allDataFromUser[0][1], average)
    singleSeat = findSingleSeatVotes(totalVotes)
    for n in range(len(allDataFromUser)):
        partyVotes = findPartyVotes(allDataFromUser[n][1], totalVotes)
        allDataFromUser[n][2] = partyVotes
    for n in range(len(allDataFromUser)):
        partyRemains = findPartyRemains(allDataFromUser[n][2], singleSeat)
        allDataFromUser[n][3] = partyRemains

    
def showResults():
    global rowCounter
    localRowCounter = 2

    resultsFrame = Frame(root)
    resultsFrame.grid(row=rowCounter+1, column=0, sticky="W", pady=5)
    
    totalVotesLabel = Label(resultsFrame, text=f"Voti totali: {int(totalVotes)}")
    totalVotesLabel.grid(row=0, column=0, sticky="W")

    singleSeatLabel = Label(resultsFrame, text=f"Voti per seggio: {int(singleSeat)}")
    singleSeatLabel.grid(row=1, column=0, sticky="W")

    listNameLabel = Label(resultsFrame, text="Lista")
    listNameLabel.grid(row=localRowCounter, column=0, sticky="W")

    percentageLabel = Label(resultsFrame, text="%")
    percentageLabel.grid(row=localRowCounter, column=1, sticky="W", padx=5)

    votesLabel = Label(resultsFrame, text="Voti")
    votesLabel.grid(row=localRowCounter, column=2, sticky="W", padx=5)

    remainsLabel = Label(resultsFrame, text="Resti")
    remainsLabel.grid(row=localRowCounter, column=3, sticky="W", padx=5)

    localRowCounter += 1
    for n in range(len(allDataFromUser)):
        name = allDataFromUser[n][0].capitalize()
        percentage = allDataFromUser[n][1]
        votes = int(allDataFromUser[n][2])
        remains = int(allDataFromUser[n][3])
        listName = Label(resultsFrame, text=name)
        listName.grid(row=localRowCounter, column=0, sticky="W")
        listPercentage = Label(resultsFrame, text=percentage)
        listPercentage.grid(row=localRowCounter, column=1, sticky="W", padx=5)
        listVotes = Label(resultsFrame, text=votes)
        listVotes.grid(row=localRowCounter, column=2, sticky="W", padx=5)
        listRemains = Label(resultsFrame, text=remains)
        listRemains.grid(row=localRowCounter, column=3, sticky="W", padx=5)

        localRowCounter += 1

    return localRowCounter


def reset(n):
    resetButton = Button(root, text="Reset", command=lambda: tryAgain())
    resetButton.grid(row=n, column=0)


root = Tk()

root.title("Analizzatore di voti")
root.geometry("350x500")
firstFrame = Frame(root)
firstFrame.grid(row=0, column=0, pady=5, sticky="W")
columnNames(firstFrame)
newLine(firstFrame)

root.mainloop()