def test_curvature_calculation():
    import numpy as np
    r = np.linspace(0, 10, 100)
    curvature = np.gradient(np.gradient(r))
    assert max(curvature) < 0.15, "Curvatura excede limite!"
