
import csv
import os


csvpath = os.path.join('Documents','BootCamp','03-Python','03-Python','python-challenge', 'PyBank', 'Resources','budget_data.csv')



total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 
    for row in csvreader:
    
        date = row[0]
        profit_loss = int(row[1])

        
        total_months += 1

        
        total_profit_loss += profit_loss

        
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(date)

      
        previous_profit_loss = profit_loss


average_change = sum(profit_loss_changes) / len(profit_loss_changes)


max_increase = max(profit_loss_changes)
max_decrease = min(profit_loss_changes)


max_increase_date = months[profit_loss_changes.index(max_increase)]
max_decrease_date = months[profit_loss_changes.index(max_decrease)]


print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")


output_file = 'financial_analysis.txt'
with open(output_file, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total Profit/Loss: ${total_profit_loss}\n")
    f.write(f"Average Change: ${average_change:.2f}\n")
    f.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    f.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

print("Results saved to", output_file)

