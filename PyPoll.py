#The data we need to retrieve
#Names of candidates
#Votes for each candidate
#Total votes cast
#Percent of votes for each candidate
#Winner of the election based on popular vote

import csv
import os
#Load file with input data using indirect file reference
file_to_load=os.path.join("Resources","election_results.csv")
#load file for output using indirect file reference
file_to_save=os.path.join("analysis","election_analysis.txt")

#Initialize vote counter, candidate list, votes by candidate dictionary
total_votes=0
candidate_list=[]
candidate_votes={}

#Initialize values for winner, wining votes, and winning %
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read the file
with open(file_to_load) as election_data:

#use csv reader to read file that was opened; file_reader is a temp file in memory
    file_reader=csv.reader(election_data)
#Exclude first row
    header=next(file_reader)

#Add total_votes, create candidate list, create candidate_votes dict
    for row in file_reader:
        total_votes=total_votes+1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes[row[2]]=0
        candidate_votes[row[2]]+=1

with open(file_to_save, "w") as election_analysis:
    election_results= (f"Election Results\n------------------------\nTotal votes: {total_votes:,}\n------------------------\n")
    print(election_results)
    election_analysis.write(election_results)

    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percentage=int(votes)/int(total_votes)*100
#Determine winner, winning votes, and winning%
        if (votes>winning_count):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate
#Print each candiate with vote share and count
        candidate_results=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        election_analysis.write(candidate_results)
#Print winning candidate and related stats
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    election_analysis.write(winning_candidate_summary)