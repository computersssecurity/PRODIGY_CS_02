from PIL import Image

def caesar_encrypt(pixel, shift):
    r, g, b = pixel
    return (r + shift, g + shift, b + shift)

def caesar_decrypt(pixel, shift):
    r, g, b = pixel
    return (r - shift, g - shift, b - shift)

def encrypt_image(image_path, shift):
    original_image = Image.open("C:/Users/asus/Downloads/Image.jpg")
    encrypted_image = Image.new("RGB", original_image.size)

    for x in range(original_image.width):
        for y in range(original_image.height):
            original_pixel = original_image.getpixel((x, y))
            encrypted_pixel = caesar_encrypt(original_pixel, shift)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(image_path, shift):
    encrypted_image = Image.open(image_path)
    decrypted_image = Image.new("RGB", encrypted_image.size)

    for x in range(encrypted_image.width):
        for y in range(encrypted_image.height):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = caesar_decrypt(encrypted_pixel, shift)
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")

if __name__ == "__main__":
    image_path = "path/to/your/image.png"  
    shift_value = 10  

    encrypt_image(image_path, shift_value)
    decrypt_image("encrypted_image.png", shift_value)
