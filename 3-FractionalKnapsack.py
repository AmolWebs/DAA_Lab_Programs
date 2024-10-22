items_arr = [[500,5],[300,7]] #[[profit,weight]]
w = 10 #Knapsack capacity
Profit = 0

items_arr = sorted(items_arr, key = lambda x : x[0] / x[1], reverse = True)
for i in range(len(items_arr)):
	itemWt = items_arr[i][1]
	itemP = items_arr[i][0]
	if(itemWt > w):
		Profit += w*(itemP / itemWt)
		break
	else:
		Profit += itemP
		w -= itemWt
print("Name : Amol Subhash Dangat \nRoll No : 09\n\n")
print("Maximum Profit : ",Profit)