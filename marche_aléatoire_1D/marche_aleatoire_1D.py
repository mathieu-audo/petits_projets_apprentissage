import numpy as np
import matplotlib.pyplot as plt

# Paramètres
n_steps = 1000  # nombre de pas
probs = [1/3, 1/3, 1/3]  # proba pour [-1, 0, 1]

# Génération des pas : -1, 0 ou 1
steps = np.random.choice([-1, 0, 1], size=n_steps, p=probs)

# Calcul des positions cumulées (position initiale = 0)
positions = np.cumsum(steps)

# Tracé
plt.figure(figsize=(10, 5))
plt.plot(positions, label="Marche aléatoire")
plt.title("Marche aléatoire 1D")
plt.xlabel("Temps (pas)")
plt.ylabel("Position")
plt.axhline(0, color='black', linewidth=1, linestyle='--')  # ligne de référence
plt.legend()
plt.grid(True)
plt.show()

