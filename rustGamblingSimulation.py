#46% chance something goes up to 150%
#12 ones 6 threes 4 fives 2 tens one 20, 25 total
import random
its = 0
totalScrap = 20
wonLastGame = True
lastGambled = 0

amountGambling1=0
amountGambling3=0
amountGambling5=0
amountGambling10=0
amountGambling20=0


#RANDOMLY GAMBLING
while True:
    amountGambling1 += random.randrange(0,totalScrap)
    totalScrap -= amountGambling1
    if totalScrap == 0: break
    amountGambling3 += random.randrange(0,totalScrap)
    totalScrap -= amountGambling3
    if totalScrap == 0: break
    amountGambling5 += random.randrange(0,totalScrap)
    totalScrap -= amountGambling5
    if totalScrap == 0: break
    amountGambling10 += random.randrange(0,totalScrap)
    totalScrap -= amountGambling10
    if totalScrap == 0: break
    amountGambling20 += random.randrange(0,totalScrap)
    totalScrap -= amountGambling20
    if totalScrap == 0: break
    

print(str(totalScrap))
strategy = "Gambled on 1: " + str(amountGambling1) + " Gambled on 3: " + str(amountGambling3)+ " Gambled on 5: " + str(amountGambling5)+ " Gambled on 10: " + str(amountGambling10)+ " Gambled on 20: " + str(amountGambling20)

# SPINNING THE WHEEL
while its<100:
    randNum=random.randrange(1,100)
    if randNum<=48:
        totalScrap += amountGambling1 * 2
    elif randNum<=72:
        totalScrap += amountGambling3 * 3
    elif randNum<=88:
        totalScrap += amountGambling5 * 5
    elif randNum<=96:
        totalScrap += amountGambling10 * 10
    elif randNum <= 100:
        totalScrap += amountGambling20 * 20
    its+=1
    print(str(its) + ": " + str(totalScrap))
print(strategy)
