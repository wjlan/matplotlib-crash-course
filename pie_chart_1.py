import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left', 'Right']


plt.pie([left, right], labels = labels, autopct='%.2f %%')

plt.title('Foot Preference of FIFA Players')

plt.show()