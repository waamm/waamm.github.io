import numpy as np
import matplotlib.pyplot as plt
from pyweierstrass import weierstrass as w

PI = np.pi
E  = np.e

# The colouring algorithm is due to Claudio Rocchini: https://en.wikipedia.org/wiki/File:Color_complex_plot.jpg
# And the rest is due to ChatGPT

def hsv_to_rgb(h, s, v):
    if s == 0:
        return v, v, v

    if h == 1:
        h = 0

    z = np.floor(h * 6)
    i = int(z)
    f = h*6 - z

    p = v*(1-s)
    q = v*(1-s*f)
    t = v*(1-s*(1-f))

    if i == 0: return v, t, p
    if i == 1: return q, v, p
    if i == 2: return p, v, t
    if i == 3: return p, q, v
    if i == 4: return t, p, v
    if i == 5: return v, p, q


def colour_value(v):
    # avoid numpy int scalar bug
    v = np.complex128(v)

    a = np.angle(v)
    while a < 0: 
        a += 2*PI
    a /= 2*PI

    m = abs(v)
    ranges, rangee = 0, 1

    while m > rangee:
        ranges = rangee
        rangee *= E

    k = (m - ranges) / (rangee - ranges)

    sat = (k*2 if k < 0.5 else 1-(k-0.5)*2)
    sat = 1 - (1-sat)**3
    sat = 0.4 + sat*0.6

    val = (k*2 if k < 0.5 else 1-(k-0.5)*2)
    val = 1 - val
    val = 1 - (1-val)**3
    val = 0.6 + val*0.4

    return hsv_to_rgb(a, sat, val)


# -------- Weierstrass sigma domain colouring --------

omega = (0.5+0j, 0.25 + 1j)   # half-periods ω1/2, ω2/2
P = 0.375 + 0.5j
two_P = 0.75 + 1j
dim = 800

re = np.linspace(-3.5, 3.5, dim)
im = np.linspace(-3.5, 3.5, dim)

img = np.zeros((dim, dim, 3), dtype=float)

for j, y in enumerate(im):
    for i, x in enumerate(re):

        z = x + 1j*y
        v = (
            w.wsigma(z - P, omega)**2
            * w.wsigma(z, omega)**-1
            * w.wsigma(z - two_P, omega)**-1
            )

        # convert weird scalars from pyweierstrass:
        try:
            v = np.complex128(v)
        except:
            v = complex(v)

        img[j, i] = colour_value(v)

plt.figure(figsize=(8,8))
plt.imshow(img)
plt.axis("off")
plt.show()