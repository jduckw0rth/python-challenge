import os
import csv

# get the real path of the current file
code_file_path = os.path.realpath(__file__)  
subfolder = 'Resources'
file_name = 'budget_data.csv'
file_path = os.path.join(os.path.dirname(code_file_path), subfolder, file_name)

# get data from Resources folder
pyBank_csv = file_path

# open the file in read mode
file = open(pyBank_csv)

# creating dictreader object
pyBank = csv.DictReader(file)

# creating empty lists
pyBank_date = []
pyBank_profit_losses = []

# iterating over each row and append values to empty list
for col in pyBank:
    pyBank_date.append(col['Date'])
    pyBank_profit_losses.append(col['Profit/Losses'])


# The total number of months included in the dataset
total_months = len(pyBank_date)

# The net total amount of "Profit/Losses" over the entire period
# change list from string to number

pyBank_profit_losses_int = list(map(float, pyBank_profit_losses))
total_profit_losses = round(sum(pyBank_profit_losses_int),0)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
t = pyBank_profit_losses_int
v = [t[i+1] - t[i] for i in range(len(t)-1)]
avgChange = round(sum(v) / len(v), 2)

# The greatest increase in profits (date and amount) over the entire period
maxIncrease = round(max(v),0)
dateMaxIndex = v.index(maxIncrease)
dateMaxIncrease = pyBank_date[dateMaxIndex + 1]

# The greatest decrease in profits (date and amount) over the entire period
maxDecrease = round(min(v),0)
dateMinIndex = v.index(maxDecrease)
dateMaxDecrease = pyBank_date[dateMinIndex + 1]


# In addition, your final script should both print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", total_months)
print("Total: ", total_profit_losses)
print("Average Change: ", avgChange)
print("Greatest Increase in Profits: ", dateMaxIncrease , "(", maxIncrease, ")")
print("Greatest Decrease in Profits: ", dateMaxDecrease, "(", maxDecrease, ")")



# make a list of the results that need to be printed into the file
results = ["Financial Analysis", "\n", "----------------------------", "\n", "Total Months: ", str(total_months), "\n", "Total: ", str(total_profit_losses), "\n", "Average Change: ", str(avgChange), "\n", "Greatest Increase in Profits: ", str(dateMaxIncrease), "(", str(maxIncrease), ")", "\n", "Greatest Decrease in Profits: ", str(dateMaxDecrease), "(", str(maxDecrease), ")"]

# create and export the text file with the results
save_path = os.path.join(os.path.dirname(code_file_path), 'analysis', 'results.txt')

with open(save_path, 'w') as f:
    f.writelines(' '.join(results))
    f.close()