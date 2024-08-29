from PIL import Image

SUPPORTED_FORMATS = ["PNG", "JPEG", "BMP"]

def validate_image_format(image_path: str):
    try:
        image = Image.open(image_path)
        if image.format not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported image format: {image.format}. Supported formats: {SUPPORTED_FORMATS}")
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")
def encrypt_and_hide(message: str, image_path: str, output_image_path: str):
    validate_image_format(image_path)
    # ... (rest of the code)

def reveal_and_decrypt(image_path: str):
    validate_image_format(image_path)
    # ... (rest of the code)
