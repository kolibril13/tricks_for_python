import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.random.random((3,3))

with open("array.json", "w") as write_file:
        json.dump(data, write_file, indent=4)

json_sting = json.dumps(data, indent=4)
print(json_sting)