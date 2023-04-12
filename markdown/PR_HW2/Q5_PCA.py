import numpy as np
import matplotlib.pyplot as plt

# Question A: Generate data
x = np.random.randn(2000, 2) @ np.array([[2, 1], [1, 2]])

plt.figure(figsize=(6, 6))
plt.scatter(x[:, 0], x[:, 1], alpha=0.6)
plt.title('Original Data')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.savefig('QuetionA.png')
plt.close()

# Question B: Perform PCA transformation
x_mean = np.mean(x, axis=0)
x_centered = x - x_mean
cov_matrix = np.cov(x_centered.T)
eig_values, eig_vectors = np.linalg.eig(cov_matrix)
idx = eig_values.argsort()[::-1]
eig_values = eig_values[idx]
eig_vectors = eig_vectors[:, idx]
x_PCA = x_centered @ eig_vectors

# Step 2.2: Plot data after PCA
plt.figure(figsize=(6, 6))
plt.scatter(x_PCA[:, 0], x_PCA[:, 1], alpha=0.6)
plt.title('Data After PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig('QuetionB.png')
plt.close()

#Question C: perform whitening transformation
whitening_matrix = eig_vectors.dot(np.diag(1 / np.sqrt(eig_values)))
X_white = x_centered.dot(whitening_matrix)

# plot the samples after whitening
plt.scatter(X_white[:, 0], X_white[:, 1], alpha=0.6)
plt.title('Samples after Whitening Transformation')
plt.savefig('QuestionC.png')
plt.close()
