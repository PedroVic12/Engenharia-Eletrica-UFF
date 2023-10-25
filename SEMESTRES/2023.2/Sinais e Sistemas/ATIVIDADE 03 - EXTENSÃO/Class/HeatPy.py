import matplotlib.pyplot as plt
from scipy.signal import resample
# video 06 e 07 -> CSV

import heartpy as hp

print(hp)
data, timer = hp.load_exampledata(0)


plt.figure(figsize=(12, 4))
plt.plot(data)
plt.show()
