%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

corners = np.array([[0, 0], [1, 0], [0.5, 0.75**0.5]])
triangle = tri.Triangulation(corners[:, 0], corners[:, 1])
ref = tri.UniformTriRefiner(triangle)
trimesh = ref.refine_triangulation(subdiv=2)
# if subdiv==n, triangle is divided into 4**n area

mat = np.array([[0.1,0.2,0.7],
                [0.2,0.3,0.5],
                [0.3,0.4,0.3],
                [0.5,0.4,0.1],
                [0.7,0.3,0.0],
                [0.1,0.1,0.8],
                [0.3,0.3,0.4]])
d_list = []  # the list of distances between mat[i] amd mat[i+1]
#  (0,0) means p1 = 1, (1,0) means p2 = 1
x_list = []  # the transition of x
y_list = []  # the transition of y
for i in range(len(mat)-1):  # len(d_list) == len(mat)-1
    dx = mat[i+1][0]-mat[i][0]
    dy = mat[1+1][1]-mat[i][1]
    dz = mat[i+1][2]-mat[i][2]
    d = (dx**2+dy**2+dz**2)**0.5
    d_list.append(np.asscalar(d))
    x_list.append(mat[i][1]+mat[i][2]*0.5)
    y_list.append(mat[i][2]*0.75**0.5)
    
plt.figure(figsize=(6, 6))
plt.triplot(trimesh)
plt.axis('off')
plt.axis('equal')
plt.tricontourf(x_list,y_list,d_list)
plt.show()