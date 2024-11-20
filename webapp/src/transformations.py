# src/transformations.py

import cv2
import numpy as np

def affine_translation(image, tx, ty):
    """
    Apply affine translation to an image.

    Parameters:
    - image: Input image (numpy array).
    - tx: Translation in the x direction.
    - ty: Translation in the y direction.

    Returns:
    - Translated image (numpy array).
    """
    if image is None:
        raise ValueError("Input image is None.")
    
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, M, (cols, rows))

def affine_rotation(image, angle):
    """
    Apply affine rotation to an image.

    Parameters:
    - image: Input image (numpy array).
    - angle: Angle of rotation in degrees.

    Returns:
    - Rotated image (numpy array).
    """
    if image is None:
        raise ValueError("Input image is None.")
    
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))

def affine_scaling(image, sx, sy):
    """
    Apply affine scaling to an image.

    Parameters:
    - image: Input image (numpy array).
    - sx: Scaling factor in the x direction.
    - sy: Scaling factor in the y direction.

    Returns:
    - Scaled image (numpy array).
    """
    if image is None:
        raise ValueError("Input image is None.")
    
    return cv2.resize(image, None, fx=sx, fy=sy)

def affine_shearing(image, shear_factor):
    """
    Apply affine shearing to an image.

    Parameters:
    - image: Input image (numpy array).
    - shear_factor: Shearing factor.

    Returns:
    - Sheared image (numpy array).
    """
    if image is None:
        raise ValueError("Input image is None.")
    
    rows, cols = image.shape[:2]
    M = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    return cv2.warpAffine(image, M, (cols, rows))