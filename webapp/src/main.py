# src/main.py

import cv2
import os
from transformations import affine_translation, affine_rotation, affine_scaling, affine_shearing

def main():
    # List of images to process
    image_filenames = ['circle.jpg', 'maze.jpg', 'star.jpg', 'portrait.jpg', 'landscape.jpg']
    
    for filename in image_filenames:
        image_path = os.path.join('images', filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error: Unable to load image {filename}")
            continue

        # Apply transformations
        translated_image = affine_translation(image, 50, 30)
        rotated_image = affine_rotation(image, 45)
        scaled_image = affine_scaling(image, 1.5, 1.5)
        sheared_image = affine_shearing(image, 0.5)

        # Save transformed images with original filename
        base_name = os.path.splitext(filename)[0]  # Get the filename without extension
        cv2.imwrite(os.path.join('images', f'translated_{base_name}.jpg'), translated_image)
        cv2.imwrite(os.path.join('images', f'rotated_{base_name}.jpg'), rotated_image)
        cv2.imwrite(os.path.join('images', f'scaled_{base_name}.jpg'), scaled_image)
        cv2.imwrite(os.path.join('images', f'sheared_{base_name}.jpg'), sheared_image)

        print(f"Processed and saved images for: {filename}")

if __name__ == "__main__":
    main()