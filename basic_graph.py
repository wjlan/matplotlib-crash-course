x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Resize your Graph
plt.figure(figsize=(5,3), dpi=100)

## Line 1

# Keyword Argument Notation
# plt.plot(x,y, label='2x', color='y', linewidth=3, linestyle='--', marker='.', markersize=10)

# Shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x,y, 'b^--', label='2x')

## Line 2

# select interval we want to plot points at
x2 = np.arange(0,4.5,0.5)
print(x2)

#plt.plot(x2, x2**2, 'r', label='X^2')

# plot part of the graph as line
plt.plot(x2[:5], x2[:5]**2, 'r', label='X^2')
# plot remainder of graph as dot
plt.plot(x2[4:], x2[4:]**2, 'r--', label='X^2')

# Add a title, specify front parameters with fontdict
plt.title('Our First Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4])
#plt.yticks([0,2,4,6,8,10])

# Add a legend
plt.legend()

# Save figure(dpi 300 is good when saving so graph has high resolution)
plt.savefig('my graph.png', dpi=300)

# Show plot
plt.show()