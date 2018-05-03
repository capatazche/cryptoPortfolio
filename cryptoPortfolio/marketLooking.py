import coinmarketcap
import pandas as pd
import time

market = coinmarketcap.Market()

for x in range(24):
    litecoin = pd.Series((market.ticker('litecoin'))[0])
    siacoin = pd.Series((market.ticker('siacoin'))[0])
    digibyte = pd.Series((market.ticker('digibyte'))[0])
    bitcoin_cash = pd.Series((market.ticker('bitcoin-cash'))[0])

    coinArray = pd.DataFrame([bitcoin_cash, litecoin, siacoin, digibyte]).set_index('id')

    location = 'Data/' + str(time.time()) + '.csv'
    coinArray.to_csv(location)

    print(x/2)
    time.sleep(1800)
