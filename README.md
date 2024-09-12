# Lab 2: Image Compression using KMeans

---

**To get credit for the lab, please show the completed work to a lab TA. They will check you off.**

**Goals**:

1. Learn how to apply KMeans clustering for image compression.
2. Implement basic image processing tasks.
3. Practice working with external libraries such as `scikit-learn`, `numpy`, and `Pillow`.

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

1. Select your favorite image file and place it in your working directory.
2. In the `__main__()` function:
    - Set `image_path` to your selected image file.
    - Set `output_path` to where you want to save the side-by-side result (e.g., `'compressed_image.png'`).
    - Choose an appropriate number of colors (`n_colors`), e.g., 8.
3. Run the script in your terminal:
   
``` bash
   python image_compression.py
```

4. Check the output image to see the original and compressed versions side by side.

## Notes:

1. Ensure that the image loaded is in RGB format.
2. Test with your favorite image and experiment with different values for `n_colors` to observe the impact of compression.
3. If you encounter issues loading or saving images, check the installation of `Pillow` and the file format compatibility.
