import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def softmax(x):
    max_x = np.max(x)
    normal_x = np.exp(x-max_x + 1e-4)
    return normal_x/np.sum(normal_x)

def cross_entropy(x, t):
    if x.ndim == 1:
        x = x.reshape(1, x.size)
        t = t.reshape(1, t.size)
    batch_size = t.shape[0]
    return -np.sum(t*np.log(x + 1e-7))/batch_size

def _numerical_gradient(f, x):
    grad = np.zeros_like(x)
    h = 1e-7
    for i in range(x.size):
        temp_x = x[i]

        x[i] = temp_x + h
        fxh1 = f(x)

        x[i] = temp_x - h
        fxh2 = f(x)

        grad[i] = (fxh2-fxh1)/(2*h)
        x[i] = temp_x

    return grad

def numerical_gradient(f, x):
    if x.ndim == 1:
        return _numerical_gradient(f, x)
    else:
        grads = np.zeros_like(x)
        for i, x_item in enumerate(x):
            grads[i] = _numerical_gradient(f, x_item)
        return grads

class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init=0.01):
        self.params = {}

        self.params['W1'] = np.random.randn(input_size, hidden_size) * weight_init
        self.params['b1'] = np.random.randn(hidden_size)
        self.params['W2'] = np.random.randn(hidden_size, output_size) * weight_init
        self.params['b2'] = np.random.rand(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = softmax(a2)

        return z2

    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t)/float(t.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss = lambda w: self.loss(x, t)
        grads = {}
        grads['W1'] = numerical_gradient(loss, self.params['W1'])
        grads['b1'] = numerical_gradient(loss, self.params['b1'])
        grads['W2'] = numerical_gradient(loss, self.params['W2'])
        grads['b2'] = numerical_gradient(loss, self.params['b2'])

        return grads

if __name__ == '__main__':
    net = TwoLayerNet(784, 100, 10)
    # print(net.params['W1'].shape)
    # print(net.params['b1'].shape)
    # print(net.params['W2'].shape)
    # print(net.params['b2'].shape)

    # x = np.random.randn(100, 784)
    # y = net.predict(x)
    # print(y)
    x = np.random.randn(100, 784)
    t = np.random.randn(100, 10)
    grads = net.numerical_gradient(x, t)
    print(grads['W1'].shape)
    print(grads['b1'].shape)
    print(grads['W2'].shape)
    print(grads['b2'].shape)
