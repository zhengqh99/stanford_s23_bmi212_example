# this needs to be run with python3.11
# inscrutable mandelbrot plotting code
# try running with 800 1000
import mahotas
import pylab
import numpy as np
import sys

import matplotlib.pyplot as plt

def mandelbrot(h, w, x=-0.5, y=0, z=1, mi=100):
    """
    Generate a Mandelbrot set image of the specified size.

    Parameters:
    h (int): The height of the output image in pixels.
    w (int): The width of the output image in pixels.
    x (float, optional): The horizontal coordinate of the center of the image. Default is -0.5.
    y (float, optional): The vertical coordinate of the center of the image. Default is 0.
    z (float, optional): The zoom level. A value of 1 represents no zoom. Default is 1.
    mi (int, optional): The maximum number of iterations for each pixel. Default is 100.

    Returns:
    numpy.ndarray: A 2D array of integers representing the Mandelbrot set image.
    """
    xw = 1.5
    yh = 1.5*h/w
    x_from = x - xw/z
    x_to = x + xw/z
    y_from = y - yh/z
    y_to = y + yh/z
    x = np.linspace(x_from, x_to, w).reshape((1, w))
    y = np.linspace(y_from, y_to, h).reshape((h, 1))
    c = x + 1j * y
    z = np.zeros(c.shape, dtype=np.complex128)
    t = np.zeros(z.shape, dtype=int)
    m = np.full(c.shape, True, dtype=bool)
    for i in range(mi):
        z[m] = z[m]**2 + c[m]
        div = np.greater(np.abs(z), 2, out=np.full(c.shape, False), where=m)
        t[div] = i
        m[np.abs(z) > 2] = False
    return t

try:
 a1 = sys.argv[1]
 a2 = sys.argv[2]
except* IndexError:
 print('you need args')
 sys.exit(1)

plt.imsave('out.jpg', mandelbrot(int(sys.argv[1]), int(sys.argv[2])), cmap='magma')
m = mahotas.imread('out.jpg')
pylab.imshow(m)
pylab.show()
