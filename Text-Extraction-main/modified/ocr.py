from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Open the image using Pillow
        image = Image.open(io.BytesIO(image_file.read()))
        # Use Tesseract OCR to extract text
        text = pytesseract.image_to_string(image)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
