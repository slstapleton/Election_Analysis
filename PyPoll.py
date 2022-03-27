# The data we need to retrieve.

# 1. The total number of votes castwon
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate 
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
# Winning Candidate, Winning Count, Winning Percentage Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1        
        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add to the candidate list
        if candidate_name not in candidate_options:
            # Add candidate name to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #  Print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Determine winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print winning candidates' results in terminal    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.

        # Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Print the candidate votes.
    #print(candidate_votes)

    # Print the total votes.
    # print(total_votes)

        #print(election_data)

    # Using the open() function with the "w" mode we will write data to the file.
    #with open(file_to_save, "w") as txt_file:

        # Write three counties to the file.
        #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

