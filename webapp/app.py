# webapp/app.py

import sys
import os
import streamlit as st
import cv2
from src.transformations import affine_translation, affine_rotation, affine_scaling, affine_shearing
from src.utils import load_image, save_image, ensure_directory_exists

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure the upload folder exists
UPLOAD_FOLDER = r'C:\Users\Lenovo\Downloads\CV\CV\webapp\static\uploads'
ensure_directory_exists(UPLOAD_FOLDER)

# Streamlit app title
st.title("Image Transformation Tool")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file to the upload folder
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load the image using the utility function
    image = load_image(file_path)

    # Apply transformations
    transformed_images = {
        'Translated': affine_translation(image, 50, 30),
        'Rotated': affine_rotation(image, 45),
        'Scaled': affine_scaling(image, 1.5, 1.5),
        'Sheared': affine_shearing(image, 0.5)
    }

    # Display the original image
    st.image(image, caption='Original Image', use_container_width=True)

    # Display transformed images
    st.header("Transformed Images:")
    for transformation_name, transformed_image in transformed_images.items():
        st.image(transformed_image, caption=transformation_name, use_container_width=True)

# No need for st.run() here