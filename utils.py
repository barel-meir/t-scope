from PIL import Image

def replace_color(image_path, output_path, limit, output_color):
    print(f'handle: {image_path}')
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB mode (if it's not already)
        img = img.convert('RGB')
        # Get the image dimensions
        width, height = img.size
        # Iterate over each pixel in the image
        for y in range(height):
            for x in range(width):
                # Get the RGB values of the pixel
                r, g, b = img.getpixel((x, y))
                # Check if the pixel is black (R=0, G=0, B=0)
                if r < limit or g < limit or b < limit:
                    # Replace black pixels with yellow (R=255, G=255, B=0)
                    img.putpixel((x, y), output_color)
        # Save the modified image
        img.save(output_path)


# Example usage:
input_image_path = 'static/lion2_original.png'  # Replace with the path to your input image
output_image_path = 'static/lion2.png'  # Replace with the desired output image path
replace_color(input_image_path, output_image_path, 10, (33, 37, 41))
print("Image processing complete.")
