import cv2
import pytesseract

def get_camera_index():
    for i in range(10):  
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  
        if cap.isOpened():
            cap.release()
            return i
    return -1  
# Get a valid camera index
camera_index = get_camera_index()
if camera_index == -1:
    print("Error: No valid camera index found. Make sure your camera is connected and not in use by another application.")
    exit()

# Initialize webcam (or video stream)
cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    print("Error: Unable to access the camera. Try a different index or check permissions.")
    exit()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

frame_count = 0  # Initialize frame counter

while True:
    # Capture frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from the camera. Exiting.")
        break

    # Increment the frame count
    frame_count += 1

    # Process every 30th frame
    if frame_count % 30 == 0:
        # Convert the frame to grayscale for better OCR performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Optional: Apply thresholding to enhance text contrast
        _, processed_frame = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Perform OCR on the processed frame
        extracted_text = pytesseract.image_to_string(processed_frame, lang='eng')

        # Display the extracted text on the frame
        cv2.putText(frame, extracted_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the frame with the overlaid text
    cv2.imshow("Real-Time Text Extraction", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
