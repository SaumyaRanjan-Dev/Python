## pip install opencv-python
import cv2

def capture_photo():
    # Open a connection to the camera (default is camera 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 's' to capture a photo, 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the live feed
        cv2.imshow('Live Feed', frame)

        # Wait for user input
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Save the captured frame
            filename = 'captured_photo.jpg'
            cv2.imwrite(filename, frame)
            print(f"Photo saved as {filename}")

        elif key == ord('q'):
            # Quit the loop
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_photo()
