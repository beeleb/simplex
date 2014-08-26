%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

corners = np.array([[0, 0], [1, 0], [0.5, 0.75**0.5]])
triangle = tri.Triangulation(corners[:, 0], corners[:, 1])
ref = tri.UniformTriRefiner(triangle)
trimesh = ref.refine_triangulation(subdiv=2)
# if subdiv==n, triangle is divided into 4**n area
plt.figure(figsize=(6, 6))
plt.triplot(trimesh)
plt.axis('off')
plt.axis('equal')
plt.show()