import matplotlib.pyplot as plt
import pandas as pd

breadprice = pd.read_csv('breadprice.csv')
new_breadprice = pd.read_csv('breadprice.csv')


new_breadprice.drop(columns="Year", inplace=True)
newValue = new_breadprice.loc[10].mean()
breadprice.fillna(newValue, inplace=True)

avg_price = breadprice.mean(axis=1)
years = breadprice['Year']
plt.plot(years, avg_price, marker='o')
plt.title('Average price of bread (2012-2022)')
plt.ylabel('Average price')
plt.xlabel('Year')
plt.show()