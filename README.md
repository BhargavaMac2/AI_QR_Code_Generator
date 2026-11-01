
# AI QR Code Generator

## Project Overview
This project is a Python-based QR code generator developed
for Hands-On Assignment 2 in Advanced Artificial Intelligence
(MSCS-633-B01).

The application accepts a website URL, validates the input,
generates a QR code, and saves the output as a PNG image.

## Features
- Accepts HTTP and HTTPS URLs
- Performs basic URL validation
- Generates QR codes using Python
- Saves output as a PNG image
- Uses high QR error correction
- Includes basic exception handling

## Technologies
- Python 3.9.6
- qrcode 8.2
- Pillow 11.3.0
- Visual Studio Code

## Installation
1. Clone or download the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   python -m pip install -r requirements.txt

## Run the Application

   python qr_generator.py

Enter a URL when prompted.

## Example Input

https://www.bioxsystems.com/

## Expected Output

output/biox_qr_code.png

## Testing
Verify that the generated QR code scans to the input URL.

## Note
QR code generation uses an encoding algorithm and does
not require a trained machine-learning model.
