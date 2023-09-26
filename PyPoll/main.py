import csv
import os


csvpath = os.path.join('Documents', 'BootCamp', '03-Python', '03-Python', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

total_votes = 0
candidate_votes = {}


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

  
    header = next(csvreader, None)

   
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

       
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

percentage_votes = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = round(percentage, 2)

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentage_votes[candidate]}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


output_file = os.path.join('Documents', 'BootCamp', '03-Python', '03-Python', 'python-challenge', 'PyPoll', 'results.txt')


with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        textfile.write(f"{candidate}: {percentage_votes[candidate]}% ({votes})\n")

    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")
