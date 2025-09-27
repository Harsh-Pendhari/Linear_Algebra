import numpy as np
from matplotlib import pyplot as plt

# Vector-Scalar multiplication (ALSO CALLED AS SCALAR MULTIPLICATION)

scalar_num = 3

# 2D :-
vect1 = np.array([5,9])
vect2 = scalar_num * vect1

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Before
axes[0].axhline(0, color='black', linewidth=0.5)
axes[0].axvline(0, color='black', linewidth=0.5)
axes[0].quiver(0, 0, vect1[0], vect1[1], angles='xy', scale_units='xy', scale=1, color='blue')
axes[0].set_xlim(0, max(vect1[0], vect2[0]) + 2)
axes[0].set_ylim(0, max(vect1[1], vect2[1]) + 2)
axes[0].set_aspect('equal', adjustable='box')
axes[0].set_title("Before")

# After
axes[1].axhline(0, color='black', linewidth=0.5)
axes[1].axvline(0, color='black', linewidth=0.5)
axes[1].quiver(0, 0, vect2[0], vect2[1], angles='xy', scale_units='xy', scale=1, color='red')
axes[1].set_xlim(0, max(vect1[0], vect2[0]) + 2)
axes[1].set_ylim(0, max(vect1[1], vect2[1]) + 2)
axes[1].set_aspect('equal', adjustable='box')
axes[1].set_title("After")

plt.suptitle("Scalar Multiplication of a Vector")
plt.show()


# 3D :-
vect3 = np.array([3, 11, 7])
vect4 = scalar_num * vect3

fig = plt.figure(figsize=(10, 5))

# Before
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.quiver(0, 0, 0, vect3[0], vect3[1], vect3[2], color='blue')
ax1.set_xlim([0, max(vect3[0], vect4[0]) + 2])
ax1.set_ylim([0, max(vect3[1], vect4[1]) + 2])
ax1.set_zlim([0, max(vect3[2], vect4[2]) + 2])
ax1.set_title("Before")

# After
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.quiver(0, 0, 0, vect4[0], vect4[1], vect4[2], color='red')
ax2.set_xlim([0, max(vect3[0], vect4[0]) + 2])
ax2.set_ylim([0, max(vect3[1], vect4[1]) + 2])
ax2.set_zlim([0, max(vect3[2], vect4[2]) + 2])
ax2.set_title("After")

plt.suptitle("3D Scalar Multiplication of a Vector")
plt.show()