import warnings
import numpy as np
import matplotlib.pyplot as plt
i = np.uint8(0)
z_warning= 1/i
warnings.filterwarnings("ignore")
z_nowarning = 2/i
warnings.filterwarnings("default")