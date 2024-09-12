# Image Compression using KMeans

---

**To get credit for the assignment, please submit your code and results through the designated submission platform.**

**Goals**:

1. Learn how to apply KMeans clustering for image compression.
2. Implement basic image processing tasks.
3. Practice working with external libraries such as `scikit-learn`, `numpy`, and `Pillow`.
4. Understand how to manipulate images as NumPy arrays and perform color reduction.

**Working in pairs is allowed but not required.**

## Part 0: Setup Environment

1. Install Python 3.8 or higher: [link](https://python.org/downloads).
2. Install the required libraries:
    - From the terminal, run: `pip install numpy scikit-learn pillow`

## Part 1: Implementing Image Compression

1. **Complete the following functions in the provided script**:
    - `load_image(image_path)`: This function should load the image from a file and return it as a NumPy array. You will need to use the `Pillow` library for this task.
    - `image_compression(image_np, n_colors)`: Implement KMeans clustering using `scikit-learn` to reduce the number of colors in the image to `n_colors`. The function should return a compressed version of the image.
2. **Save the Compressed Image**: The function `save_result` has been provided for you. Once the original and compressed images are prepared, the function will save them side by side in a single image file.

## Part 2: Running Your Code

1. Modify the `__main__()` function to load the image, apply compression, and save the results. Make sure you provide paths for both input and output images.
2. Choose your favorite image as input and experiment with different values of `n_colors` (e.g., 4, 8, 16) and observe the effect on image quality.

## Example Workflow

1. Select your favorite image file (e.g., `'favorite_image.png'`) and place it in your working directory.
2. In the `__main__()` function:
    - Set `image_path` to your selected image file.
    - Set `output_path` to where you want to save the side-by-side result (e.g., `'compressed_image.png'`).
    - Choose an appropriate number of colors (`n_colors`), e.g., 8.
3. Run the script in your terminal:
   
   python image_compression.py

4. Check the output image to see the original and compressed versions side by side.

## Part 3: Submit Your Work

1. Submit the following files:
    - Your completed Python script.
    - The resulting image file(s) showing the original and compressed images.

## Notes:

1. Ensure that the image loaded is in RGB format.
2. Test with your favorite image and experiment with different values for `n_colors` to observe the impact of compression.
3. If you encounter issues loading or saving images, check the installation of `Pillow` and the file format compatibility.
