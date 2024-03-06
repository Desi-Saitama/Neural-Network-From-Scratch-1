import numpy as np
#import nnfs

#nnfs.init()

layer_output = [[4.8, 1.21, 2.385],
				[8.9, -1.81, 0.2],
				[1.41, 1.051, 0.026]]

exp_value = np.exp(layer_output)

norm_values = exp_value/np.sum(exp_value, axis=1, keepdims=True)
print(norm_values)
#print(sum(norm_values))