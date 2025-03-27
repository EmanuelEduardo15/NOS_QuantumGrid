import numpy as np

def calculate_curvature(velocity_field):
    dx = np.gradient(velocity_field, axis=0)
    dy = np.gradient(velocity_field, axis=1)
    return np.sqrt(dx**2 + dy**2)
