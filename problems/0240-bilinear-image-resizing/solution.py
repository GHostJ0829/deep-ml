import numpy as np

def bilinear_resize(image, new_height: int, new_width: int) -> list:
    """
    Resize an image using bilinear interpolation.
    
    Args:
        image: 2D (grayscale) or 3D (RGB) array representing an image
        new_height: Target height of the resized image
        new_width: Target width of the resized image
    
    Returns:
        Resized image as a nested list with values rounded to 2 decimal places
    """
    # Your code here
    img = np.asarray(image,dtype = float)

    H, W = img.shape[:2]

    if img.ndim == 2:
        result = np.zeros((new_height,new_width))
    else:
        result = np.zeros((new_height,new_width,img.shape[2]))
    for i in range(new_height):
        for j in range(new_width):
            y = i * H / new_height
            x = j * W /new_width
            y0 = int(y)
            x0 = int(x)

            y1 = min(y0 + 1, H - 1)
            x1 = min(x0 + 1, W - 1)
            dy = y - y0
            dx = x - x0

            value = (1 - dx) * (1 - dy) * img[y0, x0] + dx * (1 - dy) * img[y0, x1] +(1 - dx) * dy * img[y1, x0] +dx * dy * img[y1, x1]

            result[i, j] = value
    return result

