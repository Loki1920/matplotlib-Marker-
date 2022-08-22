import matplotlib.pyplot as plt
import numpy as np

y = np.array([1,2,3,4,5,6,7])

plt.plot(y,marker ='o')
plt.show()
# Mark each point with a star:
plt.plot(y,marker ='*')
plt.show()

# format string fmt
plt.plot(y,'*:r')
plt.show()

#Marker Size and color 
plt.plot(y,marker ='o',ms = 20,mec = 'r')
plt.show()

# mfc : color inside the marker 
plt.plot(y,marker ='o',ms = 20,mec = 'r',mfc='r')
plt.show()


