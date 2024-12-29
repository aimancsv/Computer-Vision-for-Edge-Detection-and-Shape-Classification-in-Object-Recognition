# Computer-Vision-for-Edge-Detection-and-Shape-Classification-in-Object-Recognition
This Python script detects and classifies shapes in images. It resizes the image, applies Canny edge detection, and finds contours. Shapes are classified as Triangle, Square, Rectangle, Irregular, or Circle based on contour properties. The script annotates shapes with IDs, areas, and highlights the largest and smallest shapes. Uses OpenCV and NumPy

## Features
- **Resizes** the image to a specified width while maintaining aspect ratio.
- **Applies Canny edge detection** to highlight contours.
- **Detects and classifies shapes** (Triangle, Square, Rectangle, Irregular, Circle).
- **Annotates shapes** with ID and area.
- **Identifies largest and smallest shapes** in the image.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## 1. Input Image:
<img width="400" alt="Screenshot 2024-12-29 at 11 33 50 AM" src="https://github.com/user-attachments/assets/798d0918-da63-476a-8d6c-51a9f9fa1ca9" />

## 2. Convert to Grayscale Image and Gaussian Blur:
<img width="400" alt="Screenshot 2024-12-29 at 11 34 50 AM" src="https://github.com/user-attachments/assets/6d512f95-a942-4c4c-a0d9-922fd00efb14" />

## 3. Canny Edge Detection:

<img width="400" alt="Screenshot 2024-12-29 at 11 36 36 AM" src="https://github.com/user-attachments/assets/35cb4a56-cb62-49f2-b871-78f3f87752e5" />

## 4. Finding Contours and Area:
<img width="400" alt="Screenshot 2024-12-29 at 11 37 13 AM" src="https://github.com/user-attachments/assets/be235122-7fa6-45c3-892a-a3d8c9239a55" />

## 5. Output Image:

<img width="500" alt="Screenshot 2024-12-29 at 11 37 53 AM" src="https://github.com/user-attachments/assets/159afacc-505c-4a18-a3a3-fb085c691a10" />
