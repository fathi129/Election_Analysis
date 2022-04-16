# -*- coding: UTF-8 -*-
# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join ("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
county= []
county_votes = {}
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county_count = 0
winning_county = ""
# 2: Track the largest county and county voter turnout.
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader: 
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]  
        if candidate_name not in candidate_options:  
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        if county_name not in county: 
            county.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name]+=1

with open(file_to_save, "w") as txt_file:
#     # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results) 
    for county_name in county_votes:
         votes_county = county_votes[county_name]   
         votes_county_perc = float(votes_county)/float(total_votes) * 100        
         county_result = (f"{county_name}: {votes_county_perc:.1f}% ({votes_county:,})\n")
         print(county_result)
         txt_file.write(county_result)
         if(votes_county > winning_county_count):
             winning_county_count = votes_county
             winning_county = county_name
    winning_county_summary = (
    f"\n"    
    f"--------------------------------\n"
    f"Largest County Turnout: {winning_county}\n" 
    f"--------------------------------\n\n"   
    )         
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

#         # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

#     # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

#     # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
