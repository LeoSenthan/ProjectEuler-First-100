#brute force
counter=1
for pennies in range(0,201):
	for pence in range(0,101):
		for fiveps in range(0,41):
			for tenps in range(0,21):
				for twentyps in range(0,11):
					for fiftyps in range(0,5):
						for pounds in range(0,3):
							if (pennies+2*pence+5*fiveps+10*tenps+twentyps*20+fiftyps*50+pounds*100)==200:
								counter+=1
print(counter)