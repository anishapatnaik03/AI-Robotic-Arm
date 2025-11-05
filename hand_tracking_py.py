import cv2
import mediapipe as mp
import serial
import time

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands
cap = cv2.VideoCapture(0)
hands = mphands.Hands()

# Open a serial connection to Arduino
try:
    ser = serial.Serial('COM5', 9600, timeout=1)  # Added timeout
    time.sleep(2)  # Wait for Arduino to initialize
    print("Serial connection established on COM5")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

try:
    while True:
        success, image = cap.read()  # Changed 'data' to 'success' for clarity
        
        if not success:
            print("Failed to capture image")
            continue
        
        # Flip and convert BGR to RGB for MediaPipe processing
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        
        # Convert back to BGR for OpenCV display
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks, 
                    mphands.HAND_CONNECTIONS)

                # Thumb detection logic (for right hand, flip for left)
                thumb_tip = hand_landmarks.landmark[4]
                thumb_ip = hand_landmarks.landmark[3]
                thumb_open = 1 if thumb_tip.x < thumb_ip.x else 0

                # Detection for other fingers
                finger_open = [thumb_open] + [
                    1 if hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y else 0
                    for i in [8, 12, 16, 20]  # Index, Middle, Ring, and Pinky fingers
                ]

                # Send data to Arduino
                message = ','.join(map(str, finger_open)) + '\n'
                ser.write(message.encode())

                # Print finger states
                print("Fingers Open:", finger_open)

        cv2.imshow('Hand Tracker', image)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Exiting...")

finally:
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
    print("Resources released successfully")
