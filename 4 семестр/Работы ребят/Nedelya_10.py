#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt


data = np.load('data_3d.npy')


x = np.linspace(-5, 6, data.shape[0])
y = np.linspace(-5, 6, data.shape[1])
z = np.linspace(-5, 6, data.shape[2])


f = RegularGridInterpolator((x, y, z), data)


x_new = np.linspace(-5, 6, 100)
y_new = np.linspace(-5, 6, 100)
z_new = np.linspace(-5, 6, 100)
points = np.array(np.meshgrid(x_new, y_new, z_new)).T.reshape(-1, 3)
data_interpolated = f(points).reshape((100, 100, 100))


fig = plt.figure(figsize=(18, 6))

# z = 0.5
z_index = np.argmin(np.abs(z_new - 0.5))
plt.subplot(131)
plt.imshow(data_interpolated[:, :, z_index], origin='lower', extent=(x_new.min(), x_new.max(), y_new.min(), y_new.max()))
plt.colorbar()
plt.title('z = 0.5')
plt.xlabel('x')
plt.ylabel('y')

# x = 1.5
x_index = np.argmin(np.abs(x_new - 1.5))
plt.subplot(132)
plt.imshow(data_interpolated[x_index, :, :], origin='lower', extent=(y_new.min(), y_new.max(), z_new.min(), z_new.max()))
plt.colorbar()
plt.title('x = 1.5')
plt.xlabel('y')
plt.ylabel('z')

# y = 2.5
y_index = np.argmin(np.abs(y_new - 2.5))
plt.subplot(133)
plt.imshow(data_interpolated[:, y_index, :], origin='lower', extent=(x_new.min(), x_new.max(), z_new.min(), z_new.max()))
plt.colorbar()
plt.title('y = 2.5')
plt.xlabel('x')
plt.ylabel('z')

plt.tight_layout()
plt.show()


# In[5]:


import numpy as np
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.load('data_3d.npy')

x = np.linspace(-5, 6, data.shape[0])
y = np.linspace(-5, 6, data.shape[1])
z = np.linspace(-5, 6, data.shape[2])

f = RegularGridInterpolator((x, y, z), data)

x_new = np.linspace(-5, 6, 100)
y_new = np.linspace(-5, 6, 100)
z_new = np.linspace(-5, 6, 100)
points = np.array(np.meshgrid(x_new, y_new, z_new)).T.reshape(-1, 3)
data_interpolated = f(points).reshape((100, 100, 100))

fig = plt.figure(figsize=(18, 12))

# Графики сечений
plt.subplot(231)
z_index = np.argmin(np.abs(z_new - 0.5))
plt.imshow(data_interpolated[:, :, z_index], origin='lower', extent=(x_new.min(), x_new.max(), y_new.min(), y_new.max()))
plt.colorbar()
plt.title('z = 0.5')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(232)
x_index = np.argmin(np.abs(x_new - 1.5))
plt.imshow(data_interpolated[x_index, :, :], origin='lower', extent=(y_new.min(), y_new.max(), z_new.min(), z_new.max()))
plt.colorbar()
plt.title('x = 1.5')
plt.xlabel('y')
plt.ylabel('z')

plt.subplot(233)
y_index = np.argmin(np.abs(y_new - 2.5))
plt.imshow(data_interpolated[:, y_index, :], origin='lower', extent=(x_new.min(), x_new.max(), z_new.min(), z_new.max()))
plt.colorbar()
plt.title('y = 2.5')
plt.xlabel('x')
plt.ylabel('z')


ax = fig.add_subplot(234, projection='3d')
X, Y = np.meshgrid(x_new, y_new)
ax.plot_surface(X, Y, data_interpolated[:, :, z_index], cmap='viridis', rstride=1, cstride=1, antialiased=False)
ax.set_title('3D Electron Density Surface')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Electron Density')

plt.tight_layout()
plt.show()


# In[ ]:




