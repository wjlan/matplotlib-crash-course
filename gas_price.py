import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

# print(gas)
# print(gas.Year[::3])

plt.figure(figsize=(8,5))

plt.title('Gas Prices Over Time in USD', fontdict={'fontweight':'bold', 'fontsize':20})

plt.plot(gas.Year, gas.USA,'b.-', label='United States')
plt.plot(gas.Year, gas.Canada,'r.-', label='Canada')
plt.plot(gas.Year, gas.Australia,'g.-', label='Australia')
plt.plot(gas['Year'], gas['South Korea'],'y.-', label='South korea')

# # Another way to plot many values
# countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']
# for country in gas:
#     if country in countries_to_look_at:
#         plt.plot(gas.Year, gas[country], marker='.')

plt.xticks(gas.Year[::3].tolist()+[2011])

plt.xlabel('Year')
plt.ylabel('USD')

plt.legend()

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()