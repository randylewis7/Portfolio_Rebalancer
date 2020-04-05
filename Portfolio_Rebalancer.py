#'''
#get existing funds and corresponding (desired) allocations from user input
fund="placeholder"
allocation=0.0
allocations={} #global dictionary of funds and corresponding allocations
sum=0.0 #sum of allocations
#while true+break condition to imitate do-while loop

while True:
	print("Enter fund names and desired allocation percentage, one at a time...")
	allocations={} #wipe out allocations for each iteration of the loop
	while sum < 1.0:
		fund=raw_input("fund: ") #was behaving weirdly with regular input here
		allocation=float(input("allocation: "))
		sum+=allocation
		allocations[fund]=allocation #add fund and corresponding allocation to allocations dictionary
	if sum==1.0:
		#allocations=temp_allocations
		break
	else:
		sum=0.0 #reset sum so user can start over
		print("error! sum of allocations exceeds 1.0 (100%)")

print("all funds entered:")
print(allocations)

'''
#uncomment this section to prefill out existing allocations (cause I don't want to enter every time)
#modify the funds and numbers accordingly in code here if you want to use
#if using this method of inputting allocations, comment out the previous paragraph of code (1-23)
allocations={}
allocations["SWISX"]=.3
allocations["SWTSX"]=.65
allocations["SWAGX"]=.05
'''
total_money=0.0

#get how much money is currently in each fund
print("Enter how much money is currently in each fund...")
existing_monies={}

for key in allocations:
	money=float(input(key+": ")) #prompt for given fund
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
print("amounts to invest, by fund: ")
print(delta_monies)


	
	



#TODO: some way to save previous funds/allocations so you don't have to type them in each time
#TODO: notify to reallocate on certain dates
#resolve rounding issues?