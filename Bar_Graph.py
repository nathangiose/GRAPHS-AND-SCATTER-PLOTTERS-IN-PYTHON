# Nathan John Giose
# First we're importing the matplotlib as mpl


import matplotlib.pyplot as plt
# This is where I am inputting data as a source of reference


cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall= [140,  200, 120, 157]
# labels on the x-axis


x_pos = [i for i, _ in enumerate(cities)]
# labeling and visuals


plt.bar(x_pos, rainfall, color='Gray')
# Putting labels on the title, as well as on the x and y axis


plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
# Positioning the the data


plt.xticks(x_pos, cities)
# Displaying the data on a GUI


plt.show()


