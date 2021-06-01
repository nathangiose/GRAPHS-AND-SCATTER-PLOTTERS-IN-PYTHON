# Nathan John Giose
# First we're importing matplotlib as plt


import matplotlib.pyplot as plt
# Now I am inserting data as a source of reference


testmarks = [98,78, 68, 73, 72, 97, 88, 60, 94, 95, 80, 73, 82, 80, 99, 91, 74, 88, 70, 94, 86, 81, 100, 99, 84, 93, 94, 79]
# Substituting testmarks as a different variable


data1=[testmarks]
# This is where we choose how the information will be displayed
# The Lower Extreme is 60 because nobody got lower than 60
# The Lower Quartile is between 75 and 80, which indicates that the average range is starting
# The Median is 85
# The Upper Quartile is between 90 and 95, and indicates that the average range has ended
# The Upper Extreme is 100, because that was the highest achieved


plt.subplot(121)
plt.boxplot(data1)
# Putting labels on the title, as well as on the x and y axis


plt.xlabel("Student Average")
plt.ylabel("Marks")
plt.title("Boxplot for Testmarks")
# Information for the second plot


plt.subplot(122)
plt.hist(data1, bins=5, color="Aqua")
# Displaying the data on a GUI


plt.show()
