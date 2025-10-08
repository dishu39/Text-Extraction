
---

```
# 📝 Text Extraction

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Last Commit](https://img.shields.io/github/last-commit/amanpal02x/Text-Extraction?color=orange)  
![Repo Size](https://img.shields.io/github/repo-size/amanpal02x/Text-Extraction)  

Extract text seamlessly from images using **Python** and **Tesseract OCR**!  
This project allows you to convert scanned documents, photos, or any image containing text into **machine-readable text**, making it easier to process, search, and analyze.  

---

## ✨ Features
- 📷 **Image-to-Text Conversion** – Extract text from images in multiple formats (JPG, PNG, etc.)  
- 🌍 **Multilingual Support** – Works with many languages supported by Tesseract  
- 🎯 **Accurate OCR** – Utilizes Tesseract for reliable optical character recognition  
- ⚡ **Easy to Use** – Simple command-line interface for quick execution  

---

## 🚀 Getting Started

### 🔧 Prerequisites
Make sure you have the following installed:
- [Python 3.7+](https://www.python.org/downloads/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
- pip (Python package manager)

---

### 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/amanpal02x/Text-Extraction.git
   cd Text-Extraction
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure **Tesseract OCR** is installed and added to your system path.  
   - Windows: Add Tesseract installation path to your environment variables.  
   - Linux/macOS: Install via package manager (`sudo apt install tesseract-ocr` on Ubuntu).  

---

## ▶️ Usage

1. Place your input image(s) inside the project folder.  
2. Run the script:
   ```bash
   python extract_text.py --image sample.jpg
   ```
3. Extracted text will be printed in the terminal (and optionally saved to a file).  

Example:
```bash
python extract_text.py --image invoice.png --output result.txt
```

---

## 📸 Screenshots / Demo

Here’s how it works in action:  

**Input Image:**  
![Sample Input](Text-Extraction-main/Images/f4fe6fdeb3d5d0328b3e537977650135.webp)  

**Extracted Text Output:**  
![Extracted Output](Text-Extraction-main/Images/Screenshot 2025-10-08 110532.webp)  

## 📂 Project Structure
```
Text-Extraction/
│── extract_text.py    # Main script for OCR
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
└── screenshots/       # Screenshots for demo
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you’d like to improve the project.  

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).  

---

## 💡 Acknowledgments
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text recognition  
- [Pillow](https://python-pillow.org/) for image processing  
- Inspiration from open-source OCR projects  

---
```

---

