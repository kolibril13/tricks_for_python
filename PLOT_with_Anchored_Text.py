import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

# make some data
x = np.arange(10)
y = x

# set up figure and axes
f, ax = plt.subplots(1,1)

# loc works the same as it does with figures (though best doesn't work)
# pad=5 will increase the size of padding between the border and text
# borderpad=5 will increase the distance between the border and the axes
# frameon=False will remove the box around the text
num= 2.233434
anchored_text = AnchoredText("Test " + str(format(num, '.2f')), loc=2)
ax.plot(x,y)
ax.add_artist(anchored_text)

plt.show()