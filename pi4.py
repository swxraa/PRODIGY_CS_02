from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Convert image to RGB mode
    img_rgb = img.convert("RGB")

    # Encrypt each pixel using XOR operation with the key
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img_rgb.getpixel((x, y))
            encrypted_r = r ^ key
            encrypted_g = g ^ key
            encrypted_b = b ^ key
            encrypted_pixels.append((encrypted_r, encrypted_g, encrypted_b))

    # Create a new image with the encrypted pixels
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size

    # Convert image to RGB mode
    img_rgb = encrypted_img.convert("RGB")

    # Decrypt each pixel using XOR operation with the key
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img_rgb.getpixel((x, y))
            decrypted_r = r ^ key
            decrypted_g = g ^ key
            decrypted_b = b ^ key
            decrypted_pixels.append((decrypted_r, decrypted_g, decrypted_b))

    # Create a new image with the decrypted pixels
    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")

# Example usage:
# Encrypt image
encrypt_image(r"C:\Users\vaibhav kadam\Downloads\Spidy.png", 128)

# Decrypt image
decrypt_image("encrypted_image.png", 128)

