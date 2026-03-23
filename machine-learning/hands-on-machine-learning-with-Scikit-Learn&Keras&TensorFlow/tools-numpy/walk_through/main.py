import numpy as np

m3 = np.array([[1, 2, 3], [5, 7, 11], [21, 29, 31]])
eigenvalues, eigenvector = np.linalg.eig(m3)
print(eigenvalues)
# [42.26600592 -0.35798416 -2.90802176]
print(eigenvector)
# [[-0.08381182 -0.76283526 -0.18913107]
#  [-0.3075286   0.64133975 -0.6853186 ]
#  [-0.94784057 -0.08225377  0.70325518]]