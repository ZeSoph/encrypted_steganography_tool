from PIL import Image
from encryption import decrypt_message  # Add this import

def encode_message_into_image(encrypted_message, input_image_path, output_image_path):
    image = Image.open(input_image_path)
    image = image.convert('RGB')

    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message) + '1111111111111110'
    pixels = image.load()
    width, height = image.size

    idx = 0
    for y in range(height):
        for x in range(width):
            if idx < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                image.save(output_image_path)
                return
    image.save(output_image_path)

def decode_message_from_image(input_image_path, key):
    image = Image.open(input_image_path)
    pixels = image.load()
    width, height = image.size

    binary_message = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)

    # Split binary into bytes and decode
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111110':  # End marker
            break
        message += chr(int(byte, 2))

    decrypted_message = decrypt_message(message, key)
    return decrypted_message
