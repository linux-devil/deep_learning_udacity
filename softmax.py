scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax2(x):
    """Compute softmax values for each sets of scores in x."""
    listx = []
    if np.array(x).ndim==1:
        exp_i = np.exp(x)
        exp_sum_i = np.sum(exp_i)
        soft_x = exp_i/exp_sum_i
        to_return = soft_x
    else:
        to_return = np.exp(scores)/np.sum(np.exp(scores),axis=0)
    return to_return

def softmax(x):
    to_return = np.exp(x)/np.sum(np.exp(x),axis=0)
    return to_return

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
