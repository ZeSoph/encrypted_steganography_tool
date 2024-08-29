import sys  # Add this import
from encryption import encrypt_message, generate_key
from steganography import encode_message_into_image, decode_message_from_image

DEFAULT_KEY = "mk_gt7WT9n-aqjvUsPT1uj3kl3u6WG0tFkimUvNigck="

def encode():
    if len(sys.argv) != 5:
        print("Usage: esteg hide <message> <image_path> <output_path>")
        sys.exit(1)
    
    secret_message = sys.argv[2]
    input_image_path = sys.argv[3]
    output_image_path = sys.argv[4]

    encrypted_message = encrypt_message(secret_message, DEFAULT_KEY)
    encode_message_into_image(encrypted_message, input_image_path, output_image_path)
    
    print(f"Message encoded successfully into {output_image_path}")

def decode():
    if len(sys.argv) != 4:
        print("Usage: esteg reveal <image_path> <output_path>")
        sys.exit(1)
    
    input_image_path = sys.argv[2]
    output_image_path = sys.argv[3]

    message = decode_message_from_image(input_image_path, DEFAULT_KEY)
    with open(output_image_path, 'w') as f:
        f.write(message)
    
    print(f"Message decoded successfully from {input_image_path} to {output_image_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: esteg <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "hide":
        encode()
    elif command == "reveal":
        decode()
    else:
        print(f"Unknown command: {command}")
