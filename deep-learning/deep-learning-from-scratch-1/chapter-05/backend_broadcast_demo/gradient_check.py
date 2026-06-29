import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

print(x_batch.shape)
print(t_batch.shape)

grad_gradient = network.gradient(x_batch, t_batch)
grad_numerical = network.numerical_gradient(x_batch, t_batch)

for key in grad_gradient.keys():
    diff = np.average(np.abs(grad_gradient[key] - grad_numerical[key]))
    print(f"{key}: {str(diff)}")
