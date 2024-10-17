import numpy as np
from scipy.interpolate import interpn
import matplotlib.pyplot as plt
import math

data = np.load('./Исходные файлы/data_3d.npy')

x_initial = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
y_initial = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
z_initial = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])

x_new = np.linspace(-5, 6, 100)
y_new = np.linspace(-5, 6, 100)
z_new = np.linspace(-5, 6, 100)

X, Y, Z = np.meshgrid(x_new, y_new, z_new)
data_interpolated = interpn((x_initial, y_initial, z_initial), data, np.array([X, Y, Z]).T, method='linear')

fig, ax = plt.subplots(nrows=1, ncols=3)
plt.rcParams['font.size'] = '16'
fig.set_figheight(6)
fig.set_figwidth(18)

# z = 0.5
z_index = np.argmin(np.abs(z_new - 0.5))
im = ax[0].imshow(data_interpolated[:, :, z_index], cmap=plt.cm.plasma, extent=(x_new.min(), x_new.max(), y_new.min(), y_new.max()))
ax[0].set_title('z = 0.5')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
fig.colorbar(im)

# x = 1.5
x_index = np.argmin(np.abs(x_new - 1.5))
im = ax[1].imshow(data_interpolated[x_index, :, :], cmap=plt.cm.plasma, extent=(y_new.min(), y_new.max(), z_new.min(), z_new.max()))
ax[1].set_title('x = 1.5')
ax[1].set_xlabel('y')
ax[1].set_ylabel('z')
fig.colorbar(im)

# y = 2.5
y_index = np.argmin(np.abs(y_new - 2.5))
im = ax[2].imshow(data_interpolated[:, y_index, :], cmap=plt.cm.plasma, extent=(x_new.min(), x_new.max(), z_new.min(), z_new.max()))
ax[2].set_title('y = 2.5')
ax[2].set_xlabel('x')
ax[2].set_ylabel('z')
fig.colorbar(im)

fig.suptitle('Плотность электронов для срезов')
plt.tight_layout()


def interp_in_fractional(x, y, z):
    global data_interpn, data_interpolated

    x_min = int(x)
    x_max = x_min + 1

    y_min = int(y)
    y_max = y_min + 1

    z_min = int(z)
    z_max = z_min + 1

    data_interpolated = np.array([data_interpolated[x_min, y_min, z_min],
                                  data_interpolated[x_max, y_min, z_min],
                                  data_interpolated[x_min, y_max, z_min],
                                  data_interpolated[x_max, y_max, z_min],
                                  data_interpolated[x_min, y_min, z_max],
                                  data_interpolated[x_max, y_min, z_max],
                                  data_interpolated[x_min, y_max, z_max],
                                  data_interpolated[x_max, y_max, z_max]
                                  ])

    X, Y, Z = np.meshgrid(np.linspace(x_min, x_max, 11), np.linspace(y_min, y_max, 11), np.linspace(z_min, z_max, 11))
    data_interpn = interpn((np.array([x_min, x_max]), np.array([y_min, y_max]), np.array([z_min, z_max])),
                            data_interpolated.reshape((2, 2, 2)), np.array([X, Y, Z]).T, method='linear')

    print(data_interpn[int((x % 1) * 10), int((y % 1) * 10), int((z % 1) * 10)])

# data_interpn = data_interpolated
# interp_in_fractional(1.5, 1.6, 1.7)

def data_in_fractional(x, y, z):
    global x_new, y_new, z_new, data_interpolated

    x_index = np.argmin(abs(x_new - x))
    y_index = np.argmin(abs(y_new - x))
    z_index = np.argmin(abs(z_new - x))

    return data_interpolated[x_index, y_index, z_index]

print(data_in_fractional(1.5, 1.6, 1.7))
plt.show()
