from setuptools import setup, find_packages

setup(
    name='encrypted-steganography-tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'esteg=cli:main',  # Ensure this points to the correct `main()` function in `cli.py`
        ],
    },
)
