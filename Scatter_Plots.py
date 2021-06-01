# Nathan John Giose
# First we're importing everything from matplotlib
# Second we're importing matplotlib as plt


import matplotlib.pyplot as plt
import numpy as np
# Now I am inserting data as a source of reference



x = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])
y = np.array([220, 330, 190, 340, 410, 445, 415])
# labeling and visuals

m, b = np.polyfit(x, y, 1)
plt.scatter(x, y, color="Aqua")
plt.plot(x, m*x + b)
plt.plot(x, y, 'o', color="Red")
# Putting labels on the title, as well as on the x and y axis


plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
# Displaying the data on a GUI


plt.show()
