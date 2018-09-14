import os
import pandas as pd
import matplotlib.pyplot as plt

dictOfCurrencies = {'bitcoin-cash': [], 'litecoin': [], 'siacoin': [], 'digibyte': []}

for fileName in os.listdir('Data'):

    file = open('Data/' + fileName, 'r')

    listOfLines = file.read().splitlines()

    priceUsdPosition = 0
    firstLineAsList = listOfLines[0].split(',')

    for x in range(0, len(firstLineAsList)):
        if firstLineAsList[x] == 'price_usd':
            priceUsdPosition = x

    for x in range(1, len(listOfLines)):
        lineAsList = listOfLines[x].split(',')
        listOfCurrencyData = dictOfCurrencies[lineAsList[0]]
        listOfCurrencyData.append(float(lineAsList[priceUsdPosition]))
        #print(dictOfCurrencies[lineAsList[0]])

    file.close()

df = pd.DataFrame()
for key, value in dictOfCurrencies.items():
    print(len(value))
    df[key] = value

plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()

