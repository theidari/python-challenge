# Dependencies:
import csv, os, subprocess, platform

# Cleaning Terminal Before Run:
if platform.system()=="Windows":
    if platform.release() in {"10", "11"}:
        subprocess.run("", shell=True) 
        print("\033c", end="")
    else:
        subprocess.run(["cls"])
else: 
    print("\033c", end="")

#------------------------------------Main Part--------------------------------------------

# Add a variable to load a file from a path.
election_source = os.path.join("PyPoll","Resources", "election_data.csv")
# Add a variable to save the file to a path.
election_analysis = os.path.join("PyPoll","analysis", "election_analysis.txt")

# Initialize Variables and List:
TotalVotes = 0
WinningCount = 0
WinningPercentage = 0
WinningCandidate = ""
CandidateOptions = []
CandidateResults = []
CandidateVotes = {}

# Read the .csv
with open(election_source) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Total Vote Count
        TotalVotes += 1
        # Define the candidate name.
        CandidateName = row[2]
        # Check Candidate Name In List For Making Candidate List
        if CandidateName not in CandidateOptions:
            # Add the Candidate Name to the Candidate List.
            CandidateOptions.append(CandidateName)
            # Candidate's Voter Count.
            CandidateVotes[CandidateName] = 0
        # Total Vote Count For Each Candidate and Create Dictionary
        CandidateVotes[CandidateName] += 1

    # Recover Vote Count and Percentage
    for CandidateName in CandidateVotes:

        Votes = CandidateVotes.get(CandidateName)
        VotePercentage = float(Votes) / float(TotalVotes) * 100
        CandidateIndevidualResults = (
            f"{CandidateName}: {VotePercentage:.3f}% ({Votes:,})")
        #Making List Out of the Result:
        CandidateResults.append(CandidateIndevidualResults)

        # Determine Winner.
        if (Votes > WinningCount) and (VotePercentage > WinningPercentage):
            WinningCount = Votes
            WinningCandidate = CandidateName
# Recreate List for Print
CandidateList='\n'.join(map(str, CandidateResults))


# Print and Save Analysis.
with open(election_analysis, "w") as txtfile:

    # Print to the TERMINAL
    Election_Results_Report = (
        f"\nElection Results\n"
        f"\n--------------------------------------------\n"
        f"\nTotal Votes: {TotalVotes:,}\n"
        f"\n--------------------------------------------\n\n"
        # list
        f"{CandidateList}\n"
        # winner
        f"\n--------------------------------------------\n"
        f"\nWinner: {WinningCandidate}\n"
        f"\n--------------------------------------------\n"
        f"\n")
    print(Election_Results_Report, end="")

    # Save in .txt file
    txtfile.write(Election_Results_Report)
