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

# Add a variable to load a file from a path (Set path for file).
budget_source = os.path.join("PyBank","Resources", "budget_data.csv")
# Add a variable to save the file to a path (Specify the file to write to).
financial_analysis = os.path.join("PyBank","analysis", "financial_analysis.txt")

# Initialize Variables and List:
totalmonths = 0
totalpybank=0
Profitnet=[]
ProfitChange=[]
date=[]

# Read the .csv
with open(budget_source) as budget_data:
    money = csv.reader(budget_data)

    # Read the money
    header = next(money)

    # For each row in the CSV file.
    for row in money:
        ProfitLoss=int(row[1])
        # Total PyBank ($)
        totalpybank += ProfitLoss
        # Add to the total month count
        totalmonths += 1
        # Define List Out of Profit/Losses Column
        Profitnet.append(ProfitLoss)
        # Define List Out of Date Column
        date.append(row[0])

# Making fist for Profit/Losses change over entire period
for i in range(len(Profitnet)-1):
    ProfitChange.append(Profitnet[i+1]-Profitnet[i])
# Calculating Average / Max / Min change and looking for rele​vant date
AverageChange=round(sum(ProfitChange)/len(ProfitChange),2)
GreatestIncrease=max(ProfitChange)
GreatestIncreaseMonth=str(date[ProfitChange.index(GreatestIncrease) + 1])
GreatestDecrease=min(ProfitChange)
GreatestDecreaseMonth=str(date[ProfitChange.index(GreatestDecrease) + 1])

# Print and Save Analysis 
with open(financial_analysis, "w") as txtfile:
    # Print to the TERMINAL
    Financial_Analysis_Report = (
        f"\nFinancial Analysis\n"
        f"\n----------------------------------------------------------\n"
        f"\nTotal Month: {totalmonths}\n"
        f"\nTotal: ${totalpybank}\n"
        f"\nAverage Change: ${AverageChange}\n"
        f"\nGreatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})\n"
        f"\nGreatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})\n"
        f"\n")
    print(Financial_Analysis_Report, end="")
    
    # Save in .txt file
    txtfile.write(Financial_Analysis_Report)
