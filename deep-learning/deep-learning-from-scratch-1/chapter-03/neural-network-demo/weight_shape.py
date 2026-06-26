from neural_net_mnist import init_network

if __name__ == "__main__":
    network = init_network()
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    print(W1.shape)
    # (784, 50)
    print(W2.shape)
    # (50, 100)
    print(W3.shape)
    # (100, 10)
