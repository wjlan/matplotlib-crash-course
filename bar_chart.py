labels = ['A','B','C']
values = [1,4,2]

bars = plt.bar(labels, values)

patterns =['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop())
# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')

plt.figure(figsize=(6,4)) 

plt.show()