# Per ottenere il TOTALE DEI VOTI è sufficiente impostare una proporzione, 
# partendo dai dati conosciuti di uno dei partiti:
# 100 : percentuale = votiTot : votiPartito 

# Supponiamo che "Pippo" abbia ottenuto l' 8.4% e che, secondo i loro calcoli, 
# abbiano ricevuto 27 voti. La proporzione sarebbe così impostata:
# 100 : 8.4 = x : 27 
# ergo il calcolo si svolgerebbe così: (100*27)/8.4 = 321.(decimali vari)
# 321 è il totale dei voti che stavamo cercando.

def findTotalVotes(percentage, partyVotes):
    # if percentage == 0:
    #     percentage = 1
    return (100*partyVotes)/percentage

# A questo punto possiamo ottenere i voti ricevuti da tutti gli altri partiti(1), 
# nonchè il limite di voti per ottenere un singolo seggio (2) e infine i dati sui resti (3).

#1
def findPartyVotes(percentage, totVotes):
    return (percentage*totVotes)/100

#2
def findSingleSeatVotes(totVotes):
    return totVotes/12

#3
def findPartyRemains(partyVotes, singleSeatLimit):
    return partyVotes % singleSeatLimit


# ---------debug--------- #
# votesPPM = 48
# percentagePPM = 16.9
# percentageEnigma = 42.7

# tot = findTotalVotes(percentagePPM, votesPPM)
# singleSeat = findSingleSeatVotes(tot)
# votesEnigma = findPartyVotes(percentageEnigma, tot)
# remainsPPM = findPartyRemains(votesPPM, singleSeat)
# remainsEnigma = findPartyRemains(votesEnigma, singleSeat)

# print("Total votes\t\t:", tot)
# print("Single seat\t\t:", singleSeat)
# print("PPM\t\t\t:", votesPPM)
# print("Enigma\t\t\t:", votesEnigma)
# print("Remains PPM\t\t:", remainsPPM)
# print("Remains Enigma\t\t:", remainsEnigma)



