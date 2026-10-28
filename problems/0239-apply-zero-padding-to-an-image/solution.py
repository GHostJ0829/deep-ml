import numpy as np

def zero_pad_image(img, pad_width):
    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here
    if pad_width < 0 or type(pad_width) is not int:
        return -1

    img = np.array(img)

    if img.ndim != 2 or 0 in img.shape:
        return -1
    padded = np.pad(
        img,
        pad_width=pad_width,
        mode='constant',
        constant_values=0
    )

    return padded.astype(int).tolist()    