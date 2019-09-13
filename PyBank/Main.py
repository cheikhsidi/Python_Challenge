#Imorting Modules
import os
import csv

# Creating a path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Opening the CSV file as an object
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # printin the header of my results 
    print("Fanaicial Analysis")
    print("----------------------------------------------------")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Creating empty dictionary and lists where i am going to add my rows data
    data = {}
    profits = []
    months = []
    changes = []
    #Initializing my counter
    i = 1 
   # looping through my table rows and appending my rows into lists
    for row in csvreader:
        profits.append(int(row[1]))
        months.append(row[0])
    # looping through the profil and loss list to claculate the change    
    for i in range(1,len(profits)): 
        changes.append(profits[i] - profits[i-1])
   # Calculating the the average of change and the max and min changes
    Avg_Change = round((sum(changes))/len(changes), 2)
    MAX_profit = (max(changes))
    MIN_profit = (min(changes))
    Total_Months = len(months)
    Total_Profit = (sum(profits))\
    # mapping my months to my changes(dictionary) to extract the months of max and min changes
    data = dict(zip(months[1:], changes))
    
    # looping through my dictionary to extract the months
    for key, value in data.items():
        if value == MAX_profit:
             MAX_Month = key
        elif value == MIN_profit:
            MIN_Month = key

    # Printing my Analysis Results
    print(f"Total Months : {Total_Months}")
    print(f"Total : ${Total_Profit}")
    print(f"Average  Change : ${Avg_Change}")
    print(f"Greatest Increase in Profits : {MAX_Month} (${MAX_profit})")
    print(f"Greatest Decrease in Profits : {MIN_Month} (${MIN_profit})")

# Writing the results to a text file "Analysis.txt"
with open("Analysis.txt", "w+") as Results:
    Results.write(
        "Fanaicial Analysis""\n"
        "----------------------------------------------------""\n"
        f"Total Months : {Total_Months}""\n"
        f"Total : ${Total_Profit}""\n"
        f"Average Change : ${Avg_Change}""\n"
        f"Greatest Increase in Profits : {MAX_Month} (${MAX_profit})""\n"
        f"Greatest Decrease in Profits : {MIN_Month} (${MIN_profit})")
