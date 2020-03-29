# Election_Analysis
## Project Overview
The task assigned to me is to analyze ballots votes from a recent Colorado election and determine the winner, ie. the candidate with the most number of votes. The raw data that I was provided is a csv file with the actual voting data, by ballot, that had the ballot number, county, and candidate for whom the vote was cast. Given the size of the data set, I wrote Python code to analyze file and determine the results of the election. 

I used the following tools and resources for this assignment:
- Python 3.8
- Visual Studio v1.43.2
- GitBash
- Excel (election results csv file)

## Summary of results
My analysis of election data show the following results

- A total of 369,711 were cast in this election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The results for each candidate is as follows:
  Charles Casper Stockham received 85,213 vtes, which is 23.0% of total votes
  Diana DeGette received 272,892 votres, which is 73.8% of total votes
  Raymon Anthony Doane received 11,606 votes, which is 3.1% of total votes

- The election result is:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

(Please note that I provided the election_analysis.txt file as part of this assignment.)

## Challenge oveview
We analyzed election results by candidate but that does not provide a complete picture of voter participation. It is also important to understand the vote totals by county. I added code that would total votes by county and determine the county with the largest number of votes. I also added the summary of votes by county to my election analysis text file.

## Challenge Summary
Following is a summary if the results I determined from the running the code with changes for this challenge. As you will recall from our earlier analysis, the total votes cast in the election is 369,711. A county-wise breakdown of this is: 

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

This shows that the largest voter turnout was in Denver county.

## Challenge methodology
I'd like to highlight the specific changes that I made to the code to generate county-based results. The important aspect that I realized is that the code should determine the county with the most voter turnout in the same manner as we determined the candidate with the most votes. Following is a summary of my methodology.
- Initialize a list for counties and a dictionary for votes by county
- Initialize values for lead county, county leader for turnout, vote share %
- Create county list and county_votes dictionary
- Calculate vote % by county
- Determine county leader, #votes, and vote%
- Print and write to txt file, with format, each county with vote share and total      

