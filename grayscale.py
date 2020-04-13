import numpy as np
from matplotlib import pyplot as plt

random_image = np.random.random([1000, 1000])

plt.imshow(random_image, cmap='gray')
plt.colorbar()
plt.show()