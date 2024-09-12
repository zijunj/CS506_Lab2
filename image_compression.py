import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

# Function to load and preprocess the image
def load_image(image_path):
    raise NotImplementedError('You need to implement this function')

# Function to perform KMeans clustering for image quantization
def image_compression(image_np, n_colors):
    raise NotImplementedError('You need to implement this function')

# Function to concatenate and save the original and quantized images side by side
def save_result(original_image_np, quantized_image_np, output_path):
    # Convert NumPy arrays back to PIL images
    original_image = Image.fromarray(original_image_np)
    quantized_image = Image.fromarray(quantized_image_np)
    
    # Get dimensions
    width, height = original_image.size
    
    # Create a new image that will hold both the original and quantized images side by side
    combined_image = Image.new('RGB', (width * 2, height))
    
    # Paste original and quantized images side by side
    combined_image.paste(original_image, (0, 0))
    combined_image.paste(quantized_image, (width, 0))
    
    # Save the combined image
    combined_image.save(output_path)

def __main__():
    # Load and process the image
    image_path = 'input.png'  
    output_path = 'result.png'  
    image_np = load_image(image_path)

    # Perform image quantization using KMeans
    n_colors = 8  # Number of colors to reduce the image to, you may change this to experiment
    quantized_image_np = image_compression(image_np, n_colors)

    # Save the original and quantized images side by side
    save_result(image_np, quantized_image_np, output_path)
