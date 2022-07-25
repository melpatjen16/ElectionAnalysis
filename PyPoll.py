#Open data file of election results

#1. Add our dependencies.
import csv
import os

#2 Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
#3 Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources", "election_analysis.txt")

# 3. Initiate total variable

total_votes = 0

#4 Candidate Options

candidate_options = []

# 5. Declare the empty dictionary.

candidate_votes = {}

#6 Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#7 Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)


 #8. Print each row in the CSV file.
    for row in file_reader:

#9. Count the total number of votes/records in the file
       
        total_votes += 1

# 10. Print list of unique values in the candidates list

        candidate_name = row[2]

     #11 If the candidate does not match any existing candidate.

        if candidate_name not in candidate_options:
            #12 Add it to the list of candidates.

            candidate_options.append(candidate_name)

            #13. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
 
 #14 Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
  #15 Save the results to our text file.
with open(file_to_save, "w") as txt_file:      

    #16 After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

# Determine the percentage of votes for each candidate by looping through the counts.
 # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)