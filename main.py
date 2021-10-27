
#python sucks but its so easy to use
#ugly code, great financials
#TODO clean up code so it doesn't look like cobbled together dog shit
from bs4 import BeautifulSoup
import requests
import blockTime
import compoundingSchedule

json = {'query': '{ pool(id:"0xcde5a11a4acb4ee4c805352cec57e236bdbc3837000200000000000000000019") { name, totalLiquidity, id}}'}
url = "https://graph-node.beets-ftm-node.com/subgraphs/name/beethovenx"
r = requests.post(url=url, json=json)
json_response = r.json()


beetsperblock = 5.05
principal = 10000
FTM_Beetspoolweight = .3012
secondsInAYr = 31536000
priceofBeets = 1.16
TVL_FTM_Beets = float(json_response['data']['pool']['totalLiquidity'])
FTM_BlocksPerSecond = .87
APRcalculated = (beetsperblock*FTM_Beetspoolweight*priceofBeets*FTM_BlocksPerSecond*secondsInAYr/TVL_FTM_Beets)*100

#market cap underlying asset fluctation math
#marketCapGrowth = 1
tokenSupplyCurrent = 13760759
tokenSupplyStarting = 5000000
totalTokenSupply = 0
marketCap = 10000000
#print('APR yearly is', APRcalculated, '%')
#print('the yearly APR sum return is', yearlyReturnAPR)


emissionList = [5.05, 5.02, 4.98, 4.90, 4.75, 4.50, 4.00, 3.40, 2.80, 2.30, 2, 1.80]
inflationSupply = [13089600, 13011840, 12908160, 12700800, 12312000, 11664000, 10368000, 8812800, 7257600, 5961600, 5184000, 4665600]
time = 1/360
n = 30
i = 1
j = 0
#price fluction direction is mono-directional so a .8 would be 20% down each month 1.2% would be 20% up a month
priceFluctuation = 1
TVLCapture = .5
print('starting cash', principal)
oneYearCoinsupply = 117936000

#code for any compounding period
En = 360

Errortest = (principal*(1+(17.13/En))**En)

k = 0
i = 0
j = 0
Amount = principal
#initialize temp
exponentiation = (1 + (6.83 / En))
#snapshot of 12 times over a year
startBool = True
daysSinceLaunch = 0
marketCapBool = True
beetsMarketGrowthInt = 10000000
startingPriceOfBeets = priceofBeets
pricelist = []
scaryNumber = 0.95
for x in emissionList:
    #Depreciating interest rate based on emission schedule
    interestRate = (x * FTM_Beetspoolweight * priceofBeets * FTM_BlocksPerSecond * secondsInAYr / TVL_FTM_Beets)
    #print('APR rate', interestRate*100)
    #product notation of formula interest for APR instead of exponents

    for x in range(30 - daysSinceLaunch):
        k = k + 1
        #exponential product notation
        if(k != 360):
            exponentiation = exponentiation * (1 + (interestRate / En))
    if startBool:
        daysSinceLaunch = 0
        daysSinceLaunch = False

    #price dilution affects
    if (marketCapBool == False):
        totalTokenSupply = totalTokenSupply + inflationSupply[j]
    if marketCapBool:
        totalTokenSupply = tokenSupplyStarting + inflationSupply[j]
        marketCapBool = False
    marketCap = marketCap + inflationSupply[j]*scaryNumber
    priceofBeets = marketCap/totalTokenSupply
    #print('price of beets', priceofBeets)
    #take a snap with exponential interest added for the period
    #APR calculation for reference A = P*(1 + r/n)^nt and modification
    tempAmt = Amount
    #this formula doesn't work because it double counts losses
    #changeInPricePercent = 1+(priceofBeets - startingPriceOfBeets)/startingPriceOfBeets
    changeInPricePercent = 1 + (priceofBeets - startingPriceOfBeets) / startingPriceOfBeets
    #print('change in price percent', changeInPricePercent)
    #change in price of beets is the scariest number and can be changed here
    Amount =  (Amount * (scaryNumber) * exponentiation)
    print('Amount Snapshot ', Amount)
    Amount = Amount/exponentiation
    #print('amount after division', Amount)
    #capture a percentage of all beets that are minted and add them to the TVL pool that is captured
    TVL_FTM_Beets = TVL_FTM_Beets + ((inflationSupply[j] * priceofBeets) * TVLCapture) * .8
    #print('total inflation capture{:e}'.format(TVL_FTM_Beets))
    i = i + 1
    j = j + 1
    # Amount = (Amount*temp)
    # print('days', 30*i)
    #
    # #interestRate = (x * FTM_Beetspoolweight * priceofBeets * FTM_BlocksPerSecond * secondsInAYr / TVL_FTM_Beets)
    # TVL_FTM_Beets = TVL_FTM_Beets + ((beatsTVLinflation[j]*priceofBeets)*TVLCapture)*.8
    #
    # print(interestRate*100, '%')
    # tempAmt = Amount*.2
    # #Amount = (Amount*.8)*priceFluctuation + tempAmt*.2
    # Amount = Amount + (principal*(1 + (interestRate/n)**(time*n)))
    # #print('Current Cash', Amount)
    # i = i + 1
    # j = j + 1
    # priceofBeets = priceofBeets*priceFluctuation
    # #print('price', priceofBeets)

    #current beets price for an entry point
    calculatorprice = 1.54
    sum = 5000000
    magicnumber = 0.81
    inflationSupply = [13089600, 13011840, 12908160, 12700800, 12312000, 11664000, 10368000, 8812800, 7257600, 5961600,
                       5184000, 4665600]
    # 0.81 is extremely important is the price decrease beets can tolerate per month,
    # to not lose you money in the FTM-Beets pool
    # it is derived from a much bigger model financial model
    # but can be extracted from that to create a simple entry and ending point for customers
    # and a business growth model for the company
    # 0.19 is obviously just 1-0.81 and can illustrate the amount of market cap growth beets needs to achieve versus
    #its supply inflation
    #for x in range(12):
        # sum = sum + inflationSupply[x]*(magicnumber)
        # #0.81 should never be changed it is the 19% price drop per month your investment can tolerate
        # calculatorprice = (calculatorprice * magicnumber)

     # print('Youve lost money at this price point at the end of a year', calculatorprice)
     # print('total supply', sum)
     # print('market cap total at the end of the year needed{:e}'.format(sum*calculatorprice))

Amount = Amount * exponentiation
#print('Ending TVL{:e}'.format())
#print('Comparison cash Errortest {:e}'.format(Errortest))
print('Ending cash', format(Amount))
marketcap = oneYearCoinsupply*priceofBeets
#print('ending market cap', marketcap)