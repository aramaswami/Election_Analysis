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

#Open election results and read the file
with open(file_to_load) as election_data:

#use csv reader to read file that was opened; file_reader is a temp file in memory
    file_reader=csv.reader(election_data)
    header=next(file_reader)
    print(header)


with open(file_to_save,"w") as election_analysis:
    election_analysis.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")

