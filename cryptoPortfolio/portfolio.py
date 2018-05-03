from tkinter import *
import matplotlib.pyplot as plt
import json
import requests

root = Tk()

root.title('Crypto Currency Portfolio')
root.iconbitmap(r'wolfIcon.ico')

# setting the table headers

headers = ['Symbol', 'Name', 'Quantity', 'Initial Price', 'Current Price', 'Initial Value', 'Current Value', '% ROI', 'ROI', '24 Hour Change', '7 Day Change']

headerCounter = 0
headerBGcolor = ''
for x in headers:
    if headerCounter % 2 == 1:
        headerBGcolor = 'silver'
    else:
        headerBGcolor = 'white'
    headerLabel = Label(root, text=x, font='Arial 10 bold', bg=headerBGcolor)
    headerLabel.grid(row=0, column=headerCounter, sticky=N + W + S + E)
    headerCounter += 1

#name = Label(root, text='John Elder', bg='white', fg='blue', font='Verdana 8 bold')
#name.grid(row=0, column=0, sticky=N+S+E+W)

def lookup():
    api_request = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    api = json.loads(api_request.content)

    myPortfolio = [
        {
            'symbol': 'LTC',
            'amount': 9.5,
            'priceAtBuy': 265
        },
        {
            'symbol': 'SC',
            'amount': 2952.71750886,
            'priceAtBuy': 0.059421958095186
        },
        {
            'symbol': 'DGB',
            'amount': 1870.16593311,
            'priceAtBuy': 0.042475535338354
        },
        {
            'symbol': 'BCH',
            'amount': 0.14195009,
            'priceAtBuy': 1129.29663
        },
        {
            'symbol': 'BCH',
            'amount': 0.31626453,
            'priceAtBuy': 844.767274
        }
    ]

    portfolioInitialValue = 0
    portfolioCurrentValue = 0

    currencyCounter = 0
    pieNames = []
    pieSizes = []
    for x in api:
        for y in myPortfolio:
            if x['symbol'] == y['symbol']:
                currencyCounter += 1

                totalInvestedInCoin = y['amount'] * y['priceAtBuy']
                portfolioInitialValue += totalInvestedInCoin

                totalCoinCurrentWorth = y['amount'] * float(x['price_usd'])
                portfolioCurrentValue += totalCoinCurrentWorth

                totalROI = totalCoinCurrentWorth - totalInvestedInCoin
                percentualROI = ((totalCoinCurrentWorth / totalInvestedInCoin) * 100) - 100

                pieNames.append(x['name'])
                pieSizes.append(totalCoinCurrentWorth)

                symbol = Label(root, text=x['symbol'], font='Arial 10', bg='white')
                symbol.grid(row=currencyCounter, column=0, sticky=N + S + E + W)

                name = Label(root, text=x['name'], font='Arial 10', bg='silver')
                name.grid(row=currencyCounter, column=1, sticky=N + S + E + W)

                quantity = Label(root, text='{0:.6f}'.format(y['amount']), font='Arial 10', bg='white')
                quantity.grid(row=currencyCounter, column=2, sticky=N + S + E + W)

                initialPrice = Label(root, text='${0:.4f}'.format(y['priceAtBuy']), font='Arial 10', bg='silver')
                initialPrice.grid(row=currencyCounter, column=3, sticky=N + S + E + W)

                currentPrice = Label(root, text='${0:.4f}'.format(float(x['price_usd'])), font='Arial 10', bg='white')
                currentPrice.grid(row=currencyCounter, column=4, sticky=N + S + E + W)

                initialValue = Label(root, text='${0:.2f}'.format(totalInvestedInCoin), font='Arial 10', bg='silver')
                initialValue.grid(row=currencyCounter, column=5, sticky=N + S + E + W)

                currentValue = Label(root, text='${0:.2f}'.format(totalCoinCurrentWorth), font='Arial 10', bg='white')
                currentValue.grid(row=currencyCounter, column=6, sticky=N + S + E + W)

                percentualROI = Label(root, text='{0:.2f}%'.format(percentualROI), font='Arial 10', bg='silver', fg=profitOrLossColor(percentualROI))
                percentualROI.grid(row=currencyCounter, column=7, sticky=N + S + E + W)

                rOI = Label(root, text='${0:.2f}'.format(totalROI), font='Arial 10', bg='white', fg=profitOrLossColor(totalROI))
                rOI.grid(row=currencyCounter, column=8, sticky=N + S + E + W)

                change24hours = Label(root, text='{0:.2f}%'.format(float(x['percent_change_24h'])), font='Arial 10', bg='silver', fg=profitOrLossColor(float(x['percent_change_24h'])))
                change24hours.grid(row=currencyCounter, column=9, sticky=N + S + E + W)

                change7days = Label(root, text='{0:.2f}%'.format(float(x['percent_change_7d'])), font='Arial 10', bg='white', fg=profitOrLossColor(float(x['percent_change_7d'])))
                change7days.grid(row=currencyCounter, column=10, sticky=N + S + E + W)

    portfolioROI = portfolioCurrentValue - portfolioInitialValue
    portfolioPercentualROI = ((portfolioCurrentValue / portfolioInitialValue) * 100) - 100

    portfolioInitialValueLabel = Label(root, text='${0:.2f}'.format(portfolioInitialValue), font='Arial 10', bg='silver')
    portfolioInitialValueLabel.grid(row=(currencyCounter + 1), column=5, sticky=N + S + E + W)

    portfolioCurrentValueLabel = Label(root, text='${0:.2f}'.format(portfolioCurrentValue), font='Arial 10', bg='white')
    portfolioCurrentValueLabel.grid(row=(currencyCounter + 1), column=6, sticky=N + S + E + W)

    portfolioPercentualROIlabel = Label(root, text='{0:.2f}%'.format(portfolioPercentualROI), font='Arial 10', bg='white', fg=profitOrLossColor(portfolioPercentualROI))
    portfolioPercentualROIlabel.grid(row=(currencyCounter + 1), column=7, sticky=N + S + E + W)

    portfolioROIlabel = Label(root, text='${0:.2f}'.format(portfolioROI), font='Arial 10', bg='silver', fg=profitOrLossColor(portfolioROI))
    portfolioROIlabel.grid(row=(currencyCounter + 1), column=8, sticky=N + S + E + W)

    api = ''
    updateButton = Button(root, text='Update', command=lookup)
    updateButton.grid(row=(currencyCounter + 1), column=10, sticky=N + S + E + W)

    def createPieGraph(labels, sizes):
        patches, texts = plt.pie(sizes, shadow=True, startangle=90)
        plt.legend(patches, labels, loc='best')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    pieChartButton = Button(root, text='Pie Chart', command= lambda: createPieGraph(pieNames, pieSizes))
    pieChartButton.grid(row=(currencyCounter + 1), column=9, sticky=N + S + E + W)

def profitOrLossColor(someNumber):
    if someNumber < 0:
        return 'red'
    elif someNumber > 0:
        return 'green'
    else:
        return 'black'

lookup()

root.mainloop()