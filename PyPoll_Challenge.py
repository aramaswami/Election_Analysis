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

#CHALLENGE:Initialize county list, votes by county dictionary
county_list=[]
county_votes={}

#Initialize values for winner, wining votes, and winning %
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#CHALENGE:Initialize values for lead county, county leader for turnout, vote share %
county_leader = ""
county_leader_vote = 0
county_leader_percentage = 0

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

#CHALLENGE:Create county list and county_votes dictionary
        if row[1] not in county_list:
            county_list.append(row[1])
            county_votes[row[1]]=0
        county_votes[row[1]]+=1

#Open election analysis destination txt file
with open(file_to_save, "w") as election_analysis:
    
#Print and write to txt file the election results
    election_results= (f"Election Results\n------------------------\nTotal Votes: {total_votes:,}\n------------------------\n")
    print(election_results)
    election_analysis.write(election_results)

#CHALLENGE: Calculate vote % by county
    county_print_header=(f"\nCounty Votes:\n")
    print(county_print_header)
    election_analysis.write(county_print_header)
    for county_id in county_votes:
        votes_for_county=county_votes[county_id]
        county_vote_percentage=int(votes_for_county)/int(total_votes)*100

#CHALLENGE:Determine county leader, #votes, and vote%
        if (votes_for_county>county_leader_vote):
            county_leader_vote=votes_for_county
            county_leader_percentage=county_vote_percentage
            county_leader=county_id

#CHALLENGE:Print and write to txt file, with format, each county with vote share and total      
        county_results=(f"{county_id}: {county_vote_percentage:.1f}% ({votes_for_county:,})\n")
        print(county_results)
        election_analysis.write(county_results)

    county_leader_summary=(
        f"\n------------------------\n"
        f"Largest County Turnout: {county_leader}\n"
        f"------------------------\n"
    )
    print(county_leader_summary)
    election_analysis.write(county_leader_summary)

#Calculate vote % by candidate
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percentage=int(votes)/int(total_votes)*100

#Determine winner, winning votes, and winning%
        if (votes>winning_count):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate

#Print and write to txt file, with format, each candiate with vote share and count
        candidate_results=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        election_analysis.write(candidate_results)
#Print and write to txt file the winning candidate and related stats with format
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    election_analysis.write(winning_candidate_summary)

