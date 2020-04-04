#Step 1: import CSV – budget data
import csv
import os

budget_file=os.path.join('Resources', 'budget_data.csv')

# Step 2: create variables to be used 
total_months = 0
net_change = 0
net_change_lst = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999]
total_months_lst=[]
total_net=0

#Step 3: convert CSV to list of dictionaries 
with open(budget_file) as budget_data:
    reader = csv.reader(budget_data)

    #Step 4: extract first row
    header=next(reader) 
    first_row=next(reader)
    total_months=total_months+1
    total_net=total_net + int(first_row[1])
    prev_net=int(first_row[1])
    for row in reader:

        #calcuate total months
        total_months=total_months+1
        total_net =total_net + int(row[1])

        #calculate net change
        net_change=int(row[1])-prev_net
        prev_net=int(row[1])
        net_change_lst=net_change_lst+[net_change]
        total_months_lst=total_months_lst+[row[0]]

        #calculate greatest increase
        if net_change>greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change

        #calculate greatest decrease
        if net_change<greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change

#calculate average net change
average_net_change=sum(net_change_lst)/len(net_change_lst)


#produce summary
print(total_months, total_net, average_net_change, greatest_increase[0],greatest_increase[1], greatest_decrease[0], greatest_decrease[1])


#export results to text file
  tText=['total_months', 'total_net', 'average_net_change', 'greatest_increase[0]','greatest_increase[1]', 'greatest_decrease[0]', 'greatest_decrease[1]']
    outfile = open("C:\Users\mpc24\Desktop\personal-data\unc-ral-data-pt-02-2020-u-c.output.txt")
    outfile.writelines(tText)

