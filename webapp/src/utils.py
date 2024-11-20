import cv2
import os

def load_image(filepath):
    """Load an image from a file path."""
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError(f"Image not found or unable to load: {filepath}")
    return image

def save_image(image, filepath):
    """Save an image to a specified file path."""
    cv2.imwrite(filepath, image)

def ensure_directory_exists(directory):
    """Ensure that a directory exists; create it if it doesn't."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_unique_filename(directory, base_name, extension):
    """Generate a unique filename to avoid overwriting in the specified directory."""
    counter = 1
    new_name = os.path.join(directory, f"{base_name}{extension}")
    while os.path.exists(new_name):
        new_name = os.path.join(directory, f"{base_name}_{counter}{extension}")
        counter += 1
    return new_name
