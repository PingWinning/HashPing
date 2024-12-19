# HashPing

![HashPing Logo](pingwining.jpg)

## Overview

**HashPing** is a professional hash verification tool designed for developers, cybersecurity experts, and individuals concerned with ensuring file integrity. Built with Python and a user-friendly graphical interface, HashPing simplifies the process of calculating and comparing file hashes, helping you verify authenticity and detect modifications effortlessly.

---

## Features

- **Hash Calculation**: Supports a wide range of hashing algorithms:
  - SHA256
  - MD5
  - SHA1
  - SHA3 (224, 256, 384, 512)
  - BLAKE2 (b, s)

- **Authenticity Verification**: Compare calculated hashes with user-provided values to verify file integrity.

- **Interactive GUI**:
  - Rounded profile image for a professional aesthetic.
  - Marquee-style message for announcements and support links.
  - "Copy" button to easily save calculated hashes to the clipboard.

- **Error Handling**: Provides user-friendly error messages for unsupported algorithms or file selection issues.

- **Elegant Design**: A polished interface ensures a smooth user experience.

---

## Installation

### Prerequisites
Ensure Python 3.7+ is installed on your system.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/PingWinning/HashPing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd HashPing
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python HashPing.py
   ```

---

## How to Use

1. **Select a File**:
   - Click "Choose File" to select the file you want to verify.

2. **Choose a Hash Algorithm**:
   - Select your preferred hashing algorithm from the dropdown list.

3. **Provide an Authentic Hash (Optional)**:
   - Enter a hash value to compare against the calculated hash.

4. **Calculate**:
   - Click "Calculate and Verify" to compute the file hash and verify its authenticity.

5. **Copy the Hash**:
   - Click the "Copy" button to save the calculated hash to your clipboard.

---

## Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Support

If you find HashPing helpful, consider supporting the project. Your contributions help us maintain and improve this tool.

- [Donate via PayPal](https://paypal.me/DimitarSimeonov17?country.x=CA&locale.x=en_US)

---

## Hash Information

### Python Script (HashPing.py)
- **SHA256**: `7fbb44e4d5b172b81845b6e7868251eb261487014b0397930073fe4dbab35a0b`
- **MD5**: `18f857810bbf2c890a82f5c1f6bf982c`

### Executable (HashPing.exe)
- **SHA256**: `a981d1bbdd52f7000d71dc598cacf50e0feb3e2f39ce9b68dd28deae2914931c`
- **MD5**: `19d23ca53836ddcfa328245de7d293ea`

**Note**: Other hashes may indicate that the file has been altered or is corrupted.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Thank you to the open-source community and all contributors who make projects like HashPing possible. Your support and feedback drive innovation and improvement.
