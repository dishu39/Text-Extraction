import cv2
import pytesseract
import numpy as np

def get_camera_index():
    for i in range(10):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            cap.release()
            return i
    return -1

camera_index = get_camera_index()
if camera_index == -1:
    print("Error: No valid camera index found. Make sure your camera is connected and not in use by another application.")
    exit()
cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    print("Error: Unable to access the camera. Try a different index or check permissions.")
    exit()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 854)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

frame_count = 0 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from the camera. Exiting.")
        break

    frame_count += 1

   
    if frame_count % 30 == 0:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        processed_frame = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
        extracted_text = pytesseract.image_to_string(processed_frame, lang='eng', config='--psm 6')
        print("Extracted Text:", extracted_text)
        cv2.putText(frame, extracted_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Real-Time Text Extraction", frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
