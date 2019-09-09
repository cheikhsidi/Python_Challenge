import os
import csv

# defining my Election function
def Election_Calculator():
    # retreiving the election csv file path
    file = os.path.join("Resources", "election_data.csv")

    #Opening the file as an object
    with open(file, newline='') as csv_file:
        csvreader = csv.reader(csv_file, delimiter = ",")
        #skipping the header
        csvheader = next(csvreader)

        # defining an empty list to store my candidates in
        candidates = []
        # Initializing my dictionaries for candidates and candid_pourcents
        candid_pourcent = {}
        # Printing & Formatting the Results
        print("Election Results")
        print ("---------------------------")

        # Looping through the candidates column to retrieve all candidates
        for row in csvreader:
            candidates.append(row[2])
            #Creating a dictionary of candidates and total votes
            candid_votes = dict(zip(candidates, [0] * len(candidates)))
            # looping through the list of candidates to count each candidate
            for v in candidates:
                candid_votes[v] += 1

        #Calculating Total votes 
        Total_Votes = len(candidates)
        print(f"Total Votes : {Total_Votes}")
        print("---------------------------")

        # Calculating the pourcentage of each candidate and appending the value to the pourcent dictionary
        for k,v in candid_votes.items():
            value = v
            v = (v/Total_Votes)*100
            #formatting my pourcentages to 3 point decimal
            v = float("{0:.3f}".format(v))
            candid_pourcent[k] = v
            print(f"{k} : %{v} ({value})")

        # Retreiving the winner using the max function
        winner = max(candid_pourcent, key=candid_pourcent.get)
        print("---------------------------")
        print (f"winner : {winner}")
        print("---------------------------")

Election_Calculator()
