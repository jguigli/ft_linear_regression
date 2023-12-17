import numpy as np
import matplotlib.pyplot as plt

# Génération de données aléatoires
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Ajout d'une colonne de biais à X
X_b = np.c_[np.ones((100, 1)), X]

# Définition des hyperparamètres
learning_rate = 0.01
n_iterations = 1000

# Initialisation des coefficients
theta = np.random.randn(2, 1)

# Descente de gradient
for iteration in range(n_iterations):
    gradients = 2/100 * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - learning_rate * gradients

# Affichage des résultats
print("Coefficients finaux de la régression linéaire (descente de gradient) :")
print("Intercept (theta0) =", theta[0][0])
print("Pente (theta1) =", theta[1][0])

# Affichage de la régression linéaire
plt.scatter(X, y, label='Données')
plt.plot(X, X_b.dot(theta), color='red', label='Régression linéaire (descente de gradient)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
