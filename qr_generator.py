"""
Hands-On Assignment 2: QR Code Generator
Course: Advanced Artificial Intelligence (MSCS-633-B01)

Description:
    Generate a QR code from a user-provided website URL
    and save the resulting image as a PNG file.
"""

from pathlib import Path
from urllib.parse import urlparse

import qrcode


def is_valid_url(url: str) -> bool:
    """Check whether the entered URL is a valid HTTP(S) URL."""
    parsed_url = urlparse(url)

    # Accept only web URLs with a hostname and no embedded spaces.
    return (
        parsed_url.scheme in ("http", "https")
        and bool(parsed_url.hostname)
        and " " not in url
    )


def generate_qr_code(
    url: str,
    filename: str = "biox_qr_code.png",
) -> Path:
    """Generate and save a QR code image for the given URL."""

    # Keep generated files in a dedicated output directory.
    output_directory = Path("output")
    output_directory.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)

    # Let qrcode choose the smallest QR version that fits the URL.
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    output_path = output_directory / filename
    image.save(str(output_path))

    return output_path


def main() -> None:
    """Run the QR code generator application."""

    print("=" * 50)
    print("       AI QR CODE GENERATOR - BIOX SYSTEMS")
    print("=" * 50)

    url = input("Enter the website URL: ").strip()

    if not is_valid_url(url):
        print("Error: Enter a valid URL starting with http:// or https://")
        return

    try:
        output_path = generate_qr_code(url)

        print("\nQR code generated successfully!")
        print(f"Website URL: {url}")
        print(f"Saved image: {output_path}")
        print("Scan the QR code using your phone to verify.")

    except (OSError, ValueError) as error:
        print(f"Failed to generate QR code: {error}")


if __name__ == "__main__":
    main()
