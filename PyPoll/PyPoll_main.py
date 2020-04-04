#Step 1 Import dependencies
import csv
import os

#Step 2 Bring in two files – election data and election analysis
load_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "election_analysis.txt")

#Step 3 Create variables
total_votes=0
candidate_options=[] 
candidate_votes={}
candidate_name=[]
candidate_winner=[]
candidate_winner_counts=0
percent=[]

#Step 4 Open election data file and convert to list of dictionaries
with open(load_file) as election_data:
    reader = csv.reader(election_data)

    #Step 5 Extract first row
    header = next(reader)
    for row in reader:

        #Step 6 Add to total vote count
        total_votes = total_votes + 1
    
        #Step 7 Extract the candidate name from each row
        candidate_name = row[2]

        #Step 8 Calculate winning vote and candidate
        if candidate_name in candidate_votes.keys():
            candidate_votes[candidate_name]= candidate_votes[candidate_name]+1

        else :
            candidate_votes[candidate_name]=1
with open(output_file, "w") as txt_file:

#Step 9 Calculate percent of votes for each candidate        
    for i in candidate_votes:
        percent=round((float(candidate_votes[i])/total_votes)*100, 2)
        print(f" {i} : %{percent} ({candidate_votes[i]})")
        
        #Step 10 Calcuate percent and create output file
        percent_data=(
            f"election_result\n"
            f"Total Votes: {total_votes}\n"
            f" {i} : %{percent} ({candidate_votes[i]})"
        )
        txt_file.write(percent_data)
    
    #Step 11 Determine candidate winner and total votes
    for key in candidate_votes.keys():
        if candidate_votes[key]==max(candidate_votes.values()):
            winner=key
    print(f"winner is {winner}")
    print (total_votes)

    winner_summary=(f"Winner: {winner}\n")

    # Step 12 Print results and output to text file and terminal
    txt_file.write(winner_summary)
   
    
    
  
              
  
