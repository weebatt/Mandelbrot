import numpy as np
import matplotlib.pyplot as plt

# Parameters
width, height = 10000, 10000
dpi = 900
re_min, re_max = -2.0, 1.0
im_min, im_max = -1.5, 1.5
escape_radius = 2

# Set figure dimensions based on DPI and size
width_in_inches = width / dpi
height_in_inches = height / dpi

fig, ax = plt.subplots(figsize=(width_in_inches, height_in_inches), dpi=dpi)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.axis('off')

def mandelbrot(c, max_iter):
    """Vectorized Mandelbrot set calculation."""
    z = np.zeros_like(c)
    div_time = np.zeros(c.shape, dtype=int)
    mask = np.ones(c.shape, dtype=bool)

    for i in range(max_iter):
        z[mask] = z[mask]**2 + c[mask]
        mask = np.abs(z) <= escape_radius
        div_time += mask

    return div_time

def generate_mandelbrot(re_min, re_max, im_min, im_max, width, height, max_iter):
    """Generates a detailed image of the Mandelbrot set."""
    re_values = np.linspace(re_min, re_max, width)
    im_values = np.linspace(im_min, im_max, height)
    re, im = np.meshgrid(re_values, im_values)
    c = re + im * 1j

    # Generate the Mandelbrot set
    mandelbrot_set = mandelbrot(c, max_iter)

    # Display and save the Mandelbrot set image
    plt.imshow(mandelbrot_set, cmap='binary', extent=(re_min, re_max, im_min, im_max))
    filename = f"mandelbrot_set_detailed_{max_iter}.png"
    fig.savefig(filename, dpi=dpi, bbox_inches='tight', pad_inches=0)
    print(f"Saved: {filename}")


list_one = [2, 4, 8]
for max_iter in list_one:
    generate_mandelbrot(re_min, re_max, im_min, im_max, width, height, max_iter)
