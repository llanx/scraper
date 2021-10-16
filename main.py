
from bs4 import BeautifulSoup

import requests
import Blocktime

my_function()
json = {'query': '{ pool(id:"0xcde5a11a4acb4ee4c805352cec57e236bdbc3837000200000000000000000019") { name, totalLiquidity, id}}'}
url = "https://graph-node.beets-ftm-node.com/subgraphs/name/beethovenx"
r = requests.post(url=url, json=json)
json_response = r.json()

principal = 10000
#yearlyReturnAPR = principalAmount*(1+(20*1))
beetsperblock = 5.05
FTM_Beetspoolweight = .3012
secondsInAYr = 31536000
priceofBeets = 1.28
TVL_FTM_Beets = float(json_response['data']['pool']['totalLiquidity'])
FTM_BlocksPerSecond = 1.07
APRcalculated = (beetsperblock*FTM_Beetspoolweight*priceofBeets*FTM_BlocksPerSecond*secondsInAYr/TVL_FTM_Beets)*100

#print('APR yearly is', APRcalculated, '%')
#print('the yearly APR sum return is', yearlyReturnAPR)

emissionList = [5.05, 5.02, 4.98, 4.90, 4.75, 4.50, 4.00, 3.40, 2.80, 2.30, 2, 1.80]
beatsTVLinflation = [13089600, 13011840, 12908160, 12700800, 12312000, 11664000, 10368000, 8812800, 7257600, 5961600, 5184000, 4665600]
time = 1/360
n = 30
i = 1
j = 0
#price fluction direction is mono-directional so a .8 would be 20% down each month 1.2% would be 20% up a month
priceFluctuation = 1
TVLCapture = .5
print('starting cash', principal)
oneYearCoinsupply = 117936000

En = 360
Errortest = (principal*(1+(17.13/En))**En)
temp = (1+(17.13/En))
k = 0
i = 0
j = 0
Amount = principal
#snapshot of 12 times over a year
for x in emissionList:
    #Depreciating interest rate based on emission schedule
    interestRate = (x * FTM_Beetspoolweight * priceofBeets * FTM_BlocksPerSecond * secondsInAYr / TVL_FTM_Beets)
    #print('interest rate', interestRate)
    #product notation of formula interest for APR instead of exponents
    for x in range(30):
        k = k + 1
        if(k != 360):
            temp = temp * (1 + (interestRate / En))
    #take a snap
    Amount = principal * temp
    print('Amount Snapshot ', Amount)
    Amount = Amount/principal
    #capture a percentage of all beets that are minted and add them to the TVL pool that is captured
    TVL_FTM_Beets = TVL_FTM_Beets + ((beatsTVLinflation[j] * priceofBeets) * TVLCapture) * .8
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
Amount = principal*temp
#print('Ending TVL{:e}'.format())
#print('Comparison cash Errortest {:e}'.format(Errortest))
print('Ending cash', format(Amount))
marketcap = oneYearCoinsupply*priceofBeets
#print('ending market cap', marketcap)