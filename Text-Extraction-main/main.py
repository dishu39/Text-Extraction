import os
import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image {image_path}")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    print("Extracted Text from Image:\n")
    print(text)


def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video")
        return

    frame_count = 0
    max_frames = 100 
    while True:
        ret, frame = cap.read()
        if not ret or frame_count >= max_frames:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        print("Extracted Text from Video Frame:")
        print(text)
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Video Frame with Text', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'): 
            break
        frame_count += 1
    
    cap.release()
    cv2.destroyAllWindows()



#image_path = r'I:\Project\mini project3\Images\inspirational-quotes-swl-241121-04-1ad49f.webp'
video_path = r'I:\Project\mini project3\Videos\1.mp4'

# Extract text from image
#extract_text_from_image(image_path)

# Extract text from video
extract_text_from_video(video_path)
