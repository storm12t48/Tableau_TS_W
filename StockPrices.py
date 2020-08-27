#Question=>https://www.testdome.com/d/data-science-interview-questions/839
#You are given a list of tickers and their daily closing prices for a given period.
#Implement the most_corr function that, when given each ticker's daily closing prices, returns the pair of tickers that are the most highly (linearly) 
#correlated by daily percentage change.

import pandas as pd
import numpy as np

def most_corr(prices):
    prices = pd.DataFrame(prices)   
    cor = prices.pct_change().corr().unstack() # correlation of % change for each pair of stocks
    cor = cor[cor != 1].sort_values(ascending=False, kind='quicksort') # take out field with value = 1, and sort by values
    return list(cor.index[0]) # return the most correlated pair of stocks

#For example, the code below should print: ('FB', 'MSFT')
print(most_corr(pd.DataFrame.from_dict({
    'GOOG' : [
        742.66, 738.40, 738.22, 741.16,
        739.98, 747.28, 746.22, 741.80,
        745.33, 741.29, 742.83, 750.50
    ],
    'FB' : [
        108.40, 107.92, 109.64, 112.22,
        109.57, 113.82, 114.03, 112.24,
        114.68, 112.92, 113.28, 115.40
    ],
    'MSFT' : [
        55.40, 54.63, 54.98, 55.88,
        54.12, 59.16, 58.14, 55.97,
        61.20, 57.14, 56.62, 59.25
    ],
    'AAPL' : [
        106.00, 104.66, 104.87, 105.69,
        104.22, 110.16, 109.84, 108.86,
        110.14, 107.66, 108.08, 109.90
    ]
})))
