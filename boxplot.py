import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']

madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']

revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall'] 

labels = ['FC Barcelona','Real Madrid', 'New England Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], labels=labels, patch_artist=True, medianprops={'linewidth':2})

for box in boxes['boxes']:
    # Set edge color
    box.set(color='#4286f4', linewidth=2)
    
    # Change Fill Color
    box.set(facecolor='#e0e0e0')
    
plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overal Rating')
            

plt.show()