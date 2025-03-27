import numpy as np

def curvature(r):
    return np.gradient(np.gradient(r))

r = np.linspace(0, 10, 100)
print("Curvatura Máxima:", max(curvature(r)))
