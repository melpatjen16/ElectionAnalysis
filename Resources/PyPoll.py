#Open data file of election results

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


# 1. Count the total number of votes/records in the file
# 2. Print list of unique values in the candidates list
# 3. Count the number of votes per candidate
# 4. Calculate the percentage of votes for each candidate out of the total votes
# 5. Print the winner of the election with the greatest percentage