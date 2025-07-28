import matplotlib.pyplot as plt
from gofish import imagecube
import numpy as np
#cube = imagecube('.fits', FOV=10.0)
cube = imagecube('J1604_CN_32.fits')
x, y, dy = cube.get_spectrum(coords=(1.5, -1.0), frame='sky', coord_type='cartesian')

# fig, ax = plt.subplots()
# ax.errorbar(x, y, dy, fmt=' ', capsize=1.25, capthick=1.25, color='k', lw=1.0)
# ax.step(x, y, where='mid', color='k', lw=1.0)
# ax.set_xlabel('Velocity (m/s)')
# ax.set_ylabel('Line Flux (Jy/beam)')
# ax.set_xlim(1.84e3, 3.84e3)


# x, y, dy = cube.get_spectrum(coords=(1.5, -1.0), frame='sky', coord_type='cartesian', area=2.0)

# fig, ax = plt.subplots()
# ax.errorbar(x, y, dy, fmt=' ', capsize=1.25, capthick=1.25, color='k', lw=1.0)
# ax.step(x, y, where='mid', color='k', lw=1.0)
# ax.set_xlabel('Velocity (m/s)')
# ax.set_ylabel('Line Flux (Jy/beam)')
# ax.set_xlim(1.84e3, 3.84e3)


# x, y, dy = cube.get_spectrum(coords=(2.0, np.pi / 2.0), frame='disk', coord_type='cylindrical')

# fig, ax = plt.subplots()
# ax.errorbar(x, y, dy, fmt=' ', capsize=1.25, capthick=1.25, color='k', lw=1.0)
# ax.step(x, y, where='mid', color='k', lw=1.0)
# ax.set_xlabel('Velocity (m/s)')
# ax.set_ylabel('Line Flux (Jy/beam)')
# ax.set_xlim(1.84e3, 3.84e3)

fig, ax = plt.subplots()

# Integeter
x, y, dy = cube.average_spectrum(r_min=0.5, r_max=1.0, inc=5.0, PA=152.,
                                 mstar=0.88, dist=59.5, dr=0.1, resample=1)
ax.errorbar(x, y, dy, fmt=' ', capsize=1.25, capthick=1.25, color='k', lw=1.0)
ax.step(x, y, where='mid', color='k', lw=1.0, label='resample=1')

# Float
x, y, dy = cube.average_spectrum(r_min=0.5, r_max=1.0, inc=5.0, PA=152.,
                                 mstar=0.88, dist=59.5, dr=0.1, resample=4)
ax.errorbar(x, y, dy, fmt=' ', capsize=1.25, capthick=1.25, color='r', lw=1.0)
ax.step(x, y, where='mid', color='r', lw=1.0, label='resample=4')

ax.legend(loc=1, markerfirst=False)
ax.set_xlabel('Velocity (m/s)')
ax.set_ylabel('Flux Density (Jy/beam)')
ax.set_xlim(2.54e3, 3.14e3)

plt.show()