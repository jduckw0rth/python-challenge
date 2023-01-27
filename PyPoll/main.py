import os
import csv

# get the real path of the current file
code_file_path = os.path.realpath(__file__)  
subfolder = 'Resources'
file_name = 'election_data.csv'
file_path = os.path.join(os.path.dirname(code_file_path), subfolder, file_name)

# get data from Resources folder
pyPoll_csv = file_path

# open the file in read mode
file = open(pyPoll_csv)

# creating dictreader object
pyPoll = csv.DictReader(file)

# creating empty lists
pyPoll_voters = []
pyPoll_county = []
pyPoll_candidate = []

# iterating over each row and append values to empty list
for col in pyPoll:
    pyPoll_voters.append(col['Ballot ID'])
    pyPoll_county.append(col['County'])
    pyPoll_candidate.append(col['Candidate'])

# The total number of votes cast
totalVotes = len(pyPoll_voters)


# A complete list of candidates who received votes - find unique values from candidate list

def unique(candidateList):
    # make empty list
    uniqueCandidates = []

    # go through elements of list
    for x in candidateList:
        if x not in uniqueCandidates:
            uniqueCandidates.append(x)

candidateList = pyPoll_candidate
unique(candidateList)


# The total number of votes each candidate won
stockhamVotes = sum(1 for i in pyPoll_candidate if i == "Charles Casper Stockham")


degetteVotes = sum(1 for i in pyPoll_candidate if i == "Diana DeGette")


doaneVotes = sum(1 for i in pyPoll_candidate if i == "Raymon Anthony Doane")


# The percentage of votes each candidate won
stockhamPercent = round(stockhamVotes / totalVotes * 100, 3)


degettePercent = round(degetteVotes / totalVotes * 100, 3)


doanePercent = round(doaneVotes / totalVotes * 100, 3)


# The winner of the election based on popular vote
def winner(List):
    return max(set(List), key = List.count)

List = pyPoll_candidate


# In addition, your final script should both print the analysis to the terminal
print("Election Results")
print("----------------------------")
print("Total Votes: ", totalVotes)
print("----------------------------")
print("Charles Casper Stockham: ", stockhamPercent, "% ", "(", stockhamVotes, ")")
print("Diana DeGette: ", degettePercent, "% ", "(", degetteVotes, ")")
print("Raymon Anthony Doane: ", doanePercent, "% ", "(", doaneVotes, ")")
print("----------------------------")
print("Winner: ", winner(List))
print("----------------------------")



# make a list of the results that need to be printed into the file
results = ["Election Results", "\n", "----------------------------", "\n", "Total Votes: ", str(totalVotes), "\n", "----------------------------", "\n","Charles Casper Stockham: ", str(stockhamPercent), "% ", "(", str(stockhamVotes), ")", "\n", "Diana DeGette: ", str(degettePercent), "% ", "(", str(degetteVotes), ")", "\n", "Raymon Anthony Doane: ", str(doanePercent), "% ", "(", str(doaneVotes), ")", "\n","----------------------------", "\n","Winner: ", winner(List), "\n","----------------------------"]

# create and export the text file with the results
save_path = os.path.join(os.path.dirname(code_file_path), 'analysis', 'results.txt')


with open(save_path, 'w') as f:
    f.writelines(' '.join(results))
    f.close()