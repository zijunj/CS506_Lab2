# Image Quantization using KMeans Clustering

## Overview
This project demonstrates how to perform image quantization using KMeans clustering. The script takes an input image, reduces the number of unique colors using KMeans, and saves a new image with the original and quantized versions displayed side by side.

## How it Works
1. **Image Loading**: The image is loaded and preprocessed into a NumPy array.
2. **KMeans Clustering**: The pixel colors are clustered into `n_colors` clusters using the KMeans algorithm.
3. **Image Quantization**: Each pixel is assigned the color of its nearest cluster centroid, reducing the number of distinct colors in the image.
4. **Saving Results**: The original and quantized images are saved side by side in a new image file.

## File Description

- **`load_image(image_path)`**: This function is responsible for loading an image from a file path and returning it as a NumPy array. You need to implement this function.
  
- **`image_quantization(image_np, n_colors)`**: This function takes the image NumPy array and applies KMeans clustering to reduce the number of colors. You need to implement this function.

- **`save_side_by_side_image(original_image_np, quantized_image_np, output_path)`**: This function saves the original and quantized images side by side.

- **`__main__()`**: The main function that loads an image, performs quantization, and saves the result.

## Setup Instructions

### Prerequisites
Ensure you have the following Python packages installed:

``` bash
pip install numpy scikit-learn pillow
```

### Implement the Missing Functions
You need to implement the following two functions:

1. **`load_image(image_path)`**: This function should load the image from the given path and return it as a NumPy array.
2. **`image_quantization(image_np, n_colors)`**: This function should take a NumPy array representing the image and the number of colors, then apply KMeans clustering to quantize the image.

### How to Run

1. Implement the missing functions.
2. Run the script using Python:

``` bash
python image_quantization.py
```

This will:
- Load the image specified in **`image_path`**.
- Apply KMeans clustering to quantize the image into **`n_colors`**.
- Save the result as **`result.png`** with the original and quantized images side by side.

### Example Usage

In the **`__main__()`** function, specify:
- **`image_path`**: The path to your input image (e.g., `'input.png'`).
- **`output_path`**: The path where the side-by-side image will be saved (e.g., `'result.png'`).
- **`n_colors`**: The number of colors to which the image will be reduced.

Experiment with different values for **`n_colors`** to see how it affects the output image.

## Notes
- Ensure that the image loaded is in RGB format.
- Make sure to experiment with different images and color values to observe the effect of quantization.