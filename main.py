import cv2
import numpy as np

# Set Image Path
path = "1.jpg"

# Set new width
new_width = 450

# Set Edge detection threshold
edge_th = 500

# Set Size detection threshold
size_th = 40

# Set Size Similarity threshold
sim_th = 200

# Set Text Font
font = cv2.FONT_HERSHEY_SIMPLEX

# Load the image
img = cv2.imread(path)

# Calculate the aspect ratio and new height
height, width, channels = img.shape
aspect_ratio = height / width
new_height = int(new_width * aspect_ratio)

# Resize the image with the calculated new height
image = cv2.resize(img, (new_width, new_height))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 100, edge_th)

# Find contours in the image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a list to store the areas of each shape
areas = []
aIndex = 0

# Loop through the contours and draw a rectangle and outline around each shape with an area > size_th
for i, contour in enumerate(contours):
    # Get the bounding box of the contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Compute the area of the shape
    area = cv2.contourArea(contour)
    
    # Only draw outline around shape with an area > size_th
    is_within_range = False
    for a in areas:
        if a - sim_th <= area <= a + sim_th:
            is_within_range = True
            break
    
    if not is_within_range:
        # Get the color for this shape (based on its index)
        color = tuple(map(int, np.random.choice(range(256), size=3)))
        
        # Draw an outline around the shape with the color
        cv2.drawContours(image, [contour], 0, color, 1)
        
        # Add text for the shape's ID and area
        cv2.putText(image, f"ID: {aIndex}", (x + 10, y - 40), font, 0.5, color, 1)
        cv2.putText(image, f"Area: {area}", (x + 10, y), font, 0.5, color, 1)
        
        # Determine shape type
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        
        if len(approx) == 3:
            cv2.putText(image, "Triangle", (x + 10, y - 20), font, 0.5, color, 1)
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            if 0.95 <= ar <= 1.05:
                cv2.putText(image, "Square", (x + 10, y - 20), font, 0.5, color, 1)
            else:
                cv2.putText(image, "Rectangle", (x + 10, y - 20), font, 0.5, color, 1)
        elif len(approx) > 4 and len(approx) < 8:
            cv2.putText(image, "Irregular", (x + 10, y - 20), font, 0.5, color, 1)
        else:
            cv2.putText(image, "Circle", (x + 10, y - 20), font, 0.5, color, 1)
        
        aIndex += 1
        areas.append(area)

# Determine the index of the largest and smallest shapes
largest_index = np.argmax(areas)
smallest_index = np.argmin(areas)

# Determine the number of shapes in the image
num_shapes = len(areas)

# State the number of shapes in the image and which is the largest and smallest
cv2.putText(image, f"Number of Shapes: {num_shapes}", (10, 20), font, 0.5, (150, 150, 0), 1)
cv2.putText(image, f"Largest Shape ID: {largest_index}", (10, 40), font, 0.5, (0, 255, 0), 1)
cv2.putText(image, f"Area: {areas[largest_index]}", (10, 60), font, 0.5, (0, 255, 0), 1)
cv2.putText(image, f"Smallest Shape ID: {smallest_index}", (10, 80), font, 0.5, (0, 0, 255), 1)
cv2.putText(image, f"Area: {areas[smallest_index]}", (10, 100), font, 0.5, (0, 0, 255), 1)

# Display the image with shapes outlined, rectangles, and information about the shapes
cv2.imshow('Image with Shapes Outlined and Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
