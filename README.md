# Encrypted Steganography Tool

## Description
This tool allows you to encrypt a message and hide it inside an image using steganography. You can also extract and decrypt the hidden message from an image.

## Supported Formats
- PNG
- JPEG
- BMP

## Requirements
- Python 3.x
- `cryptography` library
- `Pillow` library

## Usage
### Hide a message:
```bash
python cli.py hide "Your secret message" input_image.png output_image.png
