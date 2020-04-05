#'''
#get existing funds and corresponding (desired) allocations from user input
fund="placeholder"
allocation=0.0
allocations={} #list of funds and corresponding allocations (dictionary)
sum=0.0 #sum of allocations

#loop through as user inputs funds, exit once their allocations add to 100%
#start over if allocations add to more than 100%
while True:
	print("Enter fund names and desired allocation percentage...")
	allocations={} #wipe out allocations for each iteration of the loop
	while sum < 1.0:
		fund=raw_input("fund: ") #was behaving weirdly with regular input here
		allocation=float(input("allocation: "))
		sum+=allocation
		allocations[fund]=allocation #add fund and corresponding allocation to allocations list
	if sum==1.0:
		#we have the allocations, they add to 100%, so we're good! move on
		break
	else:
		#oops, sum of allocations is more than 100%
		sum=0.0 #reset sum so user can start over
		print("error! sum of allocations exceeds 1.0 (100%)")

print("funds entered: "),
print(allocations)

'''
#uncomment this section to prefill out existing allocations (if you don't want to enter every time)
#modify the funds and numbers accordingly in code here if you want to use
#if using this method of inputting allocations, comment out everything above this block
allocations={}
allocations["SWISX"]=.3
allocations["SWTSX"]=.65
allocations["SWAGX"]=.05
'''

#get how much money is currently in each fund
print("Enter how much money is currently in each fund...")
existing_monies={}
total_money=0.0

for key in allocations:
	money=float(input(key+": ")) #prompt for given fund, i.e. "SWISX: "
	existing_monies[key]=money
	total_money+=money
	
print("current money in each fund: ")
print(existing_monies)
print("total money: "+str(total_money))

#get investment amount
input_money=(float(input("amount to invest: ")))
total_money+=input_money

#calculate how much money needs to be added/subtracted to get portfolio back to desired allocation
delta_monies={}
for key in existing_monies:
	delta_monies[key]=total_money*allocations[key]-existing_monies[key]
print("amounts to invest, by fund: "),
print(delta_monies)

#TODO: some way to save previous funds/allocations so you don't have to type them in each time
#TODO: notify to reallocate on certain dates
#resolve rounding issues?