#Imorting Modules
import os
import csv

#Creating a path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Opening the CSV file as an object
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #printin the header of my results 
    print("Fanaicial Analysis")
    print("----------------------------------------------------")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Creating empty dictionary where i am going to add my rows
    data = {}
    
    # Read each row of data after the header and creating dictionary out of it
    for row in csvreader:
        data.update({row[0]: int(row[1])})
    #Calculating the SUM and Lenght of my dictionary values
    Total = sum(data.values())
    count = len(data)
    #Calculating the average changes 
    Avg_Change = round(((list(data.values())[-1] - list(data.values())[0])/count), 3)
    #Getting the Maximum value in my Values
    MAX_profit = (max(data.values()))
    #Finding the correspocding month of my maximum value
    MAX_Months = [key for key, value in data.items() if value == MAX_profit]

    for key in MAX_Months:
        MAX_Month = key
    #Getting the Minimum value in my Values
    MIN_profit = (min(data.values()))
    #Finding the correspocding month of my minimum value
    MIN_Months = [key for key, value in data.items() if value == MIN_profit]

    for key in MIN_Months:
        MIN_Month = key
    # Printing my Analysis Results
    print(f"Total Months : {count}")
    print(f"Total : ${Total}")
    print(f"Average  Change : ${Avg_Change}")
    print(f"Greatest Increase in Profits : {MAX_Month} (${MAX_profit})")
    print(f"Greatest Decrease in Profits : {MIN_Month} (${MIN_profit})")

# Writing the results to a text file  
with open("Analysis.txt", "w+") as Results:
    Results.write(
        "Fanaicial Analysis" "\n"
        "----------------------------------------------------""\n"
        f"Total Months : {count}""\n"
        f"Total : ${Total}""\n"
        f"Average Change : ${Avg_Change}""\n"
        f"Greatest Increase in Profits : {MAX_Month} (${MAX_profit})""\n"
        f"Greatest Decrease in Profits : {MIN_Month} (${MIN_profit})")

   
   

